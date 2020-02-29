from scapy.all import *
import socket


def packet_check(packet):
    if packet[TCP].payload:
        if packet[IP].dport == 80:
            print("\n{} ----HTTP----> {}:{}:\n{}".format(packet[IP].src, packet[IP].dst, packet[IP].dport, str(bytes(packet[TCP].payload))))


def main():
    out_string = ""
    i = 1
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(IPAddr)
    while True:
        pkt = sniff(count=1, filter='tcp', prn=packet_check)
        # print("###############")
        print("Packet #" + str(i))
        print("\n" + str(pkt[0][IP].src) + ":" + str(pkt[0][TCP].sport) + "-->" + str(pkt[0][IP].dst) + ":" + str(pkt[0][TCP].dport)+ "\n")
        i = i + 1


if __name__ == '__main__':
    main()
