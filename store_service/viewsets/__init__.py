from store_service.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from store_service.model.AddressModel import Address
from store_service.model.BlogModel import Blog
from store_service.model.BlogCommentModel import BlogComment
from store_service.model.BlogLikeModel import BlogLike
from store_service.model.CartModel import Cart
from store_service.model.CityModel import City
from store_service.model.ContactRequestModel import ContactRequest
from store_service.model.CouponModel import Coupon
from store_service.model.FavouriteModel import Favourite
from store_service.model.ItemCategoryModel import ItemCategory
from store_service.model.ItemCommentModel import ItemComment
from store_service.model.ItemModel import Item
from store_service.model.ItemSubCategoryModel import ItemSubCategory
from store_service.model.LoginHistoryModel import LoginHistory
from store_service.model.OrderHistoryModel import OrderHistory
from store_service.model.OrderModel import Order
from store_service.model.PincodeModel import Pincode
from store_service.model.RefundModel import Refund
from store_service.model.SpecialItemsModel import SpecialItem
from store_service.model.UserDetailModel import UserDetail
from store_service.model.WalletModel import Wallet

from store_service.serializers import (
    AddressSerializer,
    BlogSerializer,
    BlogCommentSerializer,
    BlogLikeSerializer,
    CartSerializer,
    CitySerializer,
    ContactRequestSerializer,
    CouponSerializer,
    FavouriteSerializer,
    ItemCategorySerializer,
    ItemCommentSerializer,
    ItemSerializer,
    ItemSubCategorySerializer,
    LoginHistorySerializer,
    OrderHistorySerializer,
    OrderSerializer,
    PincodeSerializer,
    RefundSerializer,
    SpecialItemSerializer,
    UserSerializer,
    UserDetailSerializer,
    WalletSerializer,
)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCommentViewSet(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer


class BlogLikeViewSet(ModelViewSet):
    queryset = BlogLike.objects.all()
    serializer_class = BlogLikeSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ContactRequestViewSet(ModelViewSet):
    queryset = ContactRequest.objects.all()
    serializer_class = ContactRequestSerializer


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class FavouriteViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class ItemCategoryViewSet(ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemCommentViewSet(ModelViewSet):
    queryset = ItemComment.objects.all()
    serializer_class = ItemCommentSerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemSubCategoryViewSet(ModelViewSet):
    queryset = ItemSubCategory.objects.all()
    serializer_class = ItemSubCategorySerializer


class LoginHistoryViewSet(ModelViewSet):
    queryset = LoginHistory.objects.all()
    serializer_class = LoginHistorySerializer


class OrderHistoryViewSet(ModelViewSet):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PincodeViewSet(ModelViewSet):
    queryset = Pincode.objects.all()
    serializer_class = PincodeSerializer


class RefundViewSet(ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer


class SpecialItemViewSet(ModelViewSet):
    queryset = SpecialItem.objects.all()
    serializer_class = SpecialItemSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewSet(ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer