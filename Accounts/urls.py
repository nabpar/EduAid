from django.urls import path

from Accounts.views import( 
    UserRegiatrationView,UserLoginView,UserProfileView
    ,UserPasswordChangeView,PasswordResetView,UserPasswordResetView)



urlpatterns = [
    path('register/',UserRegiatrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name="UserLogin"),
    path('profile/',UserProfileView.as_view(),name="user_view"),
    path('changepassword/',UserPasswordChangeView.as_view(),name="user_password_change"),
    path('send_reset_password_email/',PasswordResetView.as_view(),name="user_password_reset"),
    path('user_password_reset/<uid>/<token>/',UserPasswordResetView.as_view(),name="user_password_reset"),
]