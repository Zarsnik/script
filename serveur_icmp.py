#!/usr/bin/python3

from scapy.all import sniff
from scapy.layers.inet import IP,ICMP
from scapy.packet import Raw
from scapy.sendrecv import sr1,send

while True:
    paquet=sniff(filter='icmp',iface='enp0s3',quiet=True,count=1)
    message=paquet[0].getlayer('Raw').getfieldval('load')
    DESTIP=paquet[0].getlayer('IP').getfieldval('src')
    try:    
        decode=(bytes.fromhex(bytes.decode(message))).decode('utf-8')
        if decode.split("-")[0] == "From Client ":
            text=decode.split("-")[1]
            if text != "FIN":
                print(text)
            else:
                text3=None
                while text3 != "FIN":
                    text3=input("Envoyer un message: ")
                    text2=(("From Client -" + text3).encode('utf-8')).hex()
                    packet=IP(dst=DESTIP)/ICMP()/Raw(load=text2)
                    send(packet,verbose=0)        
    except:
        True

