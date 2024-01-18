from django.shortcuts import render
from rest_framework import status,serializers,generics , viewsets ,permissions
from .serializers import MenuSerializer , BookingSerializer
from .models import Menu , Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    ordering_fields = ['Price']
    search_fields = ['Title']
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated] 
