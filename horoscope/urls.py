from django.urls import path
from horoscope import views

urlpatterns = [
    # path('', views.index, name='horoscope-index'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
]