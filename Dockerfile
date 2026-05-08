FROM ghcr.io/astral-sh/uv:0.11-trixie

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
      git  \
      curl  \
      gnupg  \
      unixodbc  \
      unixodbc-dev  \
      freetds-bin  \
      freetds-dev  \
      tdsodbc  \
      odbc-postgresql \
    && rm -rf /var/lib/apt/lists/* \
    \
    # Microsoft ODBC 17 \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update -y && \
    ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql17 \
    \
    # Microsoft ODBC 18 \
    # Download the package to configure the Microsoft repo \
    && curl -sSL -O "https://packages.microsoft.com/config/debian/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2 | cut -d '.' -f 1)/packages-microsoft-prod.deb" \
    # Install the package \
    && dpkg -i packages-microsoft-prod.deb \
    # Delete the file \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
    \
    # MySQL Driver \
    && curl -L -o mysql-connector-odbc.deb https://dev.mysql.com/get/Downloads/Connector-ODBC/9.7/mysql-connector-odbc_9.7.0-1debian12_amd64.deb \
    && dpkg -i mysql-connector-odbc.deb \
    && rm mysql-connector-odbc.deb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY pyproject.toml uv.lock ./

ARG UV_PYTHON=python3.10
ENV UV_PYTHON=${UV_PYTHON}
RUN uv sync --locked
