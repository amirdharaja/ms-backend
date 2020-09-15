from store_service.models import User

from store_service.model.ItemCategoryModel import ItemCategory
from store_service.model.ItemModel import Item
from store_service.model.CartModel import Cart
from store_service.model.FavouriteModel import Favourite
from store_service.model.AddressModel import Address
from store_service.model.PincodeModel import Pincode
from store_service.model.CityModel import City
from store_service.model.UserDetailModel import UserDetail
from store_service.model.OrderModel import Order
from store_service.model.WalletModel import Wallet

from store_service.helpers import get_cart_count, get_favourite_count, get_cart_total_amount


from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view, APIView
from rest_framework.status import (
    HTTP_200_OK as ok,
    HTTP_201_CREATED as created,
    HTTP_202_ACCEPTED as accepted,
    HTTP_304_NOT_MODIFIED as no_change,
    HTTP_400_BAD_REQUEST as bad_request,
    HTTP_401_UNAUTHORIZED as un_authorized,
    HTTP_403_FORBIDDEN as forbidden,
    HTTP_404_NOT_FOUND as not_found,
)
from store_service.serializers import (
    ItemCategorySerializer,
    AddressSerializer,
    PincodeSerializer,
    CitySerializer,
    UserSerializer
)


@permission_classes((IsAuthenticated,))
class UserAccount(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response({'status': False}, status=not_found)

        user = UserSerializer(user,  many=False)
        return Response({'status': True, 'data': user.data}, status=ok)

    def put(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        if not user:
            return Response({'status': False}, status=not_found)

        user.first_name = request.data.get('first_name') if request.data.get(
            'first_name') else user.first_name
        user.last_name = request.data.get('last_name') if request.data.get(
            'last_name') else user.last_name
        user.email = request.data.get(
            'email') if request.data.get('email') else user.email

        user.save()
        return Response({'status': True}, status=ok)

    def delete(self, request, *args, **kwargs):
        User.objects.filter(id=request.user.id).delete()
        UserDetail.objects.filter(user=request.user).delete()
        Token.objects.filter(user=request.user).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class CartFunction(APIView):

    def get(self, request, *args, **kwargs):
        all_carts = Cart.objects.filter(user=request.user, is_ordered=False)
        carts = []
        for d in all_carts:
            data = {
                'id': d.id,
                'item_id': d.item_id,
                'name': d.item.name,
                'rate': d.rate,
                'weight': d.weight,
                'count': d.count,
                'image': str(d.item.image),
                'discount':d.item.discount,
                'discount_type':d.item.discount_type,
            }
            carts.append(data)

        data = {
            'carts': carts,
            'cart_count': get_cart_count(request.user),
            'favourite_count': get_favourite_count(request.user),
            'cart_total_amount': get_cart_total_amount(request.user),
        }

        return Response({'status': True, 'data': data}, status=ok)

    def post(self, request, *args, **kwargs):
        data = request.data['cart']
        print(data)
        item_rate = int(data['rate'])
        weight = None
        rate = item_rate
        if data['divide_by'] == '1':
            weight = data['weight']

        elif data['divide_by'] == '2':
            if data['value'] == '2':
                weight = data['weight']/2
                rate = item_rate/2
            else:
                weight = data['weight']

        elif data['divide_by'] == '4':
            if data['value'] == '4':
                weight = data['weight']/4
                rate = item_rate/4
            elif data['value'] == '3':
                weight = data['weight'] - data['weight']/4
                rate = item_rate - item_rate/4
            elif data['value'] == '2':
                weight = data['weight']/2
                rate = item_rate/2
            else:
                weight = data['weight']

        is_exist = Cart.objects.filter(item=data['id'], weight=weight, user=request.user, is_ordered=False).first()
        if is_exist:
            is_exist.count += data['count']
            is_exist.save()
            cart_count = get_cart_count(request.user)
            data = {'cart_count': cart_count, }
            return Response({'status': True, 'data': data, 'message': 'Success! Cart updated'}, status=ok)

        Cart(
            weight=weight,
            count=data['count'],
            rate=rate,
            item_id=data['id'],
            user_id=request.user.id,
        ).save()

        cart_count = get_cart_count(request.user)
        data = {'cart_count': cart_count, }
        return Response({'status': True, 'data': data, 'message': 'Success! Added into Cart'}, status=ok)

    def put(self, request, *args, **kwargs):
        data = request.data['cart']
        is_exist = Cart.objects.filter(id=data['id'], is_ordered=False).first()
        if is_exist and is_exist.count > 0:
            if data['add']:
                is_exist.count += 1
            else:
                is_exist.count -= 1

            if is_exist.count <= 0:
                is_exist.delete()
            else:
                is_exist.save()

            return Response({'status': True, 'message': 'Success! Cart updated'}, status=ok)

        return Response({'status': True, 'message': 'Cart item not found'}, status=not_found)

    def delete(self, request, cart_id, *args, **kwargs):
        Cart.objects.filter(id=cart_id, is_ordered=False).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class FavouriteFunction(APIView):

    def get(self, request, *args, **kwargs):
        all_favourites = Favourite.objects.filter(user=request.user)
        favourites = []
        for d in all_favourites:
            data = {
                'id': d.id,
                'name': d.item.name,
                'item_id': d.item_id,
                'image': str(d.item.image)
            }
            favourites.append(data)

        data = {
            'favourites': favourites,
            'cart_count': get_cart_count(request.user),
            'favourite_count': get_favourite_count(request.user),
        }

        return Response({'status': True, 'data': data}, status=ok)

    def post(self, request, *args, **kwargs):
        data = request.data['item']
        is_exist = Favourite.objects.filter( item=data['id'], user=request.user).first()
        if is_exist:
            is_exist.delete()
            favourite_count = get_favourite_count(request.user)
            data = {'favourite_count': favourite_count, }
            return Response({'status': True, 'data': data, 'alertType': 'info', 'message': 'This item removed from your Favourite list'}, status=ok)

        Favourite(
            item_id=data['id'],
            user_id=request.user.id,
        ).save()

        favourite_count = get_favourite_count(request.user)
        data = {'favourite_count': favourite_count, }
        return Response({'status': True, 'data': data, 'message': 'Success! Added into your Favourite list'}, status=ok)

    def delete(self, request, favourite_id, *args, **kwargs):
        Favourite.objects.filter(id=favourite_id).delete()
        return Response({'status': True}, status=ok)


@permission_classes((IsAuthenticated,))
class Checkout(APIView):

    def get(self, request, *args, **kwargs):
        all_carts = Cart.objects.filter(user=request.user, is_ordered=False)
        all_address = Address.objects.filter(user=request.user)
        all_city = City.objects.all()
        all_pincode = Pincode.objects.all()
        all_address = AddressSerializer(all_address, many=True)
        all_city = CitySerializer(all_city, many=True)
        all_pincode = PincodeSerializer(all_pincode, many=True)
        carts = []
        for d in all_carts:
            data = {
                'id': d.id,
                'name': d.item.name,
                'rate': d.rate,
                'weight': d.weight,
                'count': d.count,
            }
            carts.append(data)

        wallet = Wallet.objects.filter(user=request.user).first()
        balance = 0
        if wallet:
            balance = wallet.balance

        cart_total_amount = get_cart_total_amount(request.user),
        shipping_charge = 0
        if cart_total_amount[0] < 500:
            shipping_charge = 60
        data = {
            'carts': carts,
            'address': all_address.data,
            'pincode': all_pincode.data,
            'city': all_city.data,
            'cart_count': get_cart_count(request.user),
            'favourite_count': get_favourite_count(request.user),
            'cart_total_amount': cart_total_amount[0],
            'wallet_balance': balance,
            'shipping_charge': shipping_charge,
        }

        return Response({'status': True, 'data': data}, status=ok)

    def post(self, request):
        address_id = None
        if 'existing_address_id' in request.data['data']:
            address_id = request.data['data']['existing_address_id']
        else:
            new_address = Address(
                user=request.user,
                address_type=request.data['data']['address']['address_type'],
                home_number=request.data['data']['address']['home_number'],
                street=request.data['data']['address']['street'],
                area=request.data['data']['address']['area'],
                city_id=request.data['data']['address']['city_id'],
                landmark=request.data['data']['address']['landmark'],
                pincode_id=request.data['data']['address']['pincode_id'],
            )
            new_address.save()
            address_id = new_address.id

        total_amount = get_cart_total_amount(request.user)
        
        if request.data['data']['payment_type'] == 'Wallet':
            check = Wallet.objects.filter(user=request.user).first()
            if check and check.balance < total_amount:
                return Response({'status': False, 'message': 'Wallet ballance insufficient, Try another option'}, status=bad_request)

            check.balance -= total_amount
            check.save()

        new_order = Order(
            user=request.user,
            address_id=address_id,
            payment=request.data['data']['payment_type'],
            total_cost=total_amount,
            shipping_charge = 60 if total_amount < 500 else 0,
            status='Confirmed' if request.data['data']['payment_type'] == 'COD' or request.data[ 'data']['payment_type'] == 'Wallet' else 'Waiting'
        )
        new_order.save()

        Cart.objects.filter(user=request.user, is_ordered=False).update(
            is_ordered=True,
            order_id=new_order.id
            )

        data = {
            'order_id': new_order.id,
        }
        return Response({'status': True, 'data': data}, status=ok)


@api_view(["get"])
@permission_classes((IsAuthenticated,))
def get_order(request, *args, **kwargs):
    orders = Order.objects.filter(user=request.user).order_by('-date', '-time')
    print(len(orders))
    all_items = Cart.objects.filter(user=request.user, is_ordered=True)

    total, current, delivered, canceled = 0, 0, 0, 0
    ordered_items = []
    for order in orders:
        total += 1
        if order.status == 'Delivered':
            delivered += 1
        elif order.status == 'Canceled':
            canceled += 1
        else:
            current += 1
        items = []
        for item in all_items:
            if order.id == item.order_id:
                data = {
                    'id': item.id,
                    'name': item.item.name,
                    'order_id': item.order_id,
                    'weight': item.weight,
                    'count': item.count,
                    'rate': item.rate,
                }

                items.append(data)
        if not items:
            continue
        else:
            ordered_items.append(
                {
                    'order_id': order.id,
                    'payment': order.payment,
                    'status': order.status,
                    'total_cost': order.total_cost,
                    'shipping_charge': order.shipping_charge,
                    'items': items,
                    'address':{
                        'address_type': order.address.address_type,
                        'home_number': order.address.home_number,
                        'street': order.address.street,
                        'area': order.address.area,
                        'landmark': order.address.landmark,
                        'city': order.address.city.name,
                        'pincode': order.address.pincode.pincode,
                    }
                }
            )
            print(len(ordered_items))

    orders_count = {
        'total': total,
        'current': current,
        'delivered': delivered,
        'canceled': canceled,
    }
    data = {
        'cart_count': get_cart_count(request.user),
        'favourite_count': get_favourite_count(request.user),
        'ordered_items': ordered_items,
        'orders_count': orders_count
    }
    return Response({'status': True, 'data': data}, status=ok)


@api_view(["post"])
@permission_classes((IsAuthenticated,))
def cart(request, *args, **kwargs):
    item = Item.objects.filter(id=request.data['id']).first()
    if item:
        if request.data['add']:
            Cart(
                weight=item.weight,
                count=1,
                rate=item.rate,
                item=item,
                user_id=request.user.id,
            ).save()
            return Response({'status': True,}, status=ok)
        else:
            Cart.objects.filter(item_id=request.data['id']).delete()
            return Response({'status': True,}, status=ok)
    else:
        return Response({'status': False,}, status=not_found)

