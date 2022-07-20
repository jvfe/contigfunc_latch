from typing import List, Union

from latch import workflow
from latch.types import LatchDir, LatchFile

from .amp import macrel
from .arg import fargene
from .bgc import gecco
from .docs import CONTIGFUNC_DOCS
from .types import fARGeneModel


@workflow(CONTIGFUNC_DOCS)
def contigfunc(
    contigs: LatchFile,
    sample_name: str = "contigfunc_sample",
    fargene_hmm_model: fARGeneModel = fARGeneModel.class_a,
) -> List[Union[LatchFile, LatchDir]]:
    macrel_results = macrel(contigs=contigs, sample_name=sample_name)
    fargene_results = fargene(
        contigs=contigs, sample_name=sample_name, hmm_model=fargene_hmm_model
    )
    gecco_results = gecco(contigs=contigs, sample_name=sample_name)

    return [macrel_results, gecco_results, fargene_results]
