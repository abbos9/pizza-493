from django.db import models

# Create your models here.

# RESERVATION

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ='reservation'
        verbose_name_plural ='reservations'

# SCROLL

class ScrollModel(models.Model):
    image = models.ImageField(upload_to='scroll/')
    discount = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls'



# GALLERY

class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'

# CATEGORY

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True,)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



# MENU
        

class MenuModel(models.Model):
    image = models.ImageField(upload_to='menu/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='menu',null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'