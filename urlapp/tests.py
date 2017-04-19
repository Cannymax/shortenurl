from django.test import TestCase
from .models import ShortUrl, ShortIndex
import short_url


# Create your tests here.
class ShortUrlTestCase(TestCase):
    def setUp(self):
        ShortUrl.objects.create(url="https://www.google.co.kr/test", description="to google")

    def test_success_shorten_url(self):
        short_index = ShortIndex.objects.get(id=1)
        obj = ShortUrl.objects.get(url="https://www.google.co.kr/test")
        self.assertIsNotNone(obj.short_url)
        self.assertEqual(short_url.decode_url(obj.short_url), short_index.seed_cnt)

    def test_short_url(self):
        enc_url = short_url.encode_url(1, 8)
        self.assertEqual(short_url.decode_url(enc_url), 1)
