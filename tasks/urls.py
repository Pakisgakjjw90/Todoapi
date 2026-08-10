from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns=[path('api/tasklist/',views.list_tasks,name="list_tasks"),
path('api/task/<int:pk>/',views.task_detail,name="task_detail"),
path('api/schema/',SpectacularAPIView.as_view(),name="schema"),
path('api/docs/',SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui"),
]


