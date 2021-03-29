from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
	class Meta:
		verbose_name='Статью'
		verbose_name_plural='Статьи'


	title = models.CharField(max_length=255, verbose_name='Название')
	body = models.TextField(verbose_name='Тело статьи')
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE,
		verbose_name='Автор'
	)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
	class Meta:
		verbose_name='Комментарий'
		verbose_name_plural='Комментарии'

	article = models.ForeignKey(
		Article, 
		on_delete=models.CASCADE,
		verbose_name='Статья'
	)
	comment = models.CharField(
		max_length=150,
		verbose_name='Комментарий',
	)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		verbose_name='Автор',
	)

	def __str__(self):
		return self.comment


	def get_absolute_url(self):
		return reverse('article_list')