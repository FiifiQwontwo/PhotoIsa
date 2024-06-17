from django.urls import path
from User.views import LoginView, UserList, LogoutView, RegistrationView, send_verification_email

app_name= 'User'

urlpatterns =[
     path('api/login/', LoginView.as_view(), name='login_endpoint'),
     path('api/logout/', LogoutView.as_view(), name='logout_endpoint'),
     path('api/users/', UserList.as_view(), name='users_endpoint'),
     path('api/signup/', RegistrationView.as_view(), name='signup_endpoint'),
     path('api/v/', send_verification_email, name='verify_endpoint'),



]