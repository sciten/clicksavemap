# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Address
from .helpers.GetAddresses import GetAddresses
from .helpers.AddressAdder import AddressAdder

class TestAddressStuff(TestCase):
    def setUp(self):
        Address.objects.create(lat="24", lng="24", address="street here")

    def testGetAdresses(self):
        getAdresses = GetAddresses()
        addresses = getAdresses.getAll()

        self.assertEqual(1, len(addresses))

    def testPutAddresses(self):
        putAddress = AddressAdder(lat="98", lng="42", address="Whatever")
        putAddress.save()

        getAdresses = GetAddresses()
        addresses = getAdresses.getAll()

        print(addresses)