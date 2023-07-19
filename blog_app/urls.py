from django.urls import path,include
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static


app_name='blog_app'

urlpatterns = [
    path("",views.post_list.as_view(),name="post_list"),
    path("newpost/<pk>",views.post_create, name="post_create"),
    path("detail/<pk>",views.post_detail.as_view(), name="post_detail"),
    path("comment/<pk>",views.comment_create, name="comment"),
    path("delete/<pk>",views.post_delete.as_view(), name="post_delete"),
    path("comment/detail/<pk>",views.comment_detail, name="comment_detail"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)