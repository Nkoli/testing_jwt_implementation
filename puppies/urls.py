from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from puppies import views

urlpatterns = [
    path('puppies/', views.PuppyList.as_view()),
    path('puppies/<int:pk>/', views.PuppyDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
