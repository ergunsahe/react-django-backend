from django.urls import path
from .views import post_list, post_get_detail, comment_view, post_create, post_update_delete, like_view

urlpatterns = [
    path('list/', post_list, name="list"),
    path('create/', post_create, name="create"),
    path('<str:slug>/detail/', post_get_detail, name="detail"),
    path('<str:slug>/update/', post_update_delete, name="update"),
    path('<str:slug>/comment/', comment_view, name="comment"),
    path('<str:slug>/like/', like_view, name="like"),
]
