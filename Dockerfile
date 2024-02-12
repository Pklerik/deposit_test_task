FROM python:3.11.8-slim-bullseye as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFEERED 1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.11.8-slim-bullseye

RUN apt-get update
RUN groupadd --gid 2005 app \
  && useradd --uid 2005 --gid app --shell /bin/bash --create-home app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFEERED 1
COPY --from=builder --chown=app:app /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN echo "${PATH}"

COPY --chown=app:app ./src /app/src
COPY --chown=app:app ./main.py /app/main.py
COPY --chown=app:app ./tests /app/tests
COPY --chown=app:app ./pyproject.toml /app/pyproject.toml
COPY --chown=app:app ./docker/entrypoints/run_server.sh /app/docker/entrypoints/run_server.sh

WORKDIR /app
USER app

ENTRYPOINT [ "bash", "/app/docker/entrypoints/run_server.sh" ]