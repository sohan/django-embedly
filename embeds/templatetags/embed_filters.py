import re
from django import template
from django.conf import settings

from embedly import Embedly
from embeds.models import SavedEmbed

register = template.Library()

#url regex found here: http://daringfireball.net/2010/07/improved_regex_for_matching_urls
URL_REGEX = re.compile(r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))""")

USER_AGENT = 'Mozilla/5.0 (compatible; django-embedly/0.2; ' \
        '+http://github.com/BayCitizen/)'

def _get_url_from_context_variable(var):
    '''
    @var: string, context variable
    Return the first instance of a url in var
    '''
    match = URL_REGEX.search(var)
    if match:
        return match.group(0)
    return None

@register.assignment_tag
def get_oembed_data(context_var, maxwidth=None):
    '''
    A custom templatetag that returns an object representing 
        all oembed data for a given url found in a context variable
    Usage:
    {% load embed_filters %}
    {% with context_var="Check out my cool photo: http://www.flickr.com/photos/visualpanic/233508614/" %}
        {{ context_var }}

        {% get_oembed_data context_var maxwidth=400 as oembed %}
        <div class="embed-data">
            {{oembed.title}} <br />
            {{oembed.description}} <br />
            {{oembed.html}} <br />
        </div>

    {% endwith %}

    Uses the Embedly API to get oembed data. Always look to the db/cache first,
        and then fall back to the Embedly API for speed 
        (at the cost of accuracy & updated urls).
    '''

    url = _get_url_from_context_variable(context_var)
    if not url:
        return {}

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
