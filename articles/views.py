from django.shortcuts import render
from .scrapers import Pixnet


def index(request):

    pixnet = Pixnet(None)

    if request.method == "POST":
        pixnet = Pixnet(request.POST.get("restaurant_name"))  # 取得查詢條件

    context = {
        "articles": pixnet.get_articles()
    }

    return render(request, "articles/index.html", context)
