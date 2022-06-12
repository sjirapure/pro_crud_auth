from django.urls import path
from .import views
urlpatterns=[
    path('av/',views.AddLaptop.as_view(),name='add_url'),
    path('sv/',views.ShowLaptop.as_view(),name='show_url'),
    path('uv/<int:id>/',views.UpdateLaptop.as_view(),name='update_url'),
    path('dv/<int:id>/',views.DeleteLaptop.as_view(),name='delete_url')
]