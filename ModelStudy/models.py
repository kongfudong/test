from django.db import models


class Car(models.Model):
    manufacture = models.ForeignKey(
        'Manufacture',
        on_delete=models.CASCADE,
    )


class Manufacture(models.Model):
    pass


'''自己引用自己'''
class Comment(models.Model):
    title = models.CharField(max_length=100),
    text = models.TextField(),
    parent_comment = models.ForeignKey
        (
            'self',
            on_delete = models.CASCADE
        )


class Tag(models.Model):
    article = models.ForeignKey
    (
        Article,
        on_delete = models.CASCADE,
        releate_name = 'tag'
        releate_query_name = 'tag',
    )


class Person(models.Model):
    name = models.CharField(max_length=100),

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100),
    members = models.MangtoMangField(Person,through='membership')

    def __str__(self):
        return self.name