from django.urls import path
from . import views

app_name ='program'
urlpatterns=[
    path('',views.IndexProject.as_view(),name='konten'),
    path('tambah/',views.TambahProject.as_view(),name='tambah'),
    path('detail/<pk>/',views.DetailProject.as_view(),name='detail'),
    path('edit/<pk>/',views.UpdateProject.as_view(),name='ubah'),
    path('delete/<pk>/',views.DeleteProject.as_view(),name='hapus'),
    path('user/',views.index,name='index'),
    path('login/',views.login_view, name='login_view'),
    path('register/',views.register,name='register'),
    path('adminpage/',views.admin,name='adminpage'),
    path('adminpage/indexpesan/',views.IndexPesan.as_view(),name='indexpesan'),
    path('tambahpesan/',views.TambahPesan.as_view(),name='tambahpesan'),
]