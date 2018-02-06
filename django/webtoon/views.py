from django.shortcuts import render
from .models import *


def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    context = {'webtoons': webtoons}
    return render(request, 'webtoon/webtoons_list.html', context)


def webtoon_detail(request, webtoon_id):
    episodes = Episode.objects.filter(webtoon_id=webtoon_id)
    context = {'episodes': episodes}

    return render(request, 'webtoon/webtoons_detail.html', context)

