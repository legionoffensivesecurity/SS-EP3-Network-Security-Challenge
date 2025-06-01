# Use Kali Linux base image
FROM kalilinux/kali-rolling

LABEL name="attacker"

# Update package list and install required packages
RUN apt update -y \
    && apt install -y \
    nmap \
    iputils-ping \
    net-tools \
    iproute2 \
    ncat \
    openssh-server \
    sudo \
    && [ ! -d /var/run/sshd ] && mkdir -p /var/run/sshd || true


# Create 'destiny' user and set its password
RUN useradd -m -s /bin/bash destiny \
    && echo "destiny:optimusprime" | chpasswd

COPY note.txt /home/destiny/

# Expose SSH port 22
EXPOSE 22

# Start SSH service and keep the container running
CMD ["/usr/sbin/sshd", "-D"]
