from django.shortcuts import render
from .models import Article, Comment, Hashtag
# Create your views here.


def index(request):
    category = request.GET.get("category")

    if not category:
        article_list = Article.objects.all()
    else:
        article_list = Article.objects.filter(category=category)
    hashtag_list = Hashtag.objects.all()

    # category_list = set([
    #     article.get_category_display()
    #     for article in article_list
    # ])

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])
    print(category_list)
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # # print(category_list)

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

    pass


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    hashtag_list = Hashtag.objects.all()
    ctx = {
        "article" : article,
        "hashtag" : hashtag_list,
    }
    return render(request, "detail.html", ctx)



# def about(request):
#     pass