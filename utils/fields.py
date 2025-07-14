from rest_framework.fields import FileField

class CustomFileField(FileField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = None

    def bind(self, field_name, parent):
        super().bind(field_name, parent)
        self.request = parent.context.get('request', None)

    def to_representation(self, value):
        if value and self.request:
            return self.request.build_absolute_uri(value.url)
        return super().to_representation(value)