FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:9a7d-main

RUN apt-get install -y curl unzip libz-dev

# Install Prodigal
RUN curl -L https://github.com/hyattpd/Prodigal/releases/download/v2.6.3/prodigal.linux -o prodigal &&\
    chmod +x prodigal

# Get miniconda
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output miniconda.sh
ENV CONDA_DIR /opt/conda
RUN bash miniconda.sh -b -p /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# Get Mamba
RUN conda install mamba -n base -c conda-forge

# Get Macrel
RUN mamba install -y -c bioconda macrel 
# RUN conda create -y -n contigfunc python=3.9
# RUN conda install -y -n contigfunc -c bioconda macrel
# ENV FUNC_ENV /opt/conda/envs/contigfunc/bin

# Create symlink
# RUN ln -s $FUNC_ENV/macrel /root/macrel

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN python3 -m pip install --upgrade latch
WORKDIR /root

