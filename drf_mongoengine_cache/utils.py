from .cache import cache
from .registry import cache_registry
from .settings import api_settings


def get_cache_key(instance, serializer, pattern=False):
    """Get cache key of instance"""

    params = {
        "id": instance.pk,
        "model_name": instance._meta.get('collection'),
        "serializer_name": serializer.__name__
    }

    key = api_settings.SERIALIZER_CACHE_KEY_FORMAT.format(**params)

    return '%s*' % key if pattern else key


def clear_for_instance(instance):
    """Clear the cache for the given instance"""

    keys = []
    serializers = cache_registry.get(instance.__class__)

    for serializer in serializers:
        keys.append(get_cache_key(instance, serializer, pattern=api_settings.REMOVE_BY_PATTERN))

    if api_settings.REMOVE_BY_PATTERN:
        for key in keys:
            cache.delete_pattern(key)
    else:
        cache.delete_many(keys)
