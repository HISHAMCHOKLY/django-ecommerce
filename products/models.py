from django.db import models
from django.utils.text import slugify

# Create your models here.

CHOICES =(
    ("new", "new"),
    ("cancel", "cancel")
)

class Products(models.Model):
    p_name=models.CharField(max_length=200)
    p_category=models.CharField(max_length=100)
    p_brand=models.CharField(max_length=100)
    p_img=models.ImageField(upload_to='pics')
    p_des=models.TextField()
    p_price=models.FloatField()
    p_offer=models.BooleanField(default=False)
    # slug = AutoSlugField(populate_from=('p_name',), prefix_from=('p_category',), unique=True, max_length=255, overwrite=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self,*args,**kwargs ) :
        if self.slug is None:
            self.slug='-'.join((slugify(self.p_name), slugify(self.p_des)))
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.p_name

class Cart(models.Model):
    p_id=models.ForeignKey('Products',on_delete=models.CASCADE)    
    qty=models.IntegerField()
    
    @property
    def p_name(self):
        return self.p_id.p_name
    @property
    def p_img(self):
        return self.p_id.p_img
    @property
    def p_price(self):
        return self.p_id.p_price        

class Reviews(models.Model):
    p_id=models.IntegerField()
    p_rating=models.IntegerField()
    p_review=models.CharField(max_length=200)    


class Orders(models.Model):
    p_id=models.IntegerField()
    p_img_url=models.URLField(max_length=200)
    p_name=models.CharField(max_length=200)
    p_price=models.FloatField()
    p_date=models.DateField()
    p_qty=models.IntegerField()  
    p_total=models.FloatField()
    p_status=models.BooleanField(default=True)
    status=models.CharField(max_length=200,choices=CHOICES,default='new')
    def __str__(self) -> str:
        return self.p_name

