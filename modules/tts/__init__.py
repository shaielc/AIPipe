from tpipes.stage import ProcessingStage
from tpipes.data import Data
from datatypes.content_types import StringContent, RawAudioContent


class TTSStage(ProcessingStage):
    def __init__(self, backend, **kwargs):
        self.backend = backend
        super().__init__(**kwargs)


    def process(self, data: Data[StringContent]):
        audio, sample_rate = self.backend.process(data.content)
        return Data[RawAudioContent](
            RawAudioContent(
                audio, sample_rate
            ),
            {"source": data}
        )
    
    