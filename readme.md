# Caesar cipher

This is a simple implementation of the caesar cipher in Python, in addition to a tool to analyze character usage in an encrypted file, for guessing for example the e.

Encrypt the file `text/plain.txt` with key `t`:
```
./caesar.py encrypt t text/plain.txt
```

Encrypt own text:
```
echo "Encrypt this, please!" | ./caesar.py encrypt t
```

Statistics on file:
```
./charstat text/plain.txt
```

Statistics on own text:
```
echo "aaaaaaabbbbbbcccd" | ./charstat
```
