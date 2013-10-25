from setuptools import setup

setup(
    name='django-embedly',
    version='0.3',
    description='Provides a templatetag to parse embed URLs and talk to embedly API',
    author='sohan',
    author_email='',
    url='http://github.com/sohan/django-embedly/',
    packages=[
        'embeds',
    ],

    install_requires=[
        'distribute',
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
