from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    aut_number= PhoneNumberField(null=False,blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    subtitle1 = models.CharField(max_length=200)
    paragraphe1 = models.TextField()
    subtitle2 = models.CharField(max_length=200,blank=True)
    paragraphe2 = models.TextField(blank=True)
    subtitle3 = models.CharField(max_length=200,blank=True)
    paragraphe3 = models.TextField(blank=True)
    subtitle4 = models.CharField(max_length=200,blank=True)
    paragraphe4 = models.TextField(blank=True)
    subtitle5  = models.CharField(max_length=200,blank=True)
    paragraphe5 = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images',blank=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

