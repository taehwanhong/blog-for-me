from django.db import models

# Create your models here.
# 기획에 따라 클래스 부터 설정함


class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}글의 댓글 {}".format(self.article.title, self.content)


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name