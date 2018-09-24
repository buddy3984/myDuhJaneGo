from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Song


def buddymainredirect(request):
    return redirect('/buddy')


def index(request):
    all_albums = Album.objects.all()
    all_songs = Song.objects.all()
    context = {
        'all_albums': all_albums,
        'all_songs': all_songs,
    }
    return render(request, 'buddy/index.html', context)


def detail(request, poo, var):
    spooge = get_object_or_404(Album, pk=var)
    return render(request, 'buddy/detail.html', {'var_album': spooge, 'var_artist': poo})


def favorite(request, album_id):
    spooge = get_object_or_404(Album, pk=var)
    try:

