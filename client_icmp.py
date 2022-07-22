#!/usr/bin/python3
from scapy.all import sniff
from scapy.layers.inet import IP,ICMP
from scapy.packet import Raw
from scapy.sendrecv import sr1,send


DESTIP=input("Veuillez saisir l'adresse ip de destination: ")
text=None
while text != "FIN":
	text=input("Envoyer un message: ")
	text2=(("From Client -" + text).encode('utf-8')).hex()
	packet=IP(dst=DESTIP)/ICMP()/Raw(load=text2)
	send(packet,verbose=0)

while True:
    paquet=sniff(filter='icmp',iface='enp0s3',quiet=True,count=1)
    message=paquet[0].getlayer('Raw').getfieldval('load')
    try:
        decode=(bytes.fromhex(bytes.decode(message))).decode('utf-8')
        if decode.split("-")[0] == "From Client ":
            text2=decode.split("-")[1]
            if text2 != "FIN":
                print(text2)
            else:
                text=None
                while text != "FIN":
                    text=input("Envoyer un message: ")
                    text=(("From Client - " + text).encode('utf-8')).hex()
                    packet=IP(dst=DESTIP)/ICMP()/Raw(load=text2)
                    send(packet,verbose=0)
    except:
        True

