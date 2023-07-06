from django.urls.converters import UUIDConverter as DefaultUUIDConverter

class UUIDConverter(DefaultUUIDConverter):
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

