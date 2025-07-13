from rest_framework import viewsets, permissions, generics
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, UserRegisterSerializer
from django.http import HttpResponse

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # cualquiera puede ver productos

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # sólo usuarios logueados

    def get_queryset(self):
        # Solo pedidos del usuario autenticado
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Al crear, asigna automáticamente el usuario actual
        serializer.save(user=self.request.user)

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]  # Cualquiera puede registrarse

def home(request):
    return HttpResponse("Bienvenido a Mateo's PetShop API")
