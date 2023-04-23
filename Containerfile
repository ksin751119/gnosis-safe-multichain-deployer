FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
CMD ["gnosis_safe_multichain_deployer"]
