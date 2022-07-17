from latch.types import LatchAuthor, LatchMetadata, LatchParameter, LatchRule

CONTIGFUNC_DOCS = LatchMetadata(
    display_name="ContigFunc",
    documentation="https://github.com/jvfe/contigfunc_latch/blob/main/README.md",
    author=LatchAuthor(
        name="jvfe",
        github="https://github.com/jvfe",
    ),
    repository="https://github.com/jvfe/contigfunc_latch",
    license="MIT",
)

CONTIGFUNC_DOCS.parameters = {
    "contigs": LatchParameter(
        display_name="Assembled Contigs",
        description="FASTA file with assembled contigs",
        section_title="Data",
    ),
    "sample_name": LatchParameter(
        display_name="Sample name",
        description="Sample name (will define output file names)",
    ),
}
