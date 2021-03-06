# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.config import Config
import time
Config.set('graphics', 'widht', '800')
Config.set('graphics', 'height', '480')

Config.set('kivy', 'keyboard_mode', 'systemanddock')
Config.set('kivy', 'keyboard_layout', 'numeric')


from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
import os
import RPi.GPIO as GPIO
speed = 1.0
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







#Window.size = (800, 480)

Window.clearcolor = (0, 0, 0, 1)

class Uygulama(App):
    def tusaBasildi(self, *args):

        kb = Window.request_keyboard(self,self.isinaditext.text,self)

        if kb.widget:
            # If the current configuration supports Virtual Keyboards, this
            # widget will be a kivy.uix.vkeyboard.VKeyboard instance.
            self._keyboard = kb.widget
            self._keyboard.layout = layout
        else:
            self._keyboard = kb


    def sinyalGeldi(self, *args):

        self.yapilan.text = str(int(self.yapilan.text)+1)
        self.cycleSuresi=time.time()-self.oncekiVurus
        self.oncekiVurus=time.time()
        self.cevrimsuresi.text="%.2f" %self.cycleSuresi+" sn"



    def build(self, *args):
        self.title = u"Otomat Sayacı"
        Ekran = BoxLayout(orientation = 'vertical')
        self.oncekiVurus=time.time()
        self.cycleSuresi=0.0




        sira1 = BoxLayout()
        sira2 = BoxLayout()
        sira3 = BoxLayout()
        sira4 = BoxLayout()
#satır1
        self.durum = Label(text= "Makine\nDurumu" , font_size=20)
        self.durumbuton = Button(text = "Çalışıyor", background_color = (0, 1, 0, 1))
        #renk kodu 0101 yeşil 1001 kırmızıdır.
#satır2
        self.yapilantext = Label(text= u"Yapılan İş", font_size=20)
        self.yapilan = TextInput(text = u"0", font_size=20)
#satır3
        self.cevrimsuresitext = Label(text= u"Çevrim Süresi", font_size=20)
        self.cevrimsuresi = Button(text = u"0.0 sn")
#satır4
        self.isinaditext = Label(text= u"İşin Adı", font_size=20)
        self.isinadi = TextInput(text = "")
        self.isinadi.bind(on_press=self.tusaBasildi)

        sira1.add_widget(self.durum)
        sira1.add_widget(self.durumbuton)
        sira2.add_widget(self.yapilantext)
        sira2.add_widget(self.yapilan)
        sira3.add_widget(self.cevrimsuresitext)
        sira3.add_widget(self.cevrimsuresi)
        sira4.add_widget(self.isinaditext)
        sira4.add_widget(self.isinadi)

        Ekran.add_widget(sira1)
        Ekran.add_widget(sira2)
        Ekran.add_widget(sira3)
        Ekran.add_widget(sira4)

        GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=self.sinyalGeldi, bouncetime=50)

        return Ekran



Uygulama().run()