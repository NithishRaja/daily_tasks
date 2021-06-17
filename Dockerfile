# Set base image
FROM python:3-slim

# Create a python directory
RUN mkdir /home/daily
RUN mkdir /home/daily/data
RUN mkdir /home/daily/src
RUN mkdir /home/daily/www
RUN mkdir /home/daily/www/js
RUN mkdir /home/daily/userData

# Set workdir
WORKDIR /home/daily

# Copy scripting code
COPY ./src/* /home/daily/src/
COPY ./index.py /home/daily/

# Copy UI code
COPY ./www/index.html /home/daily/www/
COPY ./www/js/* /home/daily/www/js/
COPY ./index.html /home/daily/

# Copy configurations
COPY ./README.md /home/daily
COPY ./.dockerignore /home/daily
COPY ./requirements.txt /home/daily
COPY ./config.json /home/daily

# Copy run script
COPY ./run.sh /home/daily

# Install python modules
RUN pip install -r requirements.txt

# Expose volume
VOLUME /home/daily/userData
VOLUME /home/daily/data
VOLUME /home/daily/credentials.json

# Expose port
EXPOSE 8000

# Set entrypoint
CMD ./run.sh
