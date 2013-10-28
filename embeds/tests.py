from django.test import TestCase
from embeds.templatetags.embed_filters import get_oembed_data
from embeds.models import SavedEmbed

class EmbedlyTemplateFilterTest(TestCase):
    def setUp(self):
        text = {}

        text['photo'] = """<p>Wish I was here..</p>
        http://www.flickr.com/photos/visualpanic/233508614/
        <p>!!!</p>
        """

        text['noop'] = """walk the line like an egyptian, but do not mess wit my links!"""

        self.text = text

    def test_photo_embed(self):
        oembed_data = get_oembed_data(self.text['photo'])

        #test that the db object exists
        saved_embed = SavedEmbed.objects.all()[0]
        self.assertTrue(saved_embed.oembed_data.keys())
        self.assertEquals(saved_embed.oembed_data['provider_url'], u'http://www.flickr.com/')

        self.assertEquals(oembed_data, saved_embed.oembed_data)

    def test_maxwidth(self):
        oembed_data = get_oembed_data(self.text['photo'], maxwidth=300)

        #test that the db object exists
        saved_embed = SavedEmbed.objects.all()[0]
        self.assertTrue(saved_embed.oembed_data.keys())
        self.assertEquals(saved_embed.oembed_data['provider_url'], u'http://www.flickr.com/')
        self.assertTrue(saved_embed.oembed_data['width'] <  300)

        self.assertEquals(oembed_data, saved_embed.oembed_data)

    def test_maxwidth_and_maxheight(self):
        oembed_data = get_oembed_data(self.text['photo'], maxwidth=300, maxheight=300)

        #test that the db object exists
        saved_embed = SavedEmbed.objects.all()[0]
        self.assertTrue(saved_embed.oembed_data.keys())
        self.assertEquals(saved_embed.oembed_data['provider_url'], u'http://www.flickr.com/')
        self.assertTrue(saved_embed.oembed_data['width'] <  300)
        self.assertTrue(saved_embed.oembed_data['height'] <  300)

        self.assertEquals(oembed_data, saved_embed.oembed_data)



    def test_leave_my_links_in_peace(self):
        oembed_data = get_oembed_data(self.text['noop'])
        self.assertFalse(oembed_data)

    def test_unique_constraint(self):
        get_oembed_data(self.text['photo'], maxwidth=300)
        self.assertEquals(SavedEmbed.objects.count(), 1)
        get_oembed_data(self.text['photo'], maxwidth=300)
        self.assertEquals(SavedEmbed.objects.count(), 1)

        get_oembed_data(self.text['photo'])
        self.assertEquals(SavedEmbed.objects.count(), 2)
