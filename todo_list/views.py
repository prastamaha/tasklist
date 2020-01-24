from django.shortcuts import render, redirect
from .models import List
from .forms import ListForms
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ListForms(request.POST or None)

        if form.is_valid():
            form.save()
            db = List.objects.all
            messages.success(request, ('Task was successfully added to the list'))
            return render(request, 'home.html', {'db': db})

    else:
        db = List.objects.all
        return render(request, 'home.html', {'db': db})

def about(request):
    return render(request, 'about.html', {})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Task was deleted'))
    return redirect('home')

def finish(request, list_id):
    item = List.objects.get(pk=list_id)
    item.status = True
    item.save()
    return redirect('home')

def unfinish(request, list_id):
    item = List.objects.get(pk=list_id)
    item.status = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    item = List.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ListForms(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task was Updated'))
            return redirect('home')

    else:
        return render(request, 'edit.html', {'item':item})