from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()
router.register('list', views.TODOViewSet, basename="todo_list")

urlpatterns = [
    path('', include(router.urls)),
    path(
        'item/<int:pk>/',
        views.TODOItemDetail.as_view(),
        name='todoitem-detail'
    )
]