from django.http import HttpResponse
from django.shortcuts import render
from .helpers.GetAddresses import GetAddresses
from .helpers.AddressAdder import AddressAdder
from .helpers.AddressJsoner import AddressJsoner
import json


def index(request):
    context = {"site_url": 'http://{domain}'.format(domain=request.get_host())}
    return render(request, 'actionmap/index.html', context)


# get all addresses (for frontend rendering)
def get_all_addresses_json(request):
    # prepare the result object
    result = {}

    try:
        getAddressesHelper = GetAddresses()
        addresses = getAddressesHelper.getAll()

        addressJsoner = AddressJsoner(addresses)

        result['status'] = "ok"
        result['result'] = addressJsoner.format()

    except Exception as e:
        # display error message
        result['status'] = "error"
        result['message'] = str(e)
    finally:
        return HttpResponse(json.dumps(result))


# save the address in the database
def save(request):
    # prepare the result object
    result = {}
    try:
        # try to get the post data
        try:
            json_data = json.loads(request.body)
            lat = json_data['lat']
            lng = json_data['lng']
            address = json_data['address']
        except:
            raise Exception("Invalid elements sent")

        addressAdder = AddressAdder(lat=lat, lng=lng, address=address)
        addressAdder.save()

        result['status'] = "ok"
        result['message'] = "Address added"
    except Exception as e:
        # display error message
        result['status'] = "error"
        result['message'] = str(e)
    finally:
        return HttpResponse(json.dumps(result))
