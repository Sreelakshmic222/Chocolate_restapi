
from django.urls import path
from knox import views as knox_views
from .views import ListChocos,DetailChoco,Checkoutview,AddToCartView,AddToFavoriteView


urlpatterns = [
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    path('chocolates/',ListChocos.as_view(),name='list'),
    path('details/<int:pk>/',DetailChoco.as_view(),name='details'),
    # path('update/<int:pk>/',UpdateChoco.as_view(),name='update'),
    path('checkout/<int:pk>/',Checkoutview.as_view(),name='checkout'),
    path('cart/add/<int:pk>',AddToCartView.as_view(),name='addcart'),
    path('fav/add/<int:pk>/',AddToFavoriteView.as_view(),name='addfavo')
]