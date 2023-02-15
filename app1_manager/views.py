from django.shortcuts import render
from django.http import HttpResponse
from app1_manager.models import Post
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app1_manager.serializers import PostSerializer
# Create your views here.
@csrf_exempt
def simpleApi(request, id=0):
    if request.method =='GET':
        post = Post.objects.al1()
        post_serializer=PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)
    elif request.method == 'POST':
        post_data=JSONParser().parse(request)
        post_serializer=PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Added Successfully" ,safe=False)
        return JsonResponse("Failed to Add")
    elif request. method == 'PUT':
        post_data=JSONParser().parse(request)
        post = Post.objects.get(Title=post_data['Title'], Image=post_data['Image'], User=post_data['User'])
        post_serializer=PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Update Successfully" ,safe=False)
        return JsonResponse("Failed to Update")
    elif request. method== 'DELETE':
        post=Post.objects.get(Title = id)
        post.delete()
        return JsonResponse("Deleted Successfully",safe=False)


def simple(request):
    obj = Post.objects.all()
    return render(request, 'simple.html',{'obj': obj})