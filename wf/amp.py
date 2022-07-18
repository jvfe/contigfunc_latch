import subprocess
from pathlib import Path

from latch import small_task
from latch.types import LatchDir, LatchFile


@small_task
def macrel(contigs: LatchFile, sample_name: str) -> LatchDir:

    output_dir_name = "macrel_results"
    outdir = Path(output_dir_name).resolve()

    _macrel_cmd = [
        "macrel",
        "contigs",
        "--fasta",
        str(contigs),
        "--output",
        str(outdir),
        "--tag",
        sample_name,
        "--log-file",
        f"{str(outdir)}/{sample_name}_log.txt",
        "--threads",
        "8",
    ]

    subprocess.run(_macrel_cmd)

    return LatchDir(str(outdir), f"latch:///contigfunc/{sample_name}/{output_dir_name}")
