FROM python:3.9-buster

RUN pip install flask && \
    groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -ms /sbin/nologin appuser

USER appuser

WORKDIR /home/appuser

COPY . /home/appuser/

ENTRYPOINT ["python", "/home/appuser/app.py"]
EXPOSE 5000
