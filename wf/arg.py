import subprocess
from pathlib import Path

from latch import small_task
from latch.types import LatchDir, LatchFile


@small_task
def fargene(contigs: LatchFile, sample_name: str, hmm_model: str) -> LatchDir:

    output_dir_name = "fargene_results"
    outdir = Path(output_dir_name).resolve()

    _fargene_cmd = [
        "fargene",
        "-i",
        str(contigs),
        "--hmm-model",
        hmm_model,
        "-o",
        output_dir_name,
        "--logfile",
        f"{output_dir_name}/{sample_name}_fargene.log",
        "-p",
        "8",
    ]

    subprocess.run(_fargene_cmd)

    return LatchDir(str(outdir), f"latch:///contigfunc/{sample_name}/{output_dir_name}")