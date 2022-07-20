import subprocess
from pathlib import Path

from latch import small_task
from latch.types import LatchDir, LatchFile


@small_task
def gecco(contigs: LatchFile, sample_name: str) -> LatchDir:

    output_dir_name = "gecco_results"
    outdir = Path(output_dir_name).resolve()

    _gecco_cmd = [
        "gecco",
        "run",
        "-g",
        str(contigs.local_path),
        "-o",
        output_dir_name,
        "-j",
        "4",
        "--force-tsv",
    ]

    subprocess.run(_gecco_cmd)

    return LatchDir(str(outdir), f"latch:///contigfunc_{sample_name}/{output_dir_name}")
