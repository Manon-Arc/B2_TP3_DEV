# TP3 DEV : Python et réseau

# V. Deploy

Déployez-moi ça dans une VM Rocky :

- git clone du dépôt git de code, dans la VM

```bash
[manon@python-dev ~]$ sudo dnf install git

[manon@python-dev ~]$ git clone https://github.com/Manon-Arc/B2_TP3_DEV.git
Cloning into 'B2_TP3_DEV'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```
- install/mise à jour de Python si nécessaire
```bash
[manon@python-dev ~]$ python3 --version
Python 3.9.16

[manon@python-dev ~]$ sudo dnf install pip -y

[manon@python-dev ~]$ pip install psutil
```
- exécution du code, le code doit fonctionner normalement
```bash
[manon@python-dev B2_TP3_DEV]$ python code/network.py lookup ynov.com
172.67.74.226

[manon@python-dev B2_TP3_DEV]$ python code/network.py ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=30.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=31.3 ms
^C
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 30.324/30.816/31.308/0.492 ms
UP !

[manon@python-dev B2_TP3_DEV]$ python code/network.py ip
None

[manon@python-dev B2_TP3_DEV]$ python code/network.py fbjydfv
'fbjydfv' is not an available command. Déso.
```