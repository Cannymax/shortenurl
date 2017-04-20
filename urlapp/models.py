# -*- coding: utf-8 -*-
import sys
from django.db import models
from django.utils import timezone
import short_url

reload(sys)
sys.setdefaultencoding('utf-8')


class ShortIndex(models.Model):
    seed_cnt = models.BigIntegerField(u'seed', default=100, help_text=u'seed')

    def increase(self):
        self.seed_cnt = self.seed_cnt + 1
        self.save()

    class Meta:
        verbose_name_plural = u"Short Index"
        verbose_name = u"Short Index"
        db_table = 'tb_short_index'


class ShortUrl(models.Model):
    url = models.CharField(u'URL', max_length=500, help_text=u'URL')
    seed = models.BigIntegerField(u'Seed', default=100, help_text=u'Seed')
    short_url = models.CharField(u'SHORT URL', null=True, blank=True, max_length=50, help_text=u'short url(생성시 미입력)')
    description = models.CharField(u'설명', max_length=50, null=True, blank=True)

    create_date = models.DateTimeField(u'등록일자', default=timezone.now)
    update_date = models.DateTimeField(u'업데이트일자', null=True, blank=True)

    def save(self, *args, **kwargs):
        d, created = ShortIndex.objects.get_or_create(id=1)
        d.increase()

        self.seed = d.seed_cnt
        self.short_url = short_url.encode_url(d.seed_cnt)

        super(ShortUrl, self).save(*args, **kwargs)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u"%s" % (self.short_url)

    class Meta:
        verbose_name_plural = u"Short URL"
        verbose_name = u"Short URL"
        db_table = 'tb_short_url'
