from django.urls import path
from .views import register_view, profile_view
urlpatterns = [
    path('register/', register_view, name="register"),
    path('profile/', profile_view, name="profile")
]

# auth/ password/reset/ [name='rest_password_reset']
# auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
# auth/ login/ [name='rest_login']
# auth/ logout/ [name='rest_logout']
# auth/ user/ [name='rest_user_details']
# auth/ password/change/ [name='rest_password_change']