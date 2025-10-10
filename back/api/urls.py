from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"imagens", ImageViewSet, basename="imagens")

urlpatterns = [
    path('authors', listar_autores),

    # GET e POST
    path('autores', AutoresView.as_view()),
    path('editoras', EditorasView.as_view()),
    path('livros', LivrosView.as_view()),

    # UPDATE e DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditorasDetailView.as_view()),
    path('livro/<int:pk>', LivrosDetailView.as_view()),

    # Token JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path ('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += router.urls
