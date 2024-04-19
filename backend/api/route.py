from django.urls import path
from rest_framework.routers import DefaultRouter

from .v1.product.views import (
    ProductModelViewSet,
    CategoryModelViewSet
)

from .v1.cart.views import (
    CartModelViewSet,
)

# from api.auth.views import (
#     RegisterView,
#     UserAuthenticationView
# )

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [

        # # registration
        # path("register/", RegisterView.as_view({"post": "register"}), name="register"),

        # # login
        # path("login/", UserAuthenticationView.as_view({"post": "login"}), name="login"),
        # path("logout/", UserAuthenticationView.as_view({"post": "logout"}), name="logout"),

        # Products
        path("products/", ProductModelViewSet.as_view({"get": "products_list"}), name="products-list"),
        path("products-detail/<slug>/", ProductModelViewSet.as_view({"get": "product_detail"}), name="products-detail"),

        # Cart
        path("cart/", CartModelViewSet.as_view({"get": "cart_list"}), name="cart"),
        path("cart-add/", CartModelViewSet.as_view({"post": "cart_add"}), name="cart-add"),
        path("cart-update/", CartModelViewSet.as_view({"post": "cart_update"}), name="cart-update"),
        path("cart-delete/", CartModelViewSet.as_view({"post": "cart_delete"}), name="cart-delete"),

        # path("apartments/create/", EstablishmentModelViewSet.as_view({"post": "create"}), name="apartments-create"),
        # path("apartments/update/<int:pk>/", EstablishmentModelViewSet.as_view({"put": "update"}),
        #      name="apartments-update"),
        # path("apartments/delete/<int:pk>/", EstablishmentModelViewSet.as_view({"delete": "delete"}),
        #      name="apartments-delete"),

        # Category
        path("category-list/<slug>/", CategoryModelViewSet.as_view({"get": "category_list"}), name="category-list"),

    ]
)


'''
http://127.0.0.1:3000/api/v1/products-detail/cars/


http://127.0.0.1:3000/api/v1/products-detail/?slug=cars

'''