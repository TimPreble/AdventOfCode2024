# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.241.1/containers/python-3/.devcontainer/base.Dockerfile

 # [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon)
 # https://mcr.microsoft.com/v2/devcontainers/python/tags/list
 ARG VARIANT="3-bullseye"
 FROM --platform=arm64 mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# Install CURL
RUN apt-get install -y apt-transport-https ca-certificates curl

# Update & Upgrade Environments
RUN apt-get update -qy && apt-get -y upgrade && export DEBIAN_FRONTEND=noninteractive
RUN python -m pip install --upgrade pip

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update -qy && apt-get -y install gcc python3-dev


# [Optional] Uncomment this section to install additional Python packages.
# These are programs that are part of the image but do not need to be published to the remote repo.
RUN pip3 install pytest pylint pylint-pydantic pip-chill
RUN pip3 install pre-commit flake8==6.0.0 black==23.3.0

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&
