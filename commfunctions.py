from mysocket import Mysocket
from klant import Klant

#SERVER='192.168.1.1'
#SERVER='127.0.0.1'
SERVER='192.168.0.22'
PORT=7893

def getKlantenList():
    klantenlist=[]
    #create the socket
    sock = Mysocket()
    sock.connect(SERVER,PORT)
    sock.mysend('b')
    sock.mysend(';')
    # read the response
    bit=''
    while(bit!=';'):
        bit = sock.myreceive(1)
    nrklanten=''
    bit=sock.myreceive(1)
    while(bit!=';'):
        nrklanten=nrklanten+bit
        bit = sock.myreceive(1)
    nrklanten=eval(nrklanten) # convert to number

    # read the klanten
    for i in range(0,nrklanten):
        current=Klant()
        bit = sock.myreceive(1)
        while (bit!='|'):
            current.nr=current.nr+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.klant=current.klant+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.adres=current.adres+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.gemeente=current.gemeente+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.u1=current.u1+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.telefoon=current.telefoon+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.gsm=current.gsm+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.rekeningnr=current.rekeningnr+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.u2=current.u2+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!='|'):
            current.u3=current.u3+bit
            bit=sock.myreceive(1)
        bit=sock.myreceive(1)
        while (bit!=';'):
            current.u4=current.u4+bit
            bit=sock.myreceive(1)
      
        klantenlist.append(current)  
        # eat the \r \n
        bit=sock.myreceive(2)
    return klantenlist


def upload(klant):
     #create the socket
    sock = Mysocket()
    sock.connect(SERVER,PORT)
    sock.mysend('u')
    sock.mysend(';')
    msg=''
    msg=msg+klant.nr+"|"+klant.klant+"|"+klant.adres+"|"+klant.gemeente+"|"+klant.u1+"|"+klant.telefoon+"|"+klant.gsm+"|"+klant.rekeningnr+"|"+klant.u2+"|"+klant.u3+"|"+klant.u4+";"
    print 'sending '+ msg
    sock.mysend(msg)
    # read the response
    bit=''
    while(bit!=';'):
        bit = sock.myreceive(1)
    answer=''
    bit=sock.myreceive(1)
    while(bit!=';'):
        answer=answer+bit
        bit = sock.myreceive(1)
    answer=eval(answer)
    return answer    

def insert(klant):
     #create the socket
    sock = Mysocket()
    sock.connect(SERVER,PORT)
    sock.mysend('z')
    sock.mysend(';')
    msg=''
    msg=msg+klant.nr+"|"+klant.klant+"|"+klant.adres+"|"+klant.gemeente+"|"+klant.u1+"|"+klant.telefoon+"|"+klant.gsm+"|"+klant.rekeningnr+"|"+klant.u2+"|"+klant.u3+"|"+klant.u4+";"
    print 'sending '+ msg
    sock.mysend(msg)
    # read the response
    bit=''
    while(bit!=';'):
        bit = sock.myreceive(1)
    answer=''
    bit=sock.myreceive(1)
    while(bit!=';'):
        answer=answer+bit
        bit = sock.myreceive(1)
    answer=eval(answer)
    return answer    
