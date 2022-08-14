FROM python:3.8

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /var/sentry-test
ADD ./src /var/sentry-test

RUN python -m pip install --upgrade pip
RUN pip install --upgrade sentry-sdk
RUN pip install python-dotenv