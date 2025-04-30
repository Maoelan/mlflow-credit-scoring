FROM python:3.12.7-slim

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    nginx \
    gcc \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/mlflow

RUN pip install mlflow==2.18.0

COPY model_dir/model /opt/ml/model
COPY model_dir/model/requirements.txt /opt/ml/model/requirements.txt
RUN pip install --no-cache-dir -r /opt/ml/model/requirements.txt

RUN python -c "from mlflow.models import container as C; C._install_pyfunc_deps('/opt/ml/model', install_mlflow=False, enable_mlserver=False, env_manager='local');"

ENV MLFLOW_DISABLE_ENV_CREATION=True
ENV ENABLE_MLSERVER=False

RUN chmod o+rwX /opt/mlflow/

RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python", "-c", "from mlflow.models import container as C; C._serve('local')"]