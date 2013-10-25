from django.db import models
from jsonfield import JSONField

OEMBED_TYPES = (
    ('video',)*2,
    ('photo',)*2,
    ('link',)*2,
    ('rich',)*2,
)

class SavedEmbed(models.Model):
    url = models.URLField()
    maxwidth = models.SmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=OEMBED_TYPES)
    oembed_data = JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('url', 'maxwidth')

    def __unicode__(self):
        return self.url

