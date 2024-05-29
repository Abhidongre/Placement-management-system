from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Student_Views, Company_Views,Student_Views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('admin/', admin.site.urls),
    path('Contact Us', views.contact,name='contact'),
    path('logout', views.logout_user, name ='logout'),

    #login page
    path('Get Started',views.LOGIN,name='login'),
    path('login_i',views.login_i,name='login_i'),
    path('Help',views.Help,name='Help'),
    path('doLogin/',views.doLogin,name='doLogin'),

    #Company
    path('Company/Homepage',Company_Views.Homepage,name='Homepage'),
    path('Company/student_info',Company_Views.student_info,name='student_info'),
    path('Company/Contact Us1', Company_Views.contact1,name='contact1'),
    path('Company/Help1',Company_Views.Help1,name='Help1'),

    #login for Students
    path('doLogin1/',Student_Views.doLogin1,name='doLogin1'),
    path('student login',Student_Views.student_login,name='student login'),
    path('Student/student_home',Student_Views.student_home,name='student_home'),
    path('Student/companies1',Student_Views.companies1,name='companies1'),
    path('Student/courses',Student_Views.courses,name='courses'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

admin.site.site_header = "Placement Management Admin"
admin.site.site_title = "Placement Management Portal"
admin.site.index_title = "Welcome to Placement System Portal"