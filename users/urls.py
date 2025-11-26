from django.urls import path
from .views import RegisterView, user_list_api, user_detail_api, MyTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', user_list_api, name='user_list_api'),
    path('<int:user_id>/', user_detail_api, name='user_detail_api'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
