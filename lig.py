#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import kivy

kivy.require("1.9.1")

from kivy.app import App

from kivy.clock import Clock

from kivy.uix.gridlayout import GridLayout

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.image import AsyncImage

from kivy.uix.widget import Widget

from kivy.uix.scrollview import ScrollView

from kivy.lang import Builder

from kivy.properties import ObjectProperty, StringProperty




from puandurumu import PuanDurumu

Builder.load_file("takimsayfasi.kv")

logolar = {"GAZİANTEP B.Ş. BLD.SPOR":"logolar/gaziantep.jpg",
			"BOLUSPOR": "logolar/bolu.jpg",
			"MERSİN İDMANYURDU":"logolar/mersiniy.jpg",
			"ŞANLIURFASPOR":"logolar/sanliurfa.jpg",
			"BANDIRMASPOR":"logolar/bandirma.jpg",
			"ESKİŞEHİRSPOR":"logolar/eskisehir.jpg",
			"EVKUR YENİ MALATYASPOR":"logolar/evkurYeniMalatyaspor.jpg",
			"YENİ MALATYASPOR":"logolar/evkurYeniMalatyaspor.jpg",
			"ELAZIĞSPOR":"logolar/elazig.jpg",
			"SİVASSPOR":"logolar/sivas.jpg",
			"MANİSASPOR":"logolar/manisa.jpg",
			"DENİZLİSPOR":"logolar/denizli.jpg",
			"ALTINORDU A.Ş.":"logolar/altinordu.jpg",
			"ADANA DEMİRSPOR":"logolar/adanademir.jpg",
			"ÜMRANİYESPOR":"logolar/umraniye.jpg",
			"GÖZTEPE A.Ş.":"logolar/goztepe.jpg",
			"GİRESUNSPOR":"logolar/giresun.jpg",
			"SAMSUNSPOR":"logolar/samsun.jpg",
			"BALIKESİRSPOR":"logolar/balikesir.jpg"}

class EkranGecis(ScreenManager):
	pass
	
class UstBolum(BoxLayout):
	pass

class UstBolumGecis(BoxLayout):
	
	pass

		
		
class GirisEkrani(Screen):
	pass

class HaftaninMaclari(Screen):
	
	def __init__(self,**kwargs):
		
		
		super(HaftaninMaclari,self).__init__(**kwargs)
		
		self.ustbolum = UstBolum()
		
		
		self.scroll = ScrollView(pos_hint = {"x":0,"top":0.95})
		
		self.liste = BoxLayout()
		self.liste.padding = 25
		self.liste.size_hint = (1,None)
		self.liste.height = 2000
		self.liste.orientation = "vertical"
		
	
		
		
		
		for i in range(9):	
			
			self.dizilim = BoxLayout()
			self.dizilim.size_hint = (1,0.2)
			
			self.kutu_1 = BoxLayout()
			self.kutu_1.orientation = "vertical"
		
			self.kutu_2 = BoxLayout()
			self.kutu_2.orientation = "vertical"	
			
			self.kutu_1.add_widget(AsyncImage(source = logolar[puandurumu.haftaninmaclari[i]["takim_1"]]))
			
			self.kutu_1.add_widget(Label(text = puandurumu.haftaninmaclari[i]["takim_1"] ))
			
			self.dizilim.add_widget(self.kutu_1)
			
			self.dizilim.add_widget(Label(text = puandurumu.haftaninmaclari[i]["takim_1_skor"]))
			
			self.dizilim.add_widget(Label(text =  puandurumu.haftaninmaclari[i]["tarih"] + "\n" + puandurumu.haftaninmaclari[i]["saat"]))
			
			self.dizilim.add_widget(Label(text = puandurumu.haftaninmaclari[i]["takim_2_skor"]))
			
			self.kutu_2.add_widget(AsyncImage(source = logolar[puandurumu.haftaninmaclari[i]["takim_2"]]))
			
			self.kutu_2.add_widget(Label(text = puandurumu.haftaninmaclari[i]["takim_2"] ))
			
			self.dizilim.add_widget(self.kutu_2)
			
			self.liste.add_widget(self.dizilim)
			
		
		self.scroll.add_widget(self.liste)
		
		
		
		self.add_widget(self.scroll)
		
		self.add_widget(self.ustbolum)



class TakimSayfasi(Screen):
	
	baskan = ObjectProperty()
	logo = ObjectProperty()
	takim = ObjectProperty()
	kod = ObjectProperty()
	sehir = ObjectProperty()
	adres = ObjectProperty()
	icsaha_1 = ObjectProperty()
	icsaha_2 = ObjectProperty()
	dissaha_1 = ObjectProperty()
	dissaha_2 = ObjectProperty()
	kaleci_1 = ObjectProperty()
	kaleci_2 = ObjectProperty()
		
		
	def __init__(self,**kwargs):
		
		 
		
		super(TakimSayfasi,self).__init__(**kwargs)

		
		self.ust_bolum_gecis = UstBolumGecis()
		self.add_widget(self.ust_bolum_gecis)
		
		
	def girisBilgileri(self,td):
		
		self.bilgiler = puandurumu.takim_bilgileri(puandurumu.kluplinkleri[td.text])
		self.logo.source = logolar[td.text]
		self.takim.text = self.bilgiler["klup_isim"]
		self.kod.text = self.bilgiler["klup_kodu"]
		self.sehir.text = self.bilgiler["klup_sehir"]
		self.adres.text = self.bilgiler["klup_adres"]
		self.baskan.text = self.bilgiler["klup_baskan"]
		

		
		

class TakimSayfasiGecis(Screen):
	
	takimsayfasi = ObjectProperty()
	
	takimsayfasi = TakimSayfasi()
	
	def __init__(self,**kwargs):
		
		super(TakimSayfasiGecis,self).__init__(**kwargs)
		
		self.ekleme = True
		
		self.yerlesim = BoxLayout(orientation = "vertical")
		self.yerlesim.pos_hint = {"x":0,"top":0.95}
		self.yerlesim.size_hint = 1,0.95
		

		for i in sorted(puandurumu.kluplinkleri.keys()):
			
			self.button = Button()
			self.button.text = i
			self.button.bind(on_release = self.klupismiBelirle)
			self.yerlesim.add_widget(self.button)
		
		self.add_widget(self.yerlesim)
		self.add_widget(UstBolum())
		
		self.ust_bolum_gecis = UstBolumGecis()
		self.takimsayfasi.add_widget(self.ust_bolum_gecis)
		
	
	def klupismiBelirle(self,buton):
		
		self.bilgiler = puandurumu.takim_bilgileri(puandurumu.kluplinkleri[buton.text])
		self.takimsayfasi.logo.source = self.bilgiler["klup_logo"]
		self.takimsayfasi.takim.text = self.bilgiler["klup_isim"]
		self.takimsayfasi.kod.text = self.bilgiler["klup_kodu"]
		self.takimsayfasi.sehir.text = self.bilgiler["klup_sehir"]
		self.takimsayfasi.adres.text = self.bilgiler["klup_adres"]
		self.takimsayfasi.baskan.text = self.bilgiler["klup_baskan"]
		self.takimsayfasi.icsaha_1.source = self.bilgiler["icsaha_1"]
		self.takimsayfasi.icsaha_2.source = self.bilgiler["icsaha_2"]
		self.takimsayfasi.dissaha_1.source = self.bilgiler["dissaha_1"]
		self.takimsayfasi.dissaha_2.source = self.bilgiler["dissaha_2"]
		self.takimsayfasi.kaleci_1.source = self.bilgiler["kaleci_1"]
		self.takimsayfasi.kaleci_2.source = self.bilgiler["kaleci_2"]
		
		self.takimsayfasi.name = "takim_sayfasi_1"
		if self.ekleme == True:
			self.parent.add_widget(self.takimsayfasi)
			self.ekleme = False
		self.parent.transition = SlideTransition(direction = "left")
		self.parent.current = "takim_sayfasi_1"	
	
	
		
		
			
			
		

	

class PuanTablo(GridLayout):
	
	
	
	def __init__(self,**kwargs):
		
		super(PuanTablo,self).__init__(**kwargs)
		for i in puandurumu.takimlar:
			
			self.label1 = Label(text = (i["takim"]),size_hint = (10,1))
			self.add_widget(self.label1)
			self.label2 = Label(text = (i["oynanan"]),size_hint = (1,1))
			self.add_widget(self.label2)
			self.label3 = Label(text = (i["galibiyet"]),size_hint = (1,1))
			self.add_widget(self.label3)
			self.label4 = Label(text = (i["beraberlik"]),size_hint = (1,1))
			self.add_widget(self.label4)
			self.label5 = Label(text = (i["malubiyet"]),size_hint = (1,1))
			self.add_widget(self.label5)
			self.label6= Label(text = (i["atilan"]),size_hint = (1,1))
			self.add_widget(self.label6)
			self.label7= Label(text = (i["yenilen"]),size_hint = (1,1))
			self.add_widget(self.label7)
			self.label8 = Label(text = (i["avaraj"]),size_hint = (1,1))
			self.add_widget(self.label8)
			self.label9 = Label(text = (i["puan"]),size_hint = (1,1))
			self.add_widget(self.label9)
	
class PuanEkrani(Screen):
	
	
	def __init__(self,**kwargs):
		
		super(PuanEkrani,self).__init__(**kwargs)
		
		self.yerlesim = BoxLayout()
		self.ustbolum = UstBolum()
		
		self.puandurumu = PuanTablo()
		
		self.yerlesim.orientation = "vertical"
		
		
		self.yerlesim.add_widget(self.ustbolum)
		

		self.yerlesim.add_widget(self.puandurumu)
		
		self.add_widget(self.yerlesim)
		
		
		


class lig(App):
	
	def build(self):
		
		return EkranGecis()
		
if __name__ == "__main__":
	
	puandurumu = PuanDurumu()
	
	lig().run()
	
	
