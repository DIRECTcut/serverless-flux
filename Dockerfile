FROM runpod/base:0.6.2-cuda12.2.0

LABEL authors="jaret"

# Install dependencies
RUN apt-get update

WORKDIR /app
ARG CACHEBUST=1
RUN git clone https://github.com/ostris/ai-toolkit.git && \
    cd ai-toolkit && \
    git submodule update --init --recursive

WORKDIR /app/ai-toolkit

RUN ln -s /usr/bin/python3 /usr/bin/python
COPY builder/requirements.txt /requirements.txt
RUN python -m pip install -r /requirements.txt && \
    rm /requirements.txt

# RUN apt-get install -y tmux nvtop htop

# RUN pip install jupyterlab

# mask workspace
RUN mkdir /workspace

# symlink app to workspace
RUN ln -s /app/ai-toolkit /workspace/ai-toolkit
WORKDIR /workspace/ai-toolkit
RUN pip install torch && \
    pip install -r requirements.txt
#  python3 -m venv venv && \
#  . venv/bin/activate && \

COPY 2d59bb4c-eeb6-4d33-84d8-448762135f11 datasets/2d59bb4c-eeb6-4d33-84d8-448762135f11
COPY 1da5c2fa-47db-48b0-82eb-7e599df3ff34-marie-3.yaml tmp/
COPY my.py /workspace/ai-toolkit

# CMD ["/start.sh"]
CMD ["sleep", "infinity"]