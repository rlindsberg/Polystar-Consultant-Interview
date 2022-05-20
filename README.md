# Polystar-Consultant-Interview

# HiQ-Code-Interview

### How to Run This Code

To setup a conda env:
```console
karlemstrand@MSI-GS63:~$ conda update -n base conda
karlemstrand@MSI-GS63:~$ conda create --name star-py39 python=3.9
karlemstrand@MSI-GS63:~$ conda activate star-py39
(star-py39) karlemstrand@MSI-GS63:~$ git clone https://github.com/rlindsberg/Polystar-Consultant-Interview.git && cd Polystar-Consultant-Interview
$ python server.py -p 50001
```
In another terminal:
```console
$ python server.py -p 50000
```
In another terminal:
```console
$ python client.py
```

### Task
- Two (2) servers shall read and expose one text file each. (frankenstein.txt and dracula.txt)
- One (1) client shall read and count the data from the two servers in parallel. As a suggestion the communication between server and client use sockets.
- The code should work just as well for very large files, thus do not keep entire files in memory at any time.
- The result shall be one (1) print out of the 5 most common words in the two texts with the total number of occurrences of the word.

### Description
This program reads all files in a given directory and counts the most common words. Right now it runs locally with a single thread.

The input files are dracula.txt and frankenstein.txt.

The results are [('the', 12483), ('and', 9018), ('i', 7692), ('to', 6919), ('of', 6517)], which looks reasonable.

### Transmission protocol

send_text()
1. client sends header - send_header()
2. server stores header, sends res - sendall()
3. client checks res == header
4. client sends payload - send_payload()
5. server stores payload, sends res - sendall()
6. client checks res == payload

send_dict()
server computes word frequency
1. server sends header - send_header()
2. client stores header, sends res
3. server checks res == header
4. server sends json dump - send_json_dump()
5. client stores json dump, sends res - sendall()
6. server checks res == json dump
