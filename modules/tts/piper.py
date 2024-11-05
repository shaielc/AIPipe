from datatypes.content_types import RawAudioContent


class PiperBackend:
    def __init__(self, model_path) -> None:
        self.model_path = model_path
