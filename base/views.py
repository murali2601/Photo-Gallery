from django.shortcuts import render,redirect
from .models import *
# Create your views here.



def home(request):
    data = request.GET.get('category')

    if data != None:
        photo = Photo.objects.filter(category__name=data)
    else:
        photo = Photo.objects.all()


    categories = Category.objects.all()
    #photo = Photo.objects.all()
    context = {'categories' : categories,'photo' : photo}
    return render(request, 'base/home.html',context)

def form(request):
    categories = Category.objects.all()
    photo = Photo.objects.all()

    if request.method == 'POST':
        data = request.POST
        img = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != 'none':
            category, created = Category.objects.get_or_create(
                name=data['category_new']
            )
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = img,
        )

        return redirect('home')
    

    context = {'categories' : categories,'photo' : photo}
    return render(request, 'base/form.html',context)
    