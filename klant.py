
class Klant:
    nr=''
    klant=''
    adres=''
    gemeente=''
    u1=''
    telefoon=''
    gsm=''
    rekeningnr=''
    u2=''
    u3=''
    u4=''
    
    def rectify(self):
        self.nr=self.toString(self.nr)
        self.klant=self.toString(self.klant)
        self.adres=self.toString(self.adres)
        self.gemeente=self.toString(self.gemeente)
        self.u1=self.toString(self.u1)
        self.telefoon=self.toString(self.telefoon)
        self.gsm=self.toString(self.gsm)
        self.rekeningnr=self.toString(self.rekeningnr)
        self.u2=self.toString(self.u2)
        self.u3=self.toString(self.u3)
        self.u4=self.toString(self.u4)
        
    def toString(self,s):
        return filter(lambda c: c not in "\x00", s)
