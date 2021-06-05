# Set base image
FROM python:3-slim

# Create a python directory
RUN mkdir /home/daily

# Set workdir
WORKDIR /home/daily

# Copy code
COPY ./quote.py /home/daily
COPY ./day.py /home/daily
COPY ./song.py /home/daily
COPY ./index.py /home/daily
COPY ./README.md /home/daily
COPY ./requirements.txt /home/daily

# Install python modules
RUN pip install -r requirements.txt

# Expose volume
VOLUME /mnt

# Set entrypoint
ENTRYPOINT ["python", "index.py"]
