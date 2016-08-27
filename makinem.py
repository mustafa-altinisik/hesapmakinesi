# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os
from kivy.config import Config
Config.set('graphics', 'widht', '600')
Config.set('graphics', 'height', '600')
#pencere boyutlarnı ayarladık.


import RPi.GPIO as GPIO

#for now, use a global for blink speed (better implementation TBD):
speed = 1.0

# Set up GPIO:
beepPin = 17
ledPin = 27
buttonPin = 22
flashLedPin = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(beepPin, GPIO.OUT)
GPIO.output(beepPin, GPIO.LOW)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)
GPIO.setup(flashLedPin, GPIO.OUT)
GPIO.output(flashLedPin, GPIO.LOW)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class Deneme(App):

    def tusaBasildi(self, *args):
        self.title = u"Hesap Makinesi"



    def tusaBasildi1(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "1"
        else:
            self.cikti.text = self.cikti.text + "1"
        self.sontus="sayi"




    def tusaBasildi2(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "2"
        else:
            self.cikti.text = self.cikti.text + "2"
        self.sontus="sayi"

    def tusaBasildi3(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "3"
        else:
            self.cikti.text = self.cikti.text + "3"
        self.sontus="sayi"

    def tusaBasildiyildiz(self, *args):
        if (self.sontus != "islem"):

            if (self.islem == "*"):
                self.deger = self.deger * int(self.cikti.text)
                self.cikti.text = self.deger

            self.deger = int(self.cikti.text)
            self.islem = "*"
            self.cikti.text = ""

        if (self.sontus == "islem"):
            self.islem = "*"

        self.sontus = "islem"

    def tusaBasildice(self, *args):
        self.deger = 0
        self.cikti.text = ""
        self.sontus = ""

    def tusaBasildi4(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "4"
        else:
            self.cikti.text = self.cikti.text + "4"
        self.sontus="sayi"

    def tusaBasildi5(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "5"
        else:
            self.cikti.text = self.cikti.text + "5"
        self.sontus="sayi"


    def tusaBasildi6(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "6"
        else:
            self.cikti.text = self.cikti.text + "6"
        self.sontus="sayi"

    def tusaBasildibolu(self, *args):
        if (self.sontus != "islem"):

            if (self.islem == "/"):
                self.deger = self.deger / int(self.cikti.text)
                self.cikti.text = self.deger

            self.deger = int(self.cikti.text)
            self.islem = "/"
            self.cikti.text = ""

        if (self.sontus == "islem"):
            self.islem = "/"

        self.sontus = "islem"

    def tusaBasildioff(self, *args):
        self.stop()


    def tusaBasildi7(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "7"
        else:
            self.cikti.text = self.cikti.text + "7"
        self.sontus="sayi"

    def tusaBasildi8(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "8"
        else:
            self.cikti.text = self.cikti.text + "8"
        self.sontus="sayi"

    def tusaBasildi9(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "9"
        else:
            self.cikti.text = self.cikti.text + "9"
        self.sontus="sayi"

    def tusaBasildieksi(self, *args):
        if (self.sontus != "islem"):
            self.deger = self.deger - int(self.cikti.text)
            self.cikti.text = str(self.deger)

        if (self.sontus == "islem"):
            self.islem = "-"

        self.sontus = "islem"


    def tusaBasildiesittir(self, *args):
        if (self.sontus != "islem"):
                if (self.islem=="+"):
                    self.deger = self.deger + int(self.cikti.text)
                elif (self.islem == "-"):
                    self.deger = self.deger - int(self.cikti.text)
                elif (self.islem == "/"):
                    self.deger = self.deger / int(self.cikti.text)
                elif (self.islem == "*"):
                    self.deger = self.deger * int(self.cikti.text)

                self.cikti.text = str(self.deger)

        if (self.sontus == "islem"):
            self.islem = ""
        self.sontus = "islem"

    def tusaBasildi00(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "0"
        else:
            self.cikti.text = self.cikti.text + "00"
        self.sontus="sayi"


    def tusaBasildi0(self, *args):
        if (self.sontus=="islem"):
            self.cikti.text = "0"
        else:
            self.cikti.text = self.cikti.text + "0"
        self.sontus="sayi"


    def tusaBasildinokta(self, *args):
        self.cikti.text = self.cikti.text + "."

    def tusaBasildiarti(self, *args):
        if(self.sontus!="islem"):

            self.deger = self.deger + int(self.cikti.text)
            self.cikti.text = str(self.deger)

        if(self.sontus=="islem"):
            self.islem = "+"

        self.sontus = "islem"





    def build(self):
        self.sontus=""
        self.deger = 0
        self.islem = "+"
        self.title = u"Hesap Makinesi"
        #pencerenin başlığını ayarladık
        Ekran = BoxLayout(orientation = 'vertical')
        #Ekran adında boxlayout oluşturduk.
        gosterge = BoxLayout()
        #Ekran adında boxlayout oluşturduk.
        sira1 = BoxLayout()
        #Sira1 adında boxlayout oluşturduk.
        sira2 = BoxLayout()
        #Sira2 adında boxlayout oluşturduk.
        sira3 = BoxLayout()
        #Sira3 adında boxlayout oluşturduk.
        sira4 = BoxLayout()
        #Sira4 adında boxlayout oluşturduk.


        #Gösterge satırına geçici olarak etiket yazdırdık.
        self.cikti = Label(text= "" , font_size=50)
        self.cikti.color=(1,1,0,1)

#        print self.cikti.text
#        a = self.cikti.text
#        sayi = int(a)



        #İlk satırın düğmelerini oluşturduk.
        self.dugme1 = Button(text = "1")
        self.dugme1.bind(on_press=self.tusaBasildi1)
        dugme2 = Button(text= "2")
        dugme2.bind(on_press=self.tusaBasildi2)
        dugme3 = Button(text= "3")
        dugme3.bind(on_press=self.tusaBasildi3)
        dugmeYILDIZ = Button(text="*", font_size=30)
        dugmeYILDIZ.color=(1,0,0,1)
        dugmeYILDIZ.bind(on_press=self.tusaBasildiyildiz)
        #düğmenin rengini değiştirdik.
        dugmeCE = Button(text=u"CE", font_size=30)
        dugmeCE.bind(on_press=self.tusaBasildice)

        #İkinci satırın düğmelerini oluşturduk.
        dugme4 = Button(text= "4")
        dugme4.bind(on_press=self.tusaBasildi4)
        dugme5 = Button(text="5")
        dugme5.bind(on_press=self.tusaBasildi5)
        dugme6 = Button(text="6")
        dugme6.bind(on_press=self.tusaBasildi6)
        dugmeBOLU = Button(text="/", font_size=30)
        dugmeBOLU.color=(1,0,0,1)
        #düğmenin rengini değiştirdik.
        dugmeBOLU.bind(on_press=self.tusaBasildibolu)
        dugmeOFF = Button(text="OFF", font_size=30)
        dugmeOFF.bind(on_press=self.tusaBasildioff)


        #Üçüncü satırın düğmelerini oluşturduk.
        dugme7 = Button(text="7")
        dugme7.bind(on_press=self.tusaBasildi7)
        dugme8 = Button(text="8")
        dugme8.bind(on_press=self.tusaBasildi8)
        dugme9 = Button(text="9")
        dugme9.bind(on_press=self.tusaBasildi9)
        dugmeEKSI = Button(text="-", font_size=30)
        dugmeEKSI.color=(1,0,0,1)
        #düğmenin rengini değiştirdik.
        dugmeEKSI.bind(on_press=self.tusaBasildieksi)
        dugmeESITTIR = Button(text="=", font_size=50)
        dugmeESITTIR.bind(on_press=self.tusaBasildiesittir)


        #Dördüncü satırın düğmelerini oluşturduk.
        dugme00 = Button(text="00")
        dugme00.bind(on_press=self.tusaBasildi00)
        dugme0 = Button(text="0")
        dugme0.bind(on_press=self.tusaBasildi0)
        dugmeNOKTA = Button(text=".", font_size=30)
        dugmeNOKTA.bind(on_press=self.tusaBasildinokta)
        dugmeARTI = Button(text="+", font_size=30)
        dugmeARTI.color=(1,0,0,1)
        #düğmenin rengini değiştirdik.
        dugmeARTI.bind(on_press=self.tusaBasildiarti)
        bosluk = Label(text="Hesap\nMakinesi\n2016")
        #Son satırın sonundaki boşluğu geçici süre için doldurduk.







        gosterge.add_widget(self.cikti)
        #Çıktı bölümüne etiket ile yazı yazdık.

        sira1.add_widget(self.dugme1)
        sira1.add_widget(dugme2)
        sira1.add_widget(dugme3)
        sira1.add_widget(dugmeYILDIZ)
        sira1.add_widget(dugmeCE)
        #İlk satırın öğelerini derledik.

        sira2.add_widget(dugme4)
        sira2.add_widget(dugme5)
        sira2.add_widget(dugme6)
        sira2.add_widget(dugmeBOLU)
        sira2.add_widget(dugmeOFF)
        #İkinci satırın öğelerini derledik.

        sira3.add_widget(dugme7)
        sira3.add_widget(dugme8)
        sira3.add_widget(dugme9)
        sira3.add_widget(dugmeEKSI)
        sira3.add_widget(dugmeESITTIR)
        #Üçüncü satırın öğelerini derledik.

        sira4.add_widget(dugme00)
        sira4.add_widget(dugme0)
        sira4.add_widget(dugmeNOKTA)
        sira4.add_widget(dugmeARTI)
        sira4.add_widget(bosluk)
        #Dördüncü satırın öğelerini derledik.


        Ekran.add_widget(gosterge)
        Ekran.add_widget(sira1)
        Ekran.add_widget(sira2)
        Ekran.add_widget(sira3)
        Ekran.add_widget(sira4)

        GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=self.tusaBasildi1, bouncetime=200)

        return Ekran


app=Deneme()
app.run()
