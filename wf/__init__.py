from typing import List, Union

from latch import workflow
from latch.resources.launch_plan import LaunchPlan
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
    """A pipeline to screen MAGs for functional components

    ContigFunc
    ----------

    ContigFunc is a workflow for screening and prediction of functional
    components from metagenomically assembled genomes (MAGs). It's composed of:

    - [Macrel](https://github.com/BigDataBiology/macrel) for predicting Antimicrobial Peptide (AMP)-like sequences
    - [fARGene](https://github.com/fannyhb/fargene) for identifying Antimicrobial Resistance Genes (ARGs)
    - [Gecco](https://github.com/zellerlab/GECCO) for predicting biosynthetic gene clusters (BCGs)

    ### References

    Santos-Júnior CD, Pan S, Zhao X, Coelho LP. 2020.
    Macrel: antimicrobial peptide screening in genomes and metagenomes.
    PeerJ 8:e10555. DOI: 10.7717/peerj.10555

    Berglund, F., Österlund, T., Boulund, F., Marathe, N. P.,
    Larsson, D. J., & Kristiansson, E. (2019).
    Identification and reconstruction of novel antibiotic resistance genes
    from metagenomes. Microbiome, 7(1), 52.

    Accurate de novo identification of biosynthetic gene clusters with GECCO.
    Laura M Carroll, Martin Larralde, Jonas Simon Fleck, Ruby Ponnudurai,
    Alessio Milanese, Elisa Cappio Barazzone, Georg Zeller.
    bioRxiv 2021.05.03.442509; doi:10.1101/2021.05.03.442509

    """
    macrel_results = macrel(contigs=contigs, sample_name=sample_name)
    fargene_results = fargene(
        contigs=contigs, sample_name=sample_name, hmm_model=fargene_hmm_model
    )
    gecco_results = gecco(contigs=contigs, sample_name=sample_name)

    return [macrel_results, gecco_results, fargene_results]


LaunchPlan(
    contigfunc,  # workflow name
    "Test Contigs",  # name of test data
    {
        "contigs": LatchFile("latch:///ExampleSeqs/example_contigs.fna"),
        "sample_name": "example_contigs",
        "fargene_hmm_model": fARGeneModel.class_b_1_2,
    },
)
