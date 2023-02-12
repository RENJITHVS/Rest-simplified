from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer , StudentModelSeralizer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse  ,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io

from django.utils.decorators import method_decorator
from django.views import View

#fuction based api-views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#class based api_views
from rest_framework.views import APIView



# Model object - single Student Data
def student_detail(request, pk):
    student = Student.objects.get(id = pk)
    serializer = StudentSerializer(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type ='application/json')
    return JsonResponse(serializer.data, content_type = 'application/json')

#queryset - All student Data
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type ='application/json')

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seralizser = StudentSerializer(data = pythondata)  
        if seralizser.is_valid():
            seralizser.save()
            res = {'msg': "Data created"}
            return JsonResponse(res, content_type = 'application/json')
        return JsonResponse(seralizser.errors, content_type = 'application/json')

#function based view
@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id = id)
            serilaizer = StudentSerializer(student)
            json_data = JSONRenderer().render(serilaizer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            student = Student.objects.all()
            serilaizer = StudentSerializer(student, many= True)
            json_data = JSONRenderer().render(serilaizer.data)
            return HttpResponse(json_data, content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seralizser = StudentSerializer(data = pythondata)
        if seralizser.is_valid():
            seralizser.save()
            res = {'msg': "Data created"}
            return JsonResponse(res, safe=False)
        return JsonResponse(seralizser.errors, content_type = 'application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        seralizser = StudentSerializer(student, data = pythondata, partial = True) # if not partials then it updated completely
        if seralizser.is_valid():
            seralizser.save()
            res = {'msg':'Data Updated !!'}
            return JsonResponse(res, content_type = 'application/json')
        return JsonResponse(seralizser.errors, content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg': "data deleted !!"}
        return JsonResponse(res, content_type = 'application/json')

#class Based View
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id = id)
            serilaizer = StudentModelSeralizer(student)
            json_data = JSONRenderer().render(serilaizer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            student = Student.objects.all()
            serilaizer = StudentSerializer(student, many= True)
            json_data = JSONRenderer().render(serilaizer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seralizser = StudentSerializer(data = pythondata)
        if seralizser.is_valid():
            seralizser.save()
            res = {'msg': "Data created"}
            return JsonResponse(res, safe=False)
        return JsonResponse(seralizser.errors, content_type = 'application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        seralizser = StudentModelSeralizer(student, data = pythondata, partial = True) # if not partials then it updated completely
        if seralizser.is_valid():
            seralizser.save()
            res = {'msg':'Data Updated !!'}
            return JsonResponse(res, safe=False)
        return JsonResponse(seralizser.errors, content_type = 'application/json')


#Function Based Api_view
@api_view(['GET','POST'])
def hello_word(request):
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'This is post request'})
    
    if request.method == "GET":
        return Response({'msg': "this is a get value"})

@api_view(['GET','POST','PUT','DELETE', 'PATCH'])
def student_api_fn(request, id = None):
    if request.method == "POST":
        serializser = StudentModelSeralizer(data = request.data)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg': "New Data Added"}, status=status.HTTP_201_CREATED)
        return Response(serializser.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        # id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializser = StudentSerializer(stu)
            return Response(serializser.data)
        stu = Student.objects.all()
        serializser = StudentSerializer(stu, many= True)
        return Response(serializser.data)

    if request.method == "PUT":
        stu = Student.objects.get(id = id)
        serializser = StudentSerializer(stu,data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg':'Data Updated'})
        return Response(serializser.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        # id = request.data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({"msg": "Data deleted"})

    if request.method == "PATCH":
        stu = Student.objects.get(id = id)
        serializser = StudentSerializer(stu,data=request.data, partial=True)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg':'Data Updated Partially'})
        return Response(serializser.errors, status= status.HTTP_400_BAD_REQUEST)
       
#Class Based Api_view
class StudentClassAPI(APIView):
    
    def get(self, request, id = None, format=None):
        #format = None , means we can add suffix to url.
        if id is not None:
            stu = Student.objects.get(id = id)
            serializser = StudentSerializer(stu)
            return Response(serializser.data)
        stu = Student.objects.all()
        serializser = StudentSerializer(stu, many= True)
        return Response(serializser.data)

    def post(self, request, format = None):
        serializser = StudentModelSeralizer(data = request.data)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg': "New Data Added"}, status=status.HTTP_201_CREATED)
        return Response(serializser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,id=None, format=None):
        stu = Student.objects.get(id = id)
        serializser = StudentSerializer(stu,data=request.data)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg':'Data Updated'})
        return Response(serializser.errors, status= status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None, format=None):
        stu = Student.objects.get(id = id)
        serializser = StudentSerializer(stu,data=request.data, partial=True)
        if serializser.is_valid():
            serializser.save()
            return Response({'msg':'Data Updated Partially'})
        return Response(serializser.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None, format=None):
        stu = Student.objects.get(id = id)
        stu.delete()
        return Response({"msg": "Data deleted"})

