from typing import List, Union

from latch import workflow
from latch.types import LatchDir, LatchFile

from .amp import macrel
from .arg import fargene
from .docs import CONTIGFUNC_DOCS


@workflow(CONTIGFUNC_DOCS)
def contigfunc(
    contigs: LatchFile, sample_name: str = "contigfunc_sample", fargene_hmm_model: str = "class_a"
) -> List[Union[LatchFile, LatchDir]]:
    macrel_results = macrel(contigs=contigs, sample_name=sample_name)
    fargene_results = fargene(contigs=contigs, sample_name=sample_name, hmm_model=fargene_hmm_model)
    return [macrel_results, fargene_results]
