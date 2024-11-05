from tpipes.stage import ProcessingStage
from tpipes.data import Data
from datatypes.content_types import StringContent, RawAudioContent


class STTStage(ProcessingStage):
    def __init__(self, backend, **kwargs):
        self.backend = backend
        super().__init__(**kwargs)


    def process(self, data: Data[RawAudioContent]):
        text = self.backend.process(data.content)
        return Data[StringContent](StringContent(text), {"source": data})
    
    