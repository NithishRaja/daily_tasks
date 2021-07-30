# Set base image
FROM python:3-slim

# Install nodejs and npm
RUN apt-get update -y && apt-get install -y nodejs npm build-essential

# Create a python directory
RUN mkdir /home/daily
RUN mkdir /home/daily/src
RUN mkdir /home/daily/userData
RUN mkdir /home/daily/server

# Set workdir
WORKDIR /home/daily

# Copy scripting code
ADD ./src/ /home/daily/src/

# Copy UI code
ADD ./server/ /home/daily/server/

# Copy configurations
COPY ./README.md /home/daily
COPY ./.dockerignore /home/daily
COPY ./requirements.txt /home/daily
COPY ./package.json /home/daily
COPY ./config.json /home/daily

# Install python modules
RUN pip install -r requirements.txt

# Install node modules
RUN npm install

# Expose volume
VOLUME /home/daily/userData

# Expose port
EXPOSE 8000

# Set entrypoint
CMD ["python", "src/main.py"]
