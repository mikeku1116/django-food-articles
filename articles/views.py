from django.shortcuts import render
from .scrapers import Pixnet


def index(request):

    pixnet = Pixnet("千葉火鍋")

    context = {
        "articles": pixnet.get_articles()
    }

    return render(request, "articles/index.html", context)
