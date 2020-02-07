from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','realtor','listing_date')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published',)
    search_fields=('title','city','state','zip',)
    list_par_page=25
admin.site.register(Listing,ListingAdmin)
