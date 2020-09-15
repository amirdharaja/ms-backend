from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

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
from store_service.model.WalletModel import Wallet

from store_service.model.PhoneOTPModel import PhoneOTP
from store_service.model.MainSlideImageModel import MainSlideImage
from store_service.model.SubSlideImageModel import SubSlideImage
from store_service.model.PageImageModel import PageImage

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()



admin.site.site_header = "Mother's Store Admin"
admin.site.index_title = ""
admin.site.site_title = "Mother's Store-Admin"



class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['phone', 'first_name', 'last_name', 'last_login']
    list_filter = ['staff', 'active', 'admin']
    fieldsets = (
        (None, {'fields': ('phone', 'role')}),
        ('personal_info', {'fields': ('first_name', 'last_name')}),
        ('permissions', {'fields': ('admin', 'staff', 'active')})
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('phone', 'password1', 'password2')
            },
        )
    )
    search_fields = ('phone',)
    ordering = ('id',)
    filter_horizontal = ()


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'details',
        'created_at',
    )
    search_fields = [
        'name',
        'email',
        'phone',
    ]

# class UserDetailAdmin(admin.ModelAdmin):
#     list_display = (
#         'user',
#         'role',
#         'email_verified',
#     )
#     search_fields = [
#         'role',
#     ]

class PincodeAdmin(admin.ModelAdmin):
    list_display = (
        'pincode',
        'created_at',
        'updated_at',
    )
    search_fields = [
        'pincode',
    ]

class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'updated_at',
    )
    search_fields = [
        'name',
    ]

class WalletAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'balance',
        'created_at',
        'updated_at'
    )
    search_fields = [
        'user_id',
        'balance',
        'created_at',
        'updated_at'
    ]


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'weight',
        'count',
        'rate',
        'created_at',
        'updated_at'
    )
    search_fields = [
        'item',
        'count'
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'address',
        'status',
        'total_cost',
        'date',
        'time',
        'created_at',
        'updated_at'
    )
    search_fields = [
        'status',
        'total_cost'
    ]


class SpecialItemAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'image',
        'date',
        'title',
        'description',
        'created_at',
        'updated_at',
    )
    search_fields = [
        'date',
        'title',
        'description'
    ]

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'created_at',
        'updated_at',
    )
    search_fields = [
        'name',
    ]

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'image',
        'is_available',
        'rate',
        'description',
        'created_at',
        'updated_at'
    )
    search_fields = [
        'name',
        'is_available',
        'rate',
        'description',
    ]

class ItemCommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'item',
        'comment',
        'created_at',
    )
    search_fields = [
        'comment',
        'created_at'
    ]


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'blog',
        'comment',
        'created_at',
    )
    search_fields = [
        'comment',
    ]

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'content',
        'created_at',
        'user',
    )
    search_fields = [
        'title',
        'content',
    ]

class BlogLikeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'blog',
        'is_like',
        'created_at',
    )


admin.site.register(Address)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogLike, BlogLikeAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
admin.site.register(Coupon)
admin.site.register(Favourite)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemComment, ItemCommentAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemSubCategory,)
admin.site.register(LoginHistory)
admin.site.register(OrderHistory)
admin.site.register(Order, OrderAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Refund)
admin.site.register(SpecialItem, SpecialItemAdmin)
admin.site.register(Wallet, WalletAdmin)

admin.site.register(PhoneOTP)
admin.site.register(MainSlideImage)
admin.site.register(SubSlideImage)
admin.site.register(PageImage)
