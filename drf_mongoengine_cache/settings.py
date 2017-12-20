"""
Settings for REST framework cache are all namespaced in the
DRF_MONGOENGINE_CACHE setting. For example your project's `settings.py` file
might look like this:

DRF_MONGOENGINE_CACHE = {
    'DEFAULT_CACHE_TIMEOUT': 86400
}

This module provides the `api_setting` object, that is used to access
REST framework cache settings, checking for user settings first, then falling
back to the defaults.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.test.signals import setting_changed


DEFAULTS = {
    'DEFAULT_CACHE_BACKEND': 'default',
    'DEFAULT_CACHE_TIMEOUT': 86400,
    'SERIALIZER_CACHE_KEY_FORMAT': '{model_name}.{serializer_name}:{id}',
    'REMOVE_BY_PATTERN': False
}


class APISettings(object):

    """
    A settings object, that allows API settings to be accessed as properties.
    For example:

        from rest_framework_cache.settings import api_settings
        print(api_settings.DEFAULT_CACHE_TIMEOUT)

    """

    def __init__(self, defaults=None):
        self.defaults = defaults
        self.settings = getattr(settings, 'DRF_MONGOENGINE_CACHE', {})

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        return val


api_settings = APISettings(DEFAULTS)


def reload_api_settings(*args, **kwargs):
    global api_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'DRF_MONGOENGINE_CACHE':
        api_settings = APISettings(DEFAULTS)


setting_changed.connect(reload_api_settings)
