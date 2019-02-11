from dispatchframework/python3-base:0.0.14-knative

COPY handler.py /function/
COPY requirements.txt /function/

RUN pip install -r /function/requirements.txt

CMD SERVER_CMD="python3 /function-server/main.py handler.handler" ./funky