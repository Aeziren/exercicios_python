import urllib.request

try:
    pudim = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[31mPudim não está acessível!')
else:
    print('\033[32mO site pudim está online!!')


