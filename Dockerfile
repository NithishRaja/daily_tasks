# Set base image
FROM python:3-slim

# Create a python directory
RUN mkdir /home/daily
RUN mkdir /home/daily/src

# Set workdir
WORKDIR /home/daily

# Copy code
COPY ./src/quote.py /home/daily/src
COPY ./src/day.py /home/daily/src/
COPY ./src/song.py /home/daily/src/
COPY ./index.py /home/daily
COPY ./README.md /home/daily
COPY ./requirements.txt /home/daily

# Install python modules
RUN pip install -r requirements.txt

# Expose volume
VOLUME /mnt

# Set entrypoint
ENTRYPOINT ["python", "index.py"]
