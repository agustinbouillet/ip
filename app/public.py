import urllib.request


#https://www.ipify.org
#https://api.ipify.org
def public():
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')

