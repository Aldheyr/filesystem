from django.urls import path
from .views import (
    IndexView,
    DiskLocal,
    DiskFolderLocal,
    DiskFolderLocal2,
    RDSView,
    WorkspaceView
)

app_name = 'home'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('disco/<str:disk>/', DiskLocal.as_view(), name='disk_local'),
    path('disco/<str:disk>/carpeta/<str:folder>', DiskFolderLocal.as_view(), name='folder_local'),
    path('disco/<str:disk>/carpeta/<str:folder>/carpeta/<str:folder2>', DiskFolderLocal2.as_view(), name='folder_local2'),
    path('rds', RDSView.as_view(), name='rds'),
    path('workspace', WorkspaceView.as_view(), name='workspace'),
]
