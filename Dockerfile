# Set base image
FROM python:3-slim

# Create a python directory
RUN mkdir /home/daily
RUN mkdir /home/daily/src
RUN mkdir /home/daily/www

# Set workdir
WORKDIR /home/daily

# Copy code
COPY ./src/quote.py /home/daily/src
COPY ./src/day.py /home/daily/src/
COPY ./src/song.py /home/daily/src/
COPY ./src/tweet.py /home/daily/src/
COPY ./src/score.py /home/daily/src/
COPY ./src/app.py /home/daily/src/
COPY ./index.py /home/daily
COPY ./README.md /home/daily
COPY ./requirements.txt /home/daily
COPY ./config.json /home/daily

# Copy run script
COPY ./run.sh /home/daily

# Install python modules
RUN pip install -r requirements.txt

# Expose volume
VOLUME /home/daily/data
VOLUME /home/daily/credentials.json

# Expose port
EXPOSE 8000

# Set entrypoint
CMD ./run.sh
