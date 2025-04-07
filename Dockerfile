# base
FROM registry.access.redhat.com/ubi9/python-312@sha256:200ee63ff54631677b52b35d5b63f7610ff5231f9052b4a8af2a974190523dd0
# set working directory for image
WORKDIR /app

#install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

USER root

# copy files from repo
COPY ./app /app

RUN chown -R 1000770000:1000770000 /app
USER 1000770000

EXPOSE 8080

#start application
CMD ["streamlit", "run", "Home.py", "--server.port", "8080"]
