from django.shortcuts import render,get_object_or_404

from .models import Contact
from .serializer import ContactSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class ContactlistAPIView(APIView):
    def get(self,request):
        try:
            contacts=Contact.objects.all()
            serializer=ContactSerializer(contacts,many=True)
            return Response(serializer.data)
        except:
            return Response({'status':'something went wrong'})









class ContactUpdateAPIlist(APIView):
    def put(self,request,pk):
        try:
            contact=Contact.objects.get(pk=pk)
            serializer=ContactSerializer(contact,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})


    def patch(self,request,pk):
        try:
            contact=Contact.objects.get(pk=pk)
            serializer=ContactSerializer(contact, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})








class ContactDeleteAPIView(APIView):
    def delete(self,request,pk):
        contact=get_object_or_404(Contact,pk=pk)
        contact.delete()
        return Response({'status':"contact deleted successfully"})







class ContactCreateAPIView(APIView):
    def post(self,request):
        malumotlar=request.data
        serializer=ContactSerializer(data=malumotlar)
        if serializer.is_valid():
            serializer.save()
            info={
                'status':'contact created successfully',
                'they are':serializer.data
            }
            return Response(info)
        else:
            return Response({'status':'something '})




class ContactDetailAPIView(APIView):
    def get(self,request,pk):
        contact=get_object_or_404(Contact,pk=pk)
        serializer=ContactSerializer(contact)
        return Response(serializer.data)







class ContactMixedAPIView(APIView):
    def put(self,request,pk):
        try:
            contact=Contact.objects.get(pk=pk)
            serializer=ContactSerializer(Contact,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})


    def putch(self,request,pk):
        try:
            contact=Contact.objects.get(pk=pk)
            serializer=ContactSerializer(contact, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status':'serializer is not available'})
        except:
            return Response({'status':'bunday id li contact mavjud emas'})

    def get(self,request,pk):
        contact=get_object_or_404(Contact,pk=pk)
        serializer=ContactSerializer(contact)
        return Response(serializer.data)


    def delete(self,request,pk):
        contact=get_object_or_404(Contact,pk=pk)
        contact.delete()
        return Response({'status':"contact deleted successfully"})

