from datatypes.content_types import StringContent

class EchoBackend:
    """For testing
    """
    def process(self, content: StringContent):
        return content.value