from django.core.management.base import BaseCommand
from app.models import Apikey

import uuid


class Command(BaseCommand):
    help = "django rest api Keymanager"

    def key_add(self):
        key_name = input("Input Key Name : ")

        try:
            key = Apikey(name=key_name, api_key=uuid.uuid4().hex)
            key.save()
        except:
            print("Key Name already exists")

        print("Success")
        print(f"name : {key.name}")
        print(f"api_Key : {key.api_key}")

    def key_show(self):
        keys = Apikey.objects.all()

        if not keys:
            print("keys empty")
        else:
            print("*")
            for row in keys:
                print(f"{row.name} | {row.api_key}")
            print("*")

    def key_delete(self):
        key_name = input("Input Key Name : ")

        try:
            key = Apikey.objects.get(name=key_name)
            key.delete()
        except:
            print("Invalid Key Name")

    def handle(self, *args, **options):
        print("Input Command!")
        print("add / show / delete / exit")

        while True:
            command = input("Input Command : ")

            if command == "add":
                self.key_add()
                print()
            elif command == "show":
                self.key_show()
                print()
            elif command == "delete":
                self.key_delete()
                print()
            elif command == "exit":
                break
            else:
                print("Invalid Command")
                print("add / show / delete / exit")
