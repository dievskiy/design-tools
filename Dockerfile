FROM python:3

RUN apt-get update && \
	apt-get install -y \
		potrace \
        imagemagick

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

EXPOSE 8080
EXPOSE 80

#RUN pip install Flask requests
RUN pip install -r requirements.txt
CMD ["python", "tools.py"]