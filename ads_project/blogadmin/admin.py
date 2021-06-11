from django.contrib import admin


# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = "softio admin panel"
    # index_template = "admin/base_site.html"
    index_template = "panel.html"
    login_template = 'login.html'

blog_site = BlogAdminArea(name="blogpanel")
