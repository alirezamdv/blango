from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})