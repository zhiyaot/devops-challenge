FROM almalinux:latest

# Install minimum dependencies to support pipenv
RUN dnf install -y python3 python3-pip which && \
  pip3 install --no-cache-dir pipenv

COPY . /app
WORKDIR /app

# Install from Pipfile
RUN pipenv install --python 3

CMD ["pipenv", "run", "/app/index.py"]