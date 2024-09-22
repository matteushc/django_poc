from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from .serializers import AppClientSerializer
from .models import AppClient
import datetime
import requests
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from pypdf import PdfReader, PdfWriter


URL = "https://jsonplaceholder.typicode.com"


class LogsViewSet(viewsets.ModelViewSet):
    queryset = AppClient.objects.all().order_by('postId')
    serializer_class = AppClientSerializer


class IndexView(generic.ListView):
    model = AppClient
    template_name = 'base.html'
  
    def get_queryset(self):
        return AppClient.objects.all()


class LogsView(generic.TemplateView):

    def get(self,request):
        data_atual = datetime.datetime.now()
        data_atual = data_atual.strftime("%Y-%m-%d")
        url = f'{URL}/comments'
        r = requests.get(url)
        logs = r.json()
        logs_list = {'logs_list': logs}
        return render(request,'buscar.html',logs_list)


@login_required(login_url='/')
def your_view(request):

    if request.method == 'GET':

        search_box = request.GET.get('search_box', None)    
        url = f'{URL}/comments'
        if search_box:
            url = f'{URL}/comments?postId={search_box}'
        r = requests.get(url)
        logs = r.json()
        logs_list = {'logs_list': logs}
        return render(request,'buscar.html',logs_list)
    

@login_required(login_url='/')
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        # Do something with the uploaded file
        # for chunk in uploaded_file.chunks():
        #     print(chunk)
        
        bytes_stream = BytesIO(uploaded_file.read())
        
        reader = PdfReader(bytes_stream)
        page = reader.pages[0]
        # extracting text from page
        text = page.extract_text()
        print(text)
        
        # fs = FileSystemStorage()
        # filename = fs.save(uploaded_file.name, uploaded_file)
        # filename = fs.url(filename)

        return render(request, 'upload_success.html', {'file_name': uploaded_file.name})
    else:
        return render(request, 'upload_file.html')