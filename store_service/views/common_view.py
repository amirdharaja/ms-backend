from store_service.models import User

from store_service.model.ItemCategoryModel import ItemCategory
from store_service.model.ItemSubCategoryModel import ItemSubCategory
from store_service.model.ItemModel import Item
from store_service.model.CartModel import Cart
from store_service.model.FavouriteModel import Favourite
from store_service.model.MainSlideImageModel import MainSlideImage
from store_service.model.SubSlideImageModel import SubSlideImage
from store_service.model.ContactRequestModel import ContactRequest
from store_service.model.PageImageModel import PageImage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from store_service.helpers import get_cart_count, get_favourite_count

from datetime import datetime, timedelta
import json
from random import randint
from pluck import pluck
from math import floor

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view, APIView
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_202_ACCEPTED as accepted,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_401_UNAUTHORIZED as un_authorized,
    HTTP_403_FORBIDDEN as forbidden,
    HTTP_404_NOT_FOUND as not_found,
    HTTP_405_METHOD_NOT_ALLOWED as method_not_allowd,
)

from store_service.serializers import (
    ItemCategorySerializer,
    ItemSubCategorySerializer,
    ItemSerializer,
    MainSlideImageSerializer,
    SubSlideImageSerializer,
    CartSerializer,
    PhoneOTPSerializer,
    ContactRequestSerializer,
    PageImageSerializer
)


@permission_classes((AllowAny,))
class Home(APIView):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        categories = ItemCategory.objects.all()
        main_slides = MainSlideImage.objects.filter(is_available=True)
        sub_slides = SubSlideImage.objects.filter(is_available=True)

        cart_count = 0
        favourite_count = 0
        if request.user.is_authenticated:
            cart_count = get_cart_count(request.user)
            favourite_count = get_favourite_count(request.user)

        category_details = []
        for d in categories:
            details = {
                'id': d.id,
                'name': d.name,
                'slug': d.slug,
                'image': str(d.image) if d.image else None,
                'created_at': d.created_at,
                'updated_at': d.updated_at,
            }
            category_details.append(details)

        main_slide_images = []
        sub_slide_images = []
        for d in main_slides:
            data = {
                'image': str(d.image)
            }
            main_slide_images.append(data)
        for d in sub_slides:
            data = {
                'image': str(d.image)
            }
            sub_slide_images.append(data)

        data = {
            'category_details': category_details,
            'cart_count': cart_count,
            'favourite_count': favourite_count,
            'main_slide_images': main_slide_images,
            'sub_slide_images': sub_slide_images,
        }
        return Response({'status': True, 'data': data}, status=ok)

    def put(self, request, *args, **kwargs):
        user_id = request.data.get('id')
        if not user_id:
            return Response({'status': False, 'detail': 'User "id" required', }, status=bad_request)

        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({'status': False, 'detail': 'User id not found', }, status=not_found)

        user.phone = request.data.get(
            'phone') if request.data.get('phone') else user.phone
        user.first_name = request.data.get('first_name') if request.data.get(
            'first_name') else user.first_name
        user.last_name = request.data.get('last_name') if request.data.get(
            'last_name') else user.last_name
        user.email = request.data.get(
            'email') if request.data.get('email') else user.email
        user.active = False
        new = {'phone': request.data.get('phone')}
        serializer = PhoneOTPSerializer(data=new)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user.save()
        return Response({'status': True, 'detail': 'Successfully upudated, Please re login', }, status=ok)

    def delete(self, request, *args, **kwargs):
        user_id = request.data.get('id')
        if not user_id:
            return Response({'status': False, 'detail': 'User "id" required', }, status=bad_request)

        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({'status': False, 'detail': 'User id not found', }, status=not_found)

        user.delete()
        return Response({'status': True, 'detail': 'Successfully deleted', }, status=ok)


@api_view(('GET',))
def get_items(request, category_name, category_id, sub_category_id=None):
    paginate = '2'
    all_categories = ItemCategory.objects.all()
    all_sub_categories = ItemSubCategory.objects.filter(
        category_id=category_id)
    all_sub_category_ids = []
    if sub_category_id:
        all_sub_category_ids.append(sub_category_id)
    else:
        all_sub_category_ids = pluck(all_sub_categories, 'id')
    if 'search_keyword' in request.GET:
        search_keyword = request.GET['search_keyword']
        sort_by = request.GET['sort'].strip()
        if sort_by == 'A':
            all_items = Item.objects.filter(
                sub_category_id__in=all_sub_category_ids, name__contains=search_keyword, is_available=True).order_by('name')
        elif sort_by == 'D':
            all_items = Item.objects.filter(sub_category_id__in=all_sub_category_ids,
                                            name__contains=search_keyword, is_available=True).order_by('-name')
        elif sort_by == 'L':
            all_items = Item.objects.filter(
                sub_category_id__in=all_sub_category_ids, name__contains=search_keyword, is_available=True).order_by('rate')
        elif sort_by == 'H':
            all_items = Item.objects.filter(sub_category_id__in=all_sub_category_ids,
                                            name__contains=search_keyword, is_available=True).order_by('-rate')
        else:
            all_items = Item.objects.filter(
                sub_category_id__in=all_sub_category_ids, name__contains=search_keyword, is_available=True).order_by('name')
    else:
        search_keyword = ''
        sort_by = ''

        all_items = Item.objects.filter(
            sub_category_id__in=all_sub_category_ids, is_available=True).order_by('name')

    paginator = Paginator(all_items, paginate)
    page = request.GET.get('page')
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        all_items = paginator.page(1)
    except EmptyPage:
        all_items = paginator.page(paginator.num_pages)

    all_sub_categories = ItemSubCategory.objects.all()
    category_names = []
    for category in all_categories:
        sub_categories = []
        for sub_category in all_sub_categories:
            if category.id == sub_category.category_id:
                sub_categories.append({
                    'id': sub_category.id,
                    'name': sub_category.name,
                    'slug': sub_category.slug,
                })

        category_names.append({
            'id': category.id,
            'name': category.name,
            'slug': category.slug,
            'sub_categories': sub_categories,
        })
    all_categories = ItemCategorySerializer(all_categories, many=True)
    all_sub_categories = ItemSubCategorySerializer(
        all_sub_categories, many=True)
    items = ItemSerializer(all_items, many=True)

    cart_count = 0
    favourite_count = 0
    if request.user.is_authenticated:
        cart_count = get_cart_count(request.user)
        favourite_count = get_favourite_count(request.user)

    # if all_items.paginator:
    #     print(dir(all_items))
    #     if all_items.has_previous:
    #         print(all_items.next_page_number,'***********')
    #     else:
    #         print('no')
    data = {
        'items': items.data,
        'categories': all_categories.data,
        'sub_categories': all_sub_categories.data,
        'category_names': category_names,
        'search_keyword': search_keyword,
        'sort_by': sort_by,
        'cart_count': cart_count,
        'favourite_count': favourite_count,
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(('GET',))
def get_item(request, sub_category_id, item_slug, item_id):
    item = Item.objects.filter(id=item_id).first()
    if not item:
        return Response({'status': False}, status=not_found)

    item = ItemSerializer(item, many=False)
    cart_count = 0
    favourite_count = 0
    is_in_cart = None
    if request.user.is_authenticated:
        cart_count = get_cart_count(request.user)
        favourite_count = get_favourite_count(request.user)
        check = Cart.objects.filter(user=request.user, item_id=item_id).first()
        if check:
            is_in_cart = True
        else:
            is_in_cart = False
    data = {
        'cart_count': cart_count,
        'favourite_count': favourite_count,
        'item': item.data,
        'is_in_cart': is_in_cart,
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(('GET',))
def get_best_selling_products(request):
    all_items = Item.objects.filter().order_by('-total_sales_amount')[:15]
    items = []
    for d in all_items:
        data = {
            'id': d.id,
            'name': d.name,
            'image': str(d.image),
            'slug': d.slug,
            'sub_category_id': d.sub_category_id,
        }
        items.append(data)
    return Response({'status': True, 'data': items}, status=ok)


@api_view(('POST',))
def send_contact_request(request):
    serializer = ContactRequestSerializer(data=request.data['data'])
    if serializer.is_valid():
        serializer.save()
        return Response({'status': True, 'detail': 'Thankyou for reaching us, We will get back with in 24 hours', }, status=ok)

    return Response({'status': True, 'detail': 'Please retry', }, status=bad_request)

@api_view(('get',))
def get_page_images(request):
    all_images = PageImage.objects.all()
    images = []
    for d in all_images:
        images.append({'images': '/images/' + str(d.image)})
    return Response({'status': True, 'data': images, }, status=ok)
