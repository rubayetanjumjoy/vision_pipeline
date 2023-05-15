import jsonschema
from jsonschema import validate
import datetime
import base64
import json

# Define the JSON schema for the payload
schema = {
    "type": "object",
    "properties": {
        "device_id": {"type": "string"},
        "client_id": {"type": "string"},
        "created_at": {"type": "string", "format": "date-time"},
        "data": {
            "type": "object",
            "properties": {
                "license_id": {"type": "string"},
                "preds": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "image_frame": {"type": "string"},
                            "prob": {"type": "number"},
                            "tags": {"type": "array", "items": {"type": "string"}}
                        },
                        "required": ["image_frame", "prob", "tags"]
                    }
                }
            },
            "required": ["license_id", "preds"]
        }
    },
    "required": ["device_id", "client_id", "created_at", "data"]
}


# Validate timestamp
def validate_timestamp(timestamp) :
    try:
        timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
        return True
    except ValueError:
        return False


# Validate base64 image
def validate_base64(image_str):
    try:
        # Decode the string using base64 decoder and encode it back to check for errors
        return base64.b64encode(base64.b64decode(image_str)).decode() == image_str
    except Exception:
        return False
def is_json(data):
    try:
        json_object = json.loads(data)
        return True
    except ValueError:
        return False

# Validate the payload
def validate_payload(payload):
    try:
        
        if not is_json(payload):
            return False
        data=json.loads(payload)
        # Validate against JSON schema
        validate(instance=data, schema=schema)
        
        # Validate the timestamp format
        if not validate_timestamp(data["created_at"]):
            return False
        
        # Validate the base64 encoded images
        for pred in data["data"]["preds"]:
            
            if not validate_base64(pred["image_frame"]):
                return False
            
            
        return True
    
    except jsonschema.exceptions.ValidationError:
        return False
