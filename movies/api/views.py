from django.shortcuts import render
from rest_framework.views import APIView,status
from .models import movies,MovieList
from .serializer import MovieSerializer,MovieModelSer,UserSerializer
from rest_framework.response import Response

# Create your views here.

# class Movielist(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response(data=movies)
#     def post(self,request,*args,**kwargs):
#         data=request.data
#         movies.append(data)
#         return Response(data=movies)
    
# class Moviesitem(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         movie=[i for i in movies if i['id']==id].pop()
#         return Response(data=movie)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("mid")
#         data=request.data
#         movie=[i for i in movies if i["id"]==id].pop()
#         movie.update(data)
#         return Response(data=movies)
#     def delete(self,*args,**kwargs):
#         id=kwargs.get("mid")
#         movie=[i for i in movies if i['id']==id].pop()
#         movies.remove(movie)
#         return Response(data=movies)


class MovieMList(APIView):
    def get(self,request,*args,**kwargs):
        mvs=MovieList.objects.all()
        dser=MovieModelSer(mvs,many=True)
        return Response(data=dser.data)
    def post(self,request,*args,**kwargs):
        mvs=request.data
        ser=MovieModelSer(data=mvs)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)
        
class MovieMItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        try:
            mv=MovieList.objects.get(id=id)
            dser=MovieModelSer(mv)
            return Response(data=dser.data)
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        try:
            mv=MovieList.objects.get(id=id)
            mv.delete()
            return Response({"msg":"ok"})
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        mv=MovieList.objects.get(id=id)
        ser=MovieModelSer(data=request.data,instance=mv)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
        
class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"registration Completed"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)