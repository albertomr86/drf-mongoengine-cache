from rest_framework import serializers

from .cache import cache
from .settings import api_settings
from .utils import get_cache_key


class CachedSerializerMixin(serializers.ModelSerializer):

    def _get_context_cache_key(self, instance):
        return ''

    def _get_cache_key(self, instance):
        base_key = get_cache_key(instance, self.__class__, pattern=False)

        return '%s%s' % (base_key, self._get_context_cache_key(instance=instance))

    def to_representation(self, instance):
        """
        Checks if the representation of instance is cached and adds to cache
        if is not.
        """

        key = self._get_cache_key(instance)
        cached = cache.get(key)

        if cached:
            return cached

        result = super(CachedSerializerMixin, self).to_representation(instance)
        cache.set(key, result, api_settings.DEFAULT_CACHE_TIMEOUT)

        return result
