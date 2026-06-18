from django.contrib import admin
from .models import *
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
  list_display =('name','slug')
  prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
  def image_tag (self,obj):
    if obj.image:
        return format_html('<img src="{}" width="45px" height="45px">',format(obj.image.url))
    return "بدون عکس"
    

  image_tag.short_description ='تصویر'

  list_display =('name','price','description','created_at','updated_at','available','image_tag')
  list_filter=['available','category','price','created_at','updated_at','available']
  search_fields=['name','description']
  list_editable=['price']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)

