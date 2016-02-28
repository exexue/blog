from django.contrib import admin
from blog.models import Blog,Tag,Category

# Register your models here.

class blogadmin(admin.ModelAdmin):
	list_display = ('title','category','publish_time')


class categoryadmin(admin.ModelAdmin):
	list_display = ('name',)

class tagadmin(admin.ModelAdmin):
	list_display = ('tag_name',)

admin.site.register(Category,categoryadmin)				
admin.site.register(Tag,tagadmin)
admin.site.register(Blog,blogadmin)