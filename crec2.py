#!/usr/bin/env python3
import subs

people = subs.read_csv()

for person in people:
    pass
    #ec2_ip, password = subs.create_ec2(person)
    #print (person[2], ec2_ip, password)

ec2_ip, password = subs.create_ec2(people[0])
print (people[0][2], ec2_ip, password)
