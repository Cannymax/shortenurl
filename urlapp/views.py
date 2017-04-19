# -*- coding: utf-8 -*-
from django.http import HttpResponse
from urlapp.models import ShortUrl
from django.http import HttpResponsePermanentRedirect
import short_url


# redirect to original url.
def redirect(request, short_url_key):
    seed_key = short_url.decode_url(short_url_key)

    if seed_key:
        a_short_url = ShortUrl.objects.get(seed=seed_key)
        return HttpResponsePermanentRedirect(a_short_url.url)

    return HttpResponse("Wrong Request.")
