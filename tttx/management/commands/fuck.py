# -*- coding: utf-8 -*-
from datetime import datetime

from django.core.management import BaseCommand
from django.db import transaction

from tttx.models import WaContact


@transaction.atomic
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        contact = WaContact()
        contact.name = "Жопа"
        contact.company_contact_id = 1
        contact.is_company = True
        contact.is_user = False
        contact.create_datetime = datetime.now()
        contact.photo = 1
        contact.create_contact_id = 1
        contact.save()
