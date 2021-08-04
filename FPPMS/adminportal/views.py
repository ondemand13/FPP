from django.shortcuts import render
import rest_framework
from adminportal.serialization import AdminSerializationClass
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from FPPMS.models import Proposalmodel
from django.shortcuts import render
from rest_framework import status
import requests

@api_view(['GET']) 
def displayProposal(request):
    if request.method=='GET':
        results=Proposalmodel.objects.all()
        serialize=AdminSerializationClass(results,many=True)
        return Response(serialize.data)

def displayProposalList(request):
    callapi = requests.get('http://127.0.0.1:8000/displayProposal')
    results = callapi.json()
    return render(request,'proposals.html',{'Proposalmodel': results})

  
def addAdmin(request):
    return render(request, "addAdmin.html")
    
def dashboard(request):
    return render(request, "dashboard.html")

class ProposalUpdate(APIView):

    def get_object(self,pk):
        try:
            return Proposalmodel.objects.get(pk=pk)
        except Proposalmodel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        results=self.get_object(pk)
        serialize=AdminSerializationClass(results)
        return Response(serialize.data)
    
    def put(self,request,pk):
        results=self.get_object(pk)
        serialize = AdminSerializationClass(results,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        results=self.get_object(pk)
        results.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


