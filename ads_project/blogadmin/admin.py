from django.contrib import admin
from adsAPI.models import Ads

# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = "softio admin panel"
    # index_template = "admin/base_site.html"
    index_template = "panel-finall.html"
    login_template = 'login.html'

    def index(self, request, extra_context=None):
        print(str(request.user))
        context = {"ads_list":list(Ads.objects.all().filter(user=request.user).values())}
        print(str(request))
        print(str(request))
        extra_context = extra_context or context
        print(extra_context)
        # Add your context here
        return super(BlogAdminArea, self).index(request, extra_context)


blog_site = BlogAdminArea(name="blogpanel")
