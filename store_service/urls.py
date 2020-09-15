from django.urls import include, path, re_path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from store_service.viewsets import (
    AddressViewSet,
    BlogViewSet,
    BlogCommentViewSet,
    BlogLikeViewSet,
    CartViewSet,
    CityViewSet,
    ContactRequestViewSet,
    CouponViewSet,
    FavouriteViewSet,
    ItemCategoryViewSet,
    ItemCommentViewSet,
    ItemViewSet,
    ItemSubCategoryViewSet,
    LoginHistoryViewSet,
    OrderHistoryViewSet,
    OrderViewSet,
    PincodeViewSet,
    RefundViewSet,
    SpecialItemViewSet,
    UserViewSet,
    UserDetailViewSet,
    WalletViewSet,
)

router = DefaultRouter()

router.register('address', AddressViewSet)
router.register('blogs', BlogViewSet)
router.register('blog/comment', BlogCommentViewSet)
router.register('block/like', BlogLikeViewSet)
router.register('city', CityViewSet)
router.register('contact-requests', ContactRequestViewSet)
router.register('coupon', CouponViewSet)
router.register('category', ItemCategoryViewSet)
router.register('commet', ItemCommentViewSet)
router.register('item', ItemViewSet)
router.register('sub-category', ItemSubCategoryViewSet)
router.register('login-history', LoginHistoryViewSet)
router.register('order-history', OrderHistoryViewSet)
# router.register('orders', OrderViewSet)
router.register('pincode', PincodeViewSet)
router.register('refund', RefundViewSet)
router.register('special-items', SpecialItemViewSet)
router.register('users', UserViewSet)
router.register('user-details', UserDetailViewSet)
router.register('wallets', WalletViewSet)

app_name = 'store_service'

from store_service.views.auth_view import (
    ValidatePhoneSendOTP,
    ValidateOTP,
    Register,
    login,
)
from store_service.views.common_view import (
    Home,
    get_items,
    get_item,
    send_contact_request,
    get_best_selling_products,
    get_page_images,
)
from store_service.views.user_view import (
    CartFunction,
    FavouriteFunction,
    Checkout,
    UserAccount,
    get_order,
    cart
)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', login, name='login'),
    re_path(r'validate/phone/', ValidatePhoneSendOTP.as_view()),
    re_path(r'validate/otp/', ValidateOTP.as_view()),
    re_path(r'register/', Register.as_view()),
    path(r'categorys/', Home.as_view()),

    path('my/account/', UserAccount.as_view(), name='my_account'),

    path('category/<str:category_name>/<int:category_id>/all-items/', get_items, name='get_items'),
    path('category/<str:category_name>/<int:category_id>/all-items/<int:sub_category_id>/<int:item_id>/', get_item, name='get_item'),
    path('category/<str:category_name>/<int:category_id>/all-items/<int:sub_category_id>/', get_items, name='get_sub_items'),

    path('cart/', CartFunction.as_view(), name='get_cart'),
    path('add/cart/', CartFunction.as_view(), name='add_cart'),
    path('update/cart/', CartFunction.as_view(), name='update_cart'),
    path('remove/cart/<int:cart_id>/', CartFunction.as_view(), name='delete_cart'),

    path('add/favourite/', FavouriteFunction.as_view(), name='add_favourite'),
    path('favourite/', FavouriteFunction.as_view(), name='get_favourite'),
    path('remove/favourite/<int:favourite_id>/', FavouriteFunction.as_view(), name='delete_favourite'),

    path('checkout/', Checkout.as_view(), name='checkout'),
    path('order/checkout/', Checkout.as_view(), name='order-checkout'),
    path('orders/', get_order, name='get_order'),

    path('contact/', send_contact_request, name='send_contact_request'),
    path('best-selling-products/', get_best_selling_products, name='get_best_selling_products'),

    path('<int:sub_category_id>/<str:item_slug>/<int:item_id>/', get_item, name='get_item'),
    path('handle/cart/', cart, name='cart'),
    path('page/images/', get_page_images, name='get_page_images'),



]