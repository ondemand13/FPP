from django.shortcuts import render
from adminportal.serialization import AdminSerializationClass
from rest_framework.decorators import api_view
from rest_framework.response import Response
from FPPMS.models import Proposalmodel

@api_view(['GET']) 
def displayProposal(request):
    if request.method=='GET':
        results=Proposalmodel.objects.all()
        serialize=AdminSerializationClass(results,many=True)
        return Response(serialize.data)


