sohan / django-embedly
===========================

This package provides a template tag to parse embed URLs and call the
embedly API to generate oembed data, that you can use in your HTML.

Installation
------------

Install requirements: pip install -r requirements.txt

Add 'embeds' to INSTALLED_APPS in settings.py.

Run syncdb or manage.py migrate, if you use South.

Also, under django's settings.py add an entry for

EMBEDLY_KEY = <embedly key>

which can be obtained by signing up for the service.

Usage
-----

Given a template context variable that looks like::

    my_text = """
    The following line will be replaced with video embed HTML.

    http://www.youtube.com/watch?v=DCL1RpgYxRM
    """

Include these lines in your template to embed the youtube video with a maximum
width of 400px::

    {% load embed_filters %}
    {{ my_text }}

    {% get_oembed_data my_text maxwidth=400 as oembed %}
    {% if oembed %}
        <div class="embed-data">
            {{oembed.title}} <br />
            {{oembed.description}} <br />
            {{oembed.html}} <br />
        </div>
    {% endif %}
