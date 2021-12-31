# set base image (host OS)
FROM python:3.10.1

ADD main.py .

# install dependencies
RUN pip install requests beautifulsoup4


# command to run on container start
CMD [ "python", "./main.py" ]