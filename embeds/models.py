from django.db import models
from jsonfield import JSONField
import caching.base

OEMBED_TYPES = (
    ('video',)*2,
    ('photo',)*2,
    ('link',)*2,
    ('rich',)*2,
)

class SavedEmbed(caching.base.CachingMixin, models.Model):
    url = models.URLField()
    maxwidth = models.SmallIntegerField(null=True, blank=True)
    maxheight = models.SmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=OEMBED_TYPES)
    oembed_data = JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    objects = caching.base.CachingManager()

    class Meta:
        unique_together = ('url', 'maxwidth', 'maxheight')

    def __unicode__(self):
        return self.url

