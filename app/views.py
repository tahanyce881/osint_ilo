from django.shortcuts import render

def index(request):
    return render(request,'osint.html',{})

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Param
from .serializers import ParamSerializer

class ParamTreeView(APIView):
    def get(self, request):
        params = Param.objects.all()
        serializer = ParamSerializer(params, many=True)
        
        # Transforming data to match the desired JSON structure
        json_data = {
            "name": "Osint ilo program",
            "type": "folder",
            "children": []
        }

        for param in serializer.data:
            children = {
                "name": param['title'],
                "type": "folder",
                "children": []
            }
            for sub_param in param['sub_params']:
                sub_children = {
                    "name": sub_param['title'],
                    "type": "folder",
                    "children": []
                }
                for server_param in sub_param['server_params']:
                    sub_children['children'].append({
                        "name": server_param['title'],
                        "type": "url",
                        "url": server_param['description']  # Assuming the description is a URL
                    })
                children['children'].append(sub_children)
            json_data['children'].append(children)

        return Response(json_data)