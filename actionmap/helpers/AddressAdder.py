from ..models import Address

class AddressAdder(object):
    def __init__(self, lat, lng, address):
        # make sure we have the lat and lng
        if isinstance(lat, float) and isinstance(lng, float):
            self.lat = lat
            self.lng = lng
            self.address = address
        else:
            raise Exception("Please make sure you set a valid latitude and longitude!")

    def save(self):
        Address.objects.create(lat=self.lat, lng=self.lng, address=self.address)
        return True
