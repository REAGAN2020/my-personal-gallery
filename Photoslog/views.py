from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.


def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'TefPics'

    return render(request, 'index.html', {'title': title, 'images': images, 'locations': locations})

def single_image(request,category_name,image_id):
    title = 'Image'
    locations = Location.objects.all()
    image_category = Image.objects.filter(Image_category__name = category_name)
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_image.html",{'title':title,"image":image, "locations":locations, "image_category":image_category})