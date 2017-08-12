from django.contrib import admin
from blog.models import *
from django.contrib.auth.admin import UserAdmin  

class BookAdmin(admin.ModelAdmin):
	search_fields=('title',)
	list_display=('title','publication_date')
	list_filter=('publication_date','title')
	date_hierarchy='publication_date'
	ordering=('publication_date',)

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)
admin.site.register(Server_db)
admin.site.register(Disk_info)
