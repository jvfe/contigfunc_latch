from typing import List, Union

from latch import workflow
from latch.types import LatchDir, LatchFile

from .amp import macrel
from .docs import CONTIGFUNC_DOCS


@workflow(CONTIGFUNC_DOCS)
def contigfunc(
    contigs: LatchFile, sample_name: str = "contigfunc_sample"
) -> List[Union[LatchFile, LatchDir]]:
    macrel_results = macrel(contigs=contigs, sample_name=sample_name)

    return [macrel_results]
