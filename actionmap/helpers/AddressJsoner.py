class AddressJsoner(object):
    def __init__(self, querySet):
        self.querySet = querySet

    def format(self):
        addresses = []
        for address in self.querySet:
            addresses.append({"lat": address['lat'], "lng": address["lng"], "address": address["address"]})
        return addresses