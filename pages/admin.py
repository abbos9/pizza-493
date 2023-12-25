from django.contrib import admin
from pages.models import  ScrollModel, GalleryModel, MenuModel, Reservation, CategoryModel
# Register your models here.


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount','created_at']
    search_fields = ['title', 'description','id']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']

@admin.register(Reservation)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name', 'message','id']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']

@admin.register(GalleryModel)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at'] 


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','price','created_at']
    list_filter = ['created_at','updated_at']
    ordering = ['-created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ['created_at','updated_at']
    search_fields = ['title']
    ordering = ['-created_at']