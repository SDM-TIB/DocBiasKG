# use an official Python image as base
FROM python:3.8.16-slim-bullseye

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends graphviz && \
    rm -rf /var/lib/apt/lists/*  && \
    python -m pip install --no-cache-dir --upgrade pip==23.0.* setuptools==58.0.*

# copy the source code and install InterpretME
COPY DocBias_over_InterpretME/README.md /InterpretME/
COPY DocBias_over_InterpretME/requirements.txt /InterpretME/
WORKDIR /InterpretME
RUN python -m pip install --no-cache-dir -r requirements.txt
