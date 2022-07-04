from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# name is used in template tags {% url 'name' %}
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    # line break
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    # line break
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),
    # Line break
    path("update-user/", views.updateUser, name="update-user"),
    path("topics/", views.topicsPage, name="topics"),
    path("activity/", views.activityPage, name="activity"),
]

# Link for user_avatars
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)