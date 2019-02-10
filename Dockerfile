from dispatchframework/python3-base:0.0.14-knative
COPY handler.py /function/
COPY requirements.txt /function/
CMD SERVER_CMD="pip install -r requirements.txt & python3 /function-server/main.py handler.handler" ./funky