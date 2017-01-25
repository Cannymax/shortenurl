# -*- coding: utf-8 -*-
from django.http import HttpResponse
from urlapp.models import ShortUrl
from django.http import HttpResponsePermanentRedirect
import short_url


# redirect to original url.
def redirect(request, short_url_key):
    a_short_id = short_url.decode_url(short_url_key)

    if a_short_id:
        a_short_url = ShortUrl.objects.get(id=a_short_id)
        return HttpResponsePermanentRedirect(a_short_url.url)

    return HttpResponse("Bad Request :(")
