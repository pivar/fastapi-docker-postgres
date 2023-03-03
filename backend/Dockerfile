FROM python:3.10.8-slim-buster
# creates a directory with this name if it doesn’t exist
RUN echo "OK HERE1"
RUN mkdir /backend
WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
	&& apt-get clean

RUN pip install --upgrade pip
# Install any needed packages specified in dependencies.txt
COPY ./dependencies.txt .
RUN pip install -r dependencies.txt
COPY . .
RUN ls

# add permission for entrypoint.sh
RUN chmod +x entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/backend/entrypoint.sh"]