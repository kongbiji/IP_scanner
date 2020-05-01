from scapy.all import *
import sys

s=[]

for i in range(1,255):
        ##input subnet
	arp_req=Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=sys.argv[1]+"."+str(i))
	arp_ans=srp1(arp_req, timeout=0.5)
	if arp_ans:
                ## if ans exist, save
		s.append(str(sys.argv[1]+"."+str(i)+" is at "+arp_ans[ARP].hwsrc))

## print hosts
for j in range(0,len(s)):
	print(s[j])
