FROM python:3.5.3

# Create app directory
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Bundle app source
COPY . /usr/src/app

CMD [ "python", "run.py" ]
