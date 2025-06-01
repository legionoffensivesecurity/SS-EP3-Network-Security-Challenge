FROM alpine:latest

# Install socat and python3
RUN apk add --no-cache socat python3

# Set up the directory and copy files
RUN mkdir -p /root/.hidden
COPY script.py /root/.hidden/
COPY flag.txt /flag.txt

# Expose port 1337 for the container
EXPOSE 1337

# Command to run the script using socat on port 1337
CMD ["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:/usr/bin/python3 /root/.hidden/script.py"]

