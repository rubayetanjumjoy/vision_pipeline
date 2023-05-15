from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .producer import publish
from .utils import validate_payload
import json

 
    
class SnapApiView(APIView):
   
    def get(self, request):
        
        text='A simple web-service that accepts a POST request with a JSON body'
        return Response({"messege":text})

    def post(self, request):
        data = request.body
        
        
        if validate_payload(data):
            data=json.loads(data)
            for pred in data["data"]["preds"]:
    
                if pred['prob']<0.25:
                    pred['tags'].append('low_prob')
            publish(data)
            return Response({'message': 'Message published successfully'},status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Unsupported content type'},status=status.HTTP_406_NOT_ACCEPTABLE)
        

        
        
        
        

        
    



    