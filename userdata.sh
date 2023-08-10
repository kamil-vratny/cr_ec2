#!/bin/sh

echo "ec2-user:<PASSWORD>" | chpasswd
perl -pi -e 's/PasswordAuthentication\s+no/PasswordAuthentication yes/gi' /etc/ssh/sshd_config
systemctl restart sshd
