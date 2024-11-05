from tpipes.data import Data
from tpipes.stage import ProcessingStage
from datatypes.content_types import StringContent

class LLMStage(ProcessingStage):
    def __init__(self, backend, **kwargs) -> None:
        self.backend = backend
        super().__init__(**kwargs)

    def process(self, data: Data[StringContent]) -> Data[StringContent]:
        text = self.backend.process(data.content.value)
        return Data[StringContent](StringContent(text), {"source": data})