FROM rocker/r-base:4.4.1

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
libssl-dev libcurl4-openssl-dev libxml2-dev && \
rm -rf /var/lib/apt/lists/*
  
  RUN R -e "install.packages(c('plumber','jsonlite','httr'), repos='https://cloud.r-project.org')"

WORKDIR /app
COPY . /app
