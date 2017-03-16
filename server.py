import socket
import sys

from os import environ
alpr_dir = "C:\\Users\\chris\\Desktop\\openalpr_64"
environ['PATH'] = alpr_dir + ';' + environ['PATH']

from openalpr import Alpr

alpr = None
conf = "C:\\Users\\chris\\Desktop\\openalpr_64\\openalpr.conf"
run = "C:\\Users\\chris\\Desktop\\openalpr_64\\runtime_data"
alpr = Alpr("eu", conf, run)

TCP_IP = '127.0.0.1'
TCP_PORT = 9999
BUFFER_SIZE = 1024

# s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)


while True:
    sc, address = s.accept()
    # sc, address = s.accept()
    print(address)
    f = open('file.jpg', 'wb')  # open in binary

    l = 1
    while(l):
        l = sc.recv(1024)
        while (l):
            f.write(l)
            l = sc.recv(1024)
        f.close()

    


    #alpr.set_top_n(20)
    alpr.set_detect_region(True)
    f = open("file.jpg", "rb")
    jpeg_bytes = f.read()
    results = alpr.recognize_array(jpeg_bytes)

    # for plate in results['results']:
    #     for candidate in plate['candidates']:
    #        print(candidate['plate'])
    #     print(plate['candidates'][0]['plate'])

    result = results['results'][0]['candidates'][0]['plate']
    print(result)
    sc.send(result.encode('utf-8'))

    # i = 0
    # for plate in results['results']:
    #     i += 1
    #     print("Plate #%d" % i)
    #     print("   %12s %12s" % ("Plate", "Confidence"))
    #     for candidate in plate['candidates']:
    #         prefix = "-"
    #         if candidate['matches_template']:
    #             prefix = "*"

    #         print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
    
    # zamkniecie pliku po odczytaniu tablicy
    f.close()
    # zakonczenie polaczenia
    sc.close()
s.close()
