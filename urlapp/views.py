# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .models import ShortUrl
from .constants import SHORTEN_URL_MIN_LENGTH
import short_url


def index(request):
    return HttpResponse("Hello Shorten Url :)")


# redirect to original url.
def redirect(request, short_url_key):
    if len(short_url_key) >= SHORTEN_URL_MIN_LENGTH:
        seed_key = short_url.decode_url(short_url_key)

        if seed_key:
            try:
                a_short_url = ShortUrl.objects.get(seed=seed_key)
            except ObjectDoesNotExist:
                return HttpResponse("Bad Request :(")

            return HttpResponsePermanentRedirect(a_short_url.url)

    return HttpResponse("Bad Request :(")
