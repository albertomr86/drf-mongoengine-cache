from .cache import cache
from .registry import cache_registry
from .settings import api_settings


def get_cache_key(instance, serializer, pattern=False):
    """Get cache key of instance"""

    if not getattr(instance, 'pk', None):
        return None

    params = {
        "id": getattr(instance, 'pk'),
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
        clear_key = get_cache_key(instance, serializer, pattern=api_settings.REMOVE_BY_PATTERN)
        if clear_key:
            keys.append(clear_key)

    if api_settings.REMOVE_BY_PATTERN:
        for key in keys:
            cache.delete_pattern(key)
    else:
        cache.delete_many(keys)
