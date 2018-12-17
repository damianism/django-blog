from django import forms
from . import models    # alternative - from .models import Post


# inheritance (difference between "forms.Form" and "forms.ModelForm")
    # https://stackoverflow.com/questions/2303268/djangos-forms-form-vs-forms-modelform
    # "forms.Form" - are usually suitable for forms not interactiing directly with the database - e.g. contact form
    # class inherits from "forms.ModelForm"  - froms from forms.ModelForm will be automatically created and then can later be tweaked by you. 

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = models.Post # alternative - model = Post
        fields = ('title', 'content', 'image', 'tags', 'published_date')
        # note: "views" and "created_date" were left out since they're not user edittable!
        #       only add fields to the form that the user can actually edit