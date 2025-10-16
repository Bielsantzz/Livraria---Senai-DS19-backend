from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

router = DefaultRouter()
router.register(r"imagens", ImageViewSet, basename="imagens")
router.register(r"livros", LivrosView, basename="livros")

urlpatterns = [
    # Autores
    path('autores/', AutoresView.as_view()),                 # GET e POST
    path('autor/<int:pk>/', AutoresDetailView.as_view()),    # UPDATE e DELETE

    # Editoras
    path('editoras/', EditorasView.as_view()),
    path('editora/<int:pk>/', EditorasDetailView.as_view()),

    # Registro e JWT
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
