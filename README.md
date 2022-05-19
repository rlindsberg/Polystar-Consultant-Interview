# Polystar-Consultant-Interview

This program reads all files in a given directory and counts the most common words. Right now it runs locally with a single thread.

The input files are dracula.txt and frankenstein.txt.

The results are [('the', 12483), ('and', 9018), ('i', 7692), ('to', 6919), ('of', 6517)], which looks reasonable.

The transmission protocol is as follows:

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
