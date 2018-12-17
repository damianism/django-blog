from django.db import models
from django.utils import timezone

# models.Model being the STANDARD model! - so Post inherits from an standard model (imported through "models")
class Post(models.Model):
    """ Definition of a single blog post """
    
    # defining what the model needs using the imported "models"
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) # add the current date and time whenever the record is created!
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)  # starts off BLANK, nulls will be allowed by defualt it will be current time from timezone!
    views = models.IntegerField(default=0)
    tags = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True) # the "img" corresponds to the "media/img" directory, the image folder inside the media directory
    
    
    def __unicode__(self):
        return self.title
    