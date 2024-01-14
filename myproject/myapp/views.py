from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the beginning of something wonderful.")

def handle_image_upload(request):
    if request.method == 'POST' and request.FILES['image']: # this corresponds to the name given in front end code, TODO: create name to match
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url
    
