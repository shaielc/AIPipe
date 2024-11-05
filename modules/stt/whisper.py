from faster_whisper import WhisperModel
from typing import BinaryIO, Literal, Union
from scipy.signal import resample_poly
import numpy as np

from datatypes.content_types import RawAudioContent

QuantizationType = Literal[
    "int8",
    "int8_float32",
    "int8_float16",
    "int8_bfloat16",
    "int16",
    "float16",
    "bfloat16",
    "float32",
]

class FasterWhisperBackend:
    def __init__(
            self,
            model_size: str,
            device: Literal["cuda", "cpu", "auto"],
            compute_type: QuantizationType
        ) -> None:
        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

    def process(self, audio_content: Union[str, BinaryIO, RawAudioContent]):
        # TODO: figure out passing the sample rate
        if isinstance(audio_content, RawAudioContent):
            audio = resample_poly(audio_content.value, self.model.feature_extractor.sampling_rate, audio_content.sample_rate)
        else:
            audio = audio_content
        segments, _ = self.model.transcribe(audio, language="en")
        
        # TODO: log

        return " ".join([segment.text for segment in segments])
        