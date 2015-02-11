from django.contrib import admin

from url.models import Url

class urladmin(admin.ModelAdmin):
	pass

admin.site.register(Url, urladmin)
