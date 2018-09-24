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
    return render(request, 'buddy/detail.html', {
        'var_album': spooge,
        'var_artist': poo,
    })


def favorites(request, poo, var):
    spooge = get_object_or_404(Album, pk=var)
    try:
        buddyssong = spooge.song_set.get(pk=request.POST['da song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'buddy/detail.html', {
            'var_album': spooge,
            'errr_message': "you fuck up bitch! you lost?"
        })
    else:
        buddyssong.is_favorite = True
        buddyssong.save()
        return render(request, 'buddy/detail.html', {
            'var_album': spooge,
            'var_artist': poo,
        })
