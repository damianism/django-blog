from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# PLACE VIEW FUNCTIONS HERE!

def get_posts(request):
    """
    Create a view that returns a list of posts that were published 
    pior to "now" and then render them to the "blogposts.html" template!
    """
    
    
    # filter all the posts in db that are "larger and equal"(__lte) to "timezone.now()" - timezone.now() being the current time
    # order the filtered posts by "published_date" and in a decsending order "-published_date" - "-" at the beginning 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date") # ignore the memeber c9 error
    
    return render(request, "blogposts.html", {"posts":posts})
    
    
def post_detail(request, pk):
    """
    Create a view that returns a SINGLE "Post object" based on the post ID (pk) and
    render it to the "postdetail.html" template.
    or
    return a 404 error if the post is not found!
    """
    
    # get the Post object using its ID (pk), otherwise return a 404 error 
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    
    return render(request, "postdetail.html", {"post": post})
    
    
def create_or_edit_post(request, pk=None):
    """ 
    Create a view that allows us to create or edit a single post depending if 
    its Post ID is null or not!
    
    using form data to edit db
    """
    

    # if pk:
    #     post = get_object_or_404(Post, pk)
    # else:
    #     post = None
    # as shown above if pk is not given set post to None
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == "POST":
        # https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
        # request.FILES:    a dictionary containing a key for each FileField (or ImageField, or other FileField subclass) in the form. 
        #                   So the data from the above form would be accessible as request.FILES['file'].
        # instance? why? BlogPostForm is already based on the Post model
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()  # doesnt this save the form onject in the db? why is it equating it to post? post doesnt even get used after that!
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
        
    return render(request, "blogpostform.html", {"form":form})

