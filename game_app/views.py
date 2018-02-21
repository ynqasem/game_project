from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Game
from .forms import GameForm

def game_list(request):
	games_list = Game.objects.all()
	query = request.GET.get('q')
	if query:
		games_list = games_list.filter(name__contains=query)
	context = {
	"title": "List",
	"games_list": games_list,
	}
	return render(request,'list.html', context)

def game_detail(request, game_id):
	instance = Game.objects.get(id= game_id)
	context = {
	"title": "Detail",
	"instance": instance,
	}
	return  render(request, 'detail.html', context)

def game_create(request):
	form = GameForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("gamelist")
	context = {
	"title": "Create",
	"form": form,
	}
	return render(request, 'create.html', context)

def game_update(request, game_id):
	instance = get_object_or_404(Game, id=game_id)
	form = GameForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("gamelist")
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}

	return render(request, 'update.html', context)

def game_delete(request, game_id):
	instance = get_object_or_404(Game, id=game_id)
	instance.delete()
	return redirect("gamelist")
