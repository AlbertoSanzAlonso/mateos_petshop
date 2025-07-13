from rest_framework import viewsets, permissions
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

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
