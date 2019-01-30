from datetime import datetime

from django.db import transaction

# Create your views here.
from django.http import HttpResponse

from tttx.models import WaContact


@transaction.atomic
def test(request):
    return HttpResponse([item.name for item in list(WaContact.objects.all())])


# def albums_list(request):
#     albums = Post.objects.all()
#     return render(request, 'blog/index.html', context={'posts': albums})
#
#
# def album_detail(request, slug):
#     album = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': album})
