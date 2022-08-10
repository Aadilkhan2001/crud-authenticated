from django.urls import path
from .views import CartUpdateDelete, UserList ,UserRetrive,CartAddRetrive
urlpatterns = [
    path('user/',UserList.as_view()),
    path('user/<int:pk>',UserRetrive.as_view()),
    path('addretrive/',CartAddRetrive.as_view()),
    path('updatedelete/<int:pk>',CartUpdateDelete.as_view())
]