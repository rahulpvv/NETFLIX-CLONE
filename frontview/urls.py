from django.urls import path
from frontview import views


urlpatterns = [
    path('front_index/',views.front_index,name="front_index"),
    path('front_content/',views.front_content,name="front_content"),
    path('content/<c_name>/',views.content,name="content"),
    path('single_content/<dataid>/',views.single_content,name="single_content"),
    path('vidio/<vidioid>/',views.vidio,name="vidio"),





    path('login_page/',views.login_page,name="login_page"),

    path('signin/',views.signin,name="signin"),

    path('save_signup/',views.save_signup,name="save_signup"),
    
    path('user_login/',views.user_login,name="user_login"),
    path('userlogout/',views.userlogout,name="userlogout"),






    path('save_comment/',views.save_comment,name="save_comment"),
    path('profile/',views.profile,name="profile"),









    path('intovidio/',views.intovidio,name="intovidio"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),








]