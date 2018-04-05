from ..models import Address

class GetAddresses():
    def __init__(self):
        self.ok = True

    def getAll(self, ordered_by="-added_on"):
        addresses = Address.objects.values('id', 'lat', 'lng', 'address').order_by(ordered_by).all()

        if(len(addresses)):
            return addresses
        else:
            raise Exception("No addresses found in database")