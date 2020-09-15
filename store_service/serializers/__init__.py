from store_service.models import User

from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

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

from store_service.model.PhoneOTPModel import PhoneOTP
from store_service.model.MainSlideImageModel import MainSlideImage
from store_service.model.SubSlideImageModel import SubSlideImage
from store_service.model.PageImageModel import PageImage


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'address_type',
            'home_number',
            'street',
            'area',
            'landmark',
        )


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogCommentSerializer(ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'


class BlogLikeSerializer(ModelSerializer):
    class Meta:
        model = BlogLike
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)


class ContactRequestSerializer(ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'phone', 'details')


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, APIView
@permission_classes((AllowAny,))
class ItemCategorySerializer(ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class ItemCommentSerializer(ModelSerializer):
    class Meta:
        model = ItemComment
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ItemSubCategorySerializer(ModelSerializer):
    class Meta:
        model = ItemSubCategory
        fields = '__all__'


class LoginHistorySerializer(ModelSerializer):
    class Meta:
        model = LoginHistory
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PincodeSerializer(ModelSerializer):
    class Meta:
        model = Pincode
        fields = ('id','pincode',)


class RefundSerializer(ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'


class SpecialItemSerializer(ModelSerializer):
    class Meta:
        model = SpecialItem
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'phone',
            'password',
            'first_name',
            'last_name',
            'email',
        )
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'



class PhoneOTPSerializer(ModelSerializer):
    class Meta:
        model = PhoneOTP
        fields = '__all__'


class MainSlideImageSerializer(ModelSerializer):
    class Meta:
        model = MainSlideImage
        fields = '__all__'


class SubSlideImageSerializer(ModelSerializer):
    class Meta:
        model = SubSlideImage
        fields = '__all__'


class PageImageSerializer(ModelSerializer):
    class Meta:
        model = PageImage
        fields = ('image')
