FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit==2023.9.2
RUN pip install datamol==0.12.1
RUN pip install molfeat==0.9.5
RUN conda install -c conda-forge xorg-libxrender xorg-libxtst

WORKDIR /repo
COPY . /repo
