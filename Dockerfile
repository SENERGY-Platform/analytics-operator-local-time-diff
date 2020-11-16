FROM python:3.7-alpine
LABEL org.opencontainers.image.source https://github.com/SENERGY-Platform/analytics-operator-local-time-diff

ADD . /opt/app
WORKDIR /opt/app
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://www.piwheels.org/simple
CMD [ "python", "./main.py" ]