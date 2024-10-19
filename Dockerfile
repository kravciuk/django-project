# Specifying base image
FROM python:3.12-slim

ENV HOME=/code

# Generation of pyc files
ENV PYTHONDONTWRITEBYTECODE 0
# stdout and stderr streams are not buffered and sent straight to your terminal
ENV PYTHONUNBUFFERED 1

# Setting work directory
WORKDIR $HOME

# Copying the project data into work directory
COPY . $HOME

# install poetry
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==1.8.3
RUN ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry

RUN apt-get update -y && apt-get install -y \
    gdal-bin  \
    libgdal-dev \
    python3-gdal \
    binutils \
    libproj-dev \
    gettext make

RUN poetry install
RUN make var

ENTRYPOINT ["poetry", "run", "python", "src/manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

#EXPOSE 8080
#
#RUN poetry run src/manage.py runserver 0.0.0.0:8080

