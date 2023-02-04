from django.urls import path
from horoscope import views

urlpatterns = [
    path('<sign_zodiac>/', views.get_info_about_sign_zodiac),
    # path('horoscope/leo/', views.leo),
    # path('horoscope/scorpione/', views.scorpione),
]