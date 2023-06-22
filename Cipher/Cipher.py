from cryptography.fernet import Fernet


#funzione che genera la chiave
def gen_key():
    key = Fernet.generate_key()
    #salvare la key nel file
    with open('secret.key', 'wb') as kfile: 
        kfile.write(key)

#funzione che legge la chiave
def read_key():
    return open('secret.key', 'rb').read()

#funzione principale che va a crittografare il messaggio 
def c_mes(messaggio):
         key = read_key()
         m_encoded = messaggio.encode()
         #instanziamo la classe Fernet
         f=Fernet(key)
         encrypted_message = f.encrypt(m_encoded)
         print(encrypted_message)

 #decripttare
def  dec_mes(mes):
    key = read_key()
    f = Fernet(key)
    dec_mes = f.decrypt(mes)  
    print(dec_mes.decode())    

#utilizzare sempre la medesima chiave e non crearne un aper ogno messaggio 
with open('secret.key') as f:
     if f.read() == '':
      gen_key()

#Richiamiamo al funzione principale
c_mes("Questo è il mio primo cifrario, è funziona")
dec_mes(b'gAAAAABklFZ4FcfQmRtpcJi5CbvknVgC24QxjWsahj7f_0AVsWTxlR2mtMjq89ogaNze1g4RzMmFbDUaRqXWe8uHac600S2xV7eMpM-oFBvnbTA62LeyOF1DbP4hcmaX_0PdvtMVWYLd')
