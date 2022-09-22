FROM python:3.8-slim

RUN mkdir /workspace/
WORKDIR /workspace/
ADD . /workspace/
ENV TZ=Asia/Shanghai
ENV EXTERNAL_PYPI_SERVER=https://mirrors.aliyun.com/pypi/simple/
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && python -m venv /opt/venv \
    && /bin/bash -c "source /opt/venv/bin/activate" \
    && pip install -i $EXTERNAL_PYPI_SERVER --upgrade pip \
    && pip install -i $EXTERNAL_PYPI_SERVER --upgrade pip poetry \
    && poetry install
ENTRYPOINT ["poetry", "run"]
