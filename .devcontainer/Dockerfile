FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

COPY . .

RUN pip install -r requirements.txt
RUN python -m ipykernel install --user