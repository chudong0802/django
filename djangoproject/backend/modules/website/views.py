from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog,Project
from .serializers import BlogSerializer,ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse,HttpResponse
from django.conf import settings



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    # authentication_classes = (TokenAuthentication,)
    serializer_class = BlogSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



def writeFile(filePath, file):
    with open(filePath, "wb") as f:
        if file.multiple_chunks():
            for content in file.chunks():
                f.write(content)
        else:
            data=file.read() ###.decode('utf-8')
            f.write(data)


def uploadFile(request):
    if request.method == "POST": 
        fileDict = request.FILES.items()
        # 获取上传的文件，如果没有文件，则默认为None 
    if not fileDict:
        return JsonResponse({'msg': 'no file upload'})
    for (k, v) in fileDict:
        print("dic[%s]=%s" %(k,v))
        fileData = request.FILES.getlist(k)
        for file in fileData:
            fileName = file._get_name()
            filePath = os.path.join(settings.TEMP_FILE_PATH, fileName)
            print('filepath = [%s]'%filePath)
        try:
            writeFile(filePath, file)
        except:
            return JsonResponse({'msg': 'file write failed'})
    return JsonResponse({'msg': 'success'})
# if __name__ == "__main__":
#     uploadFile()
# Create your views here.
