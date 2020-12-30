FROM python:3.6

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
ADD src/requirements.txt /app/requirements.txt
RUN python3.6 -m pip install -r /app/requirements.txt

WORKDIR /
ADD src /app

EXPOSE $PORT
CMD python3.6 /app/main.py $PORT