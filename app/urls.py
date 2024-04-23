from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('login/', views.login_user, name='Login'),
    path('logout/', views.logout_user, name='Logout'),
    path('about/', views.about, name="About"),
    path('executive/', views.executive, name='Executive'),
    path('principle/', views.principle, name="Principle"),
    path('admission/', views.admission, name="Admission"),
    path('fee/', views.fee, name="Fee"),
    path('contact/', views.contact, name="Contact"),
    path('upload/', views.upload_image, name='upload_image'),
    path('gallery/', views.image_display, name='Gallery'),
    path('examination/', views.examination, name='examination'),
    path('academic/', views.academic, name='Academic'),
    path('facility/',views.facility, name='Facility'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)