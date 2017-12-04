FROM alpine:latest
RUN apk add --no-cache gcc g++ make python python-dev openssl-dev py-pip libffi-dev py-mysqldb\
	&& pip install --upgrade pip \
	&& pip install jira \
    && pip install paramiko \
    && apk del gcc g++ make openssl-dev python-dev \
    && rm -rf /var/cache/apk/*
COPY src /src
ENV APP_DIR /src
CMD ["/usr/bin/python", "/src/main.py"]
