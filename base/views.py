from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.



def home(request):
    categories = Category.objects.all()
    data = request.GET.get('category')
    delete = request.GET.get('delete')


    if data != None:
        photo = Photo.objects.filter(category__name=data)
    else:
        photo = Photo.objects.all()



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
            title = data['title'],
            description = data['description'],
            image = img,
        )

        return redirect('home')
    

    context = {'categories' : categories,'photo' : photo}
    return render(request, 'base/form.html',context)
    

def delete(request,pk):
    categories = Category.objects.get(id=pk)
    photo = Photo.objects.get()

    if request.method == 'POST':
        categories.delete()
        return redirect('home')
    
    context = {'obj': photo.title}

    return render(request, 'base/delete.html',context)

#------------- testing purpose only -----------------

def test(request):
    form = PhotoForm()

    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request,'base/test.html',context)