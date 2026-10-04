# Ota pyydetyt kirjastot käyttöön
from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

#nopeus
nopeus = 50000

#Aika liikkumiseen
eteenAika = 1.65
taakseAika = 1.65
vasenAika = 0.8
oikeaAika = 0.8

#Funktio ohjeet toiminnoille
def pysayta():
    e1.duty_u16(1)
    e2.duty_u16(1)
    sleep(1)

#Eteenpäin liikkuminen
def eteen():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(eteenAika)
    pysayta()

#taaksepäin liikkuminen tarvittaessa
def taakse():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(taakseAika)
    pysayta()

#Vasemmalle käännös
def vasen90():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(vasenAika)
    pysayta()

#Oikealle käännös
def oikea90():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(oikeaAika)
    pysayta()


# Odota ennen lähtöä
pysayta()
sleep(5)

# S-kirjaimen reitti peilikuvana, hyödyntäen tehtyjä funktioita

eteen()
vasen90()

eteen()
vasen90()

eteen()
oikea90()

eteen()
oikea90()

eteen()