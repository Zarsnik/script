#!/usr/bin/python3
import csv

file=open('data.csv')
zone=open('/var/named/ccs.lab', mode='a')

for line in csv.DictReader(file):
    if line[';nom']) or line['ip']:
        zone.write(line[';nom']+"\t\tA\t"+line['ip']+"\n")
    else:
        print('fichier de donnée corrompu')
zone.close()

