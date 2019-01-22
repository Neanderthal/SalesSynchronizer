from datetime import datetime

from django.db import transaction


# Create your views here.
from django.http import HttpResponse

from tttx.models import WaContact


@transaction.atomic
def test(request):

    return HttpResponse([item.name for item in list(WaContact.objects.all())])

