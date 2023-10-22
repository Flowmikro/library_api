from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='REST API service'
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/', include('book_api.urls')),
]
