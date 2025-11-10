from django.urls import path, include
from django.shortcuts import get_object_or_404, render
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView
from .models import Task
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

app_name = 'notes'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='notes:schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='notes:schema'), name='swagger-redoc'),
    
    path('ui/register/', lambda request: render(request, 'notes/register.html'), name='register_page'),
    path('ui/login/', lambda request: render(request, 'notes/login.html'), name='login_page'),
    path('ui/tasks/', lambda request: render(request, 'notes/task_list.html'), name='task_list_page'),
    #path('ui/tasks/<slug>/delete/', lambda request, slug: render(request, 'notes/task_delete.html', {'task': get_object_or_404(Task, slug=slug)}), name='task_delete_page'),
]
