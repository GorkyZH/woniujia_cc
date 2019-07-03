# coding:utf-8
from case.guest_case import GuestCase

class GuestApi:
    def __init__(self):
        guest = GuestCase()
        guest.go_to_guest()

if __name__ == '__main__':
    guest_api = GuestApi()
