
from django.urls import path
from knox import views as knox_views
from .views import ListChocos,DetailChoco,Checkoutview,AddToCartView,AddToFavoriteView


urlpatterns = [
    path('chocolates/',ListChocos.as_view(),name='list'),
    path('details/<int:pk>/',DetailChoco.as_view(),name='details'),
    path('checkout/<int:pk>/',Checkoutview.as_view(),name='checkout'),
    path('cart/add/<int:pk>',AddToCartView.as_view(),name='addcart'),
    path('fav/add/<int:pk>/',AddToFavoriteView.as_view(),name='addfavo')
]