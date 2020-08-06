FROM python:3

RUN apt-get update && \
	apt-get install -y \
		potrace

ENV APP_HOME /app
ENV PATH_WEIGHTS $APP_HOME/weights
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install -r requirements.txt

CMD ["python", "tools.py"]
