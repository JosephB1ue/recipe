from django.shortcuts import render, redirect
from .models import Recipes
def index(request):
    if request.method=='POST':
        search=request.POST['search']
        data=Recipes.objects.filter(title=search)
        return render(request,'searchresult.html',{'data': data})
    object = Recipes.objects.all()
    return render(request,'index.html', {'data': object})

def addrecipe(request):
    if request.method == 'POST':
        images = request.FILES['image']
        title = request.POST['title']
        ingredients = request.POST['ingredients']
        description = request.POST['description']
        instructions = request.POST['instructions']
        obj= Recipes.objects.create(pic=images, title=title, ingredients=ingredients, description=description, instructions=instructions)
        obj.save()
        if obj:
            return render(request, 'addrecipe.html', {'message':'New recipee added successfully'})
        else:
            return render(request, 'addrecipe.html', {'message':'Failed to add recipe'})
    return render(request,'addrecipe.html')

# def search(request,pk):
#     obj= Recipes.objects.get(id=pk)
#     return render(request,'searchresult.html',{'data':obj})

    
# Create your views here.
