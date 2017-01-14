# -*- coding: utf-8 -*-
import sys
from django.db import models
from django.utils import timezone

reload(sys)
sys.setdefaultencoding('utf-8')


class ShortUrl(models.Model):
    url = models.CharField(u'URL', max_length=500, help_text=u'URL')
    short_url = models.CharField(u'SHORT URL', null=True, blank=True, max_length=50, help_text=u'short url(생성시 미입력)')
    description = models.CharField(u'설명', max_length=50, null=True, blank=True)

    create_date = models.DateTimeField(u'등록일자', default=timezone.now)
    update_date = models.DateTimeField(u'업데이트일자', null=True, blank=True)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u"%s" % (self.short_url)

    class Meta:
        verbose_name_plural = u"Short URL"
        verbose_name = u"Short URL"
        db_table = 'tb_short_url'
