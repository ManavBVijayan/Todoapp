from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.listview.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.detailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(), name='cbvdelete')

]
