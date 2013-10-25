from django import template
from django.conf import settings

from embedly import Embedly
from embeds.models import SavedEmbed

register = template.Library()

USER_AGENT = 'Mozilla/5.0 (compatible; django-embedly/0.2; ' \
        '+http://github.com/BayCitizen/)'

@register.assignment_tag
def get_oembed_data(url, maxwidth=None):
    '''
    '''
    try:
        saved_embed = SavedEmbed.objects.get(url=url, maxwidth=maxwidth)
    except SavedEmbed.DoesNotExist:
        client = Embedly(key=settings.EMBEDLY_KEY, user_agent=USER_AGENT)
        if maxwidth:
            oembed = client.oembed(url, maxwidth=maxwidth)
        else:
            oembed = client.oembed(url)

        if oembed.error:
            return {}

        saved_embed, created = SavedEmbed.objects.get_or_create(
                url=url,
                maxwidth=maxwidth,
                defaults={
                    'type': oembed.type,
                    'oembed_data': oembed
                })

    return saved_embed.oembed_data
