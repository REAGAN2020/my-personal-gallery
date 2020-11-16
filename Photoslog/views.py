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
    return render(request, "single_image.html", {'title': title, "image": image, "locations": locations, "image_category": image_category})

def search_photo(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'Image_category' in request.GET and request.GET['Image_category']:
        search = request.GET.get('Image_category')
        found_results = Image.search_by_category(search)
        message = f"{search}"
        print(search)
        print(found_results)

        return render(request, 'search_photo.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search_photo.html',{"message": message})