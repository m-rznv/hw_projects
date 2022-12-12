FROM python:3.11

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install poetry


COPY . /app/
# COPY ["poetry.lock", "pyproject.toml", "/hw_projects/"]
RUN poetry install
# COPY . /app
CMD ["python", "__main__.py"]