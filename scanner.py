from scapy.all import *
import sys

s=[]

for i in range(1,255):
        ##서브넷 주소만 입력받기
	arp_req=Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=sys.argv[1]+"."+str(i))
	arp_ans=srp1(arp_req, timeout=0.5)
	if arp_ans:
                ##존재한다면 저장
		s.append(str(sys.argv[1]+"."+str(i)+" is at "+arp_ans[ARP].hwsrc))

##실행중인 호스트들 출력
for j in range(0,len(s)):
	print(s[j])
