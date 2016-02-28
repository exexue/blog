from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name
		
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
   

    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    #tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + str(self.publish_time)

    class Meta:
        ordering = ['-publish_time']

	


