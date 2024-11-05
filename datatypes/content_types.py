from tpipes.data import Data
from tpipes.stage import ProcessingStage
from enum import Enum
from typing import Any, Protocol
from dataclasses import dataclass

class ContentType(Enum):
    STRING = 0
    RAW_AUDIO = 1

class Content(Protocol):
    type: ContentType
    value: Any

class StringContent:
    type = ContentType.STRING
    
    def __init__(self, value):
        self.value = value

class RawAudioContent:
    type = ContentType.RAW_AUDIO

    def __init__(self, value, sample_rate):
        self.value = value
        self.sample_rate = sample_rate