from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from accounts.models import CustomUser

from django.contrib.auth.decorators import login_required

from articles.models import Article



# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"




class Profile(TemplateView):
    template_name= "profile.html"

# @login_required
# def AllPosts(request):
#     logged_in_user=request.user
#     logged_in_user_posts= Article.objects.filter(author=logged_in_user)

#     return render(request, 'all_post_by_user.html', {'posts': logged_in_user_posts},)

class AllPosts(ListView):
    model= Article
    template_name="all_post_by_user.html"
    context_object_name="posts"
    ordering= ["-date"]
    # def get_queryset(self):
    #     self.logged_in_user=self.request.user
    #     self.logged_in_user_posts= Article.objects.filter(author=self.logged_in_user)
    #     return self.logged_in_user_posts
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        self.logged_in_user=self.request.user
        self.logged_in_user_posts= Article.objects.order_by("-date").filter(author=self.logged_in_user)
        context['posts'] = self.logged_in_user_posts
        return context