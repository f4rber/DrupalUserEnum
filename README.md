# DrupalUserEnum
Script to enumerate Drupal users
```
usage: drupal_user_enum.py [-h] [-t THREADS] [-o TIMEOUT] -u URL [-v]

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        number of threads (15)
  -o TIMEOUT, --timeout TIMEOUT
                        timeout (5)
  -d DELAY, --delay DELAY
                        delay between requests (1)
  -u URL, --url URL     url (http://site.com)
  -v, --verbose         verbose

python3 drupal_user_enum.py -u https://site.com -t 15
Starting...
[ID] https://site.com/ru/users/admin
[ID] https://site.com/ru/users/berserk
[ID] https://site.com/ru/users/olya
[ID] https://site.com/ru/users/baxus
[ID] https://site.com/ru/users/tamilinak
[ID] https://site.com/ru/users/lemeshkoe
[ID] https://site.com/ru/users/petrenkog
[ID] https://site.com/ru/users/kosolapov


python3 drupal_user_enum.py -u https://site.com -t 2 -v 
Starting...
Trying id: 1
[ID] https://site.com/ru/users/admin
Trying id: 126
Trying id: 2
Trying id: 127
Trying id: 3
Trying id: 128
Trying id: 4
Trying id: 129
Trying id: 5
Trying id: 6
[ID] https://site.com/ru/users/kosolapov
```
