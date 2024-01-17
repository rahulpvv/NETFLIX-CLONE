from django.urls import path
from newapp import views


urlpatterns = [
path('main_index/',views.main_index,name="main_index"),


path('add_cat/',views.add_cat,name="add_cat"),
path('save_cat/',views.save_cat,name="save_cat"),
path('display_category/',views.display_category,name="display_category"),
path('edit_category/<int:dataid>/',views.edit_category,name="edit_category"),
path('update_category/<int:dataid>/',views.update_category,name="update_category"),
path('delete_category<int:dataid>/',views.delete_category,name="delete_category"),


path('items/',views.items,name="items"),
path('save_items/',views.save_items,name="save_items"),
path('display_items/',views.display_items,name="display_items"),
path('edit_items/<int:dataid>/',views.edit_items,name="edit_items"),
path('update_items/<int:dataid>/',views.update_items,name="update_items"),
path('delete_items/<int:dataid>/',views.delete_items,name="delete_items"),




path('admin_login/',views.admin_login,name="admin_login"),
path('admin_save/',views.admin_save,name="admin_save"),
path('admin_logout/',views.admin_logout,name="admin_logout"),
path('delete_comment<int:dataid>/',views.delete_comment,name="delete_comment"),




path('userdisplay/',views.userdisplay,name="userdisplay"),
path('display_comment/',views.display_comment,name="display_comment"),





path('topview/',views.topview,name="topview"),
path('save_view/',views.save_view,name="save_view"),




path('display_view/',views.display_view,name="display_view"),
path('delete_view/<int:dataid>/',views.delete_view,name="delete_view"),



path('enquiry/',views.enquiry,name="enquiry"),
path('delete_enq/<int:dataid>/',views.delete_enq,name="delete_enq"),






]