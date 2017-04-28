import requests
from bs4 import BeautifulSoup
import re

class PuanDurumu():
	
	def __init__(self):
		
		super().__init__()
		
		self.url =  "http://www.tff.org/default.aspx?pageID=142"
		
		self.site_html = requests.get(self.url).text
		
		# puan durumuna ulasmak icin gerekli html id'leri
		
		self.o = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_lblOyun"
		self.g = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_Label4"
		self.b = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_lblKazanma"
		self.m = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_lblPuan"
		self.a = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_Label1"
		self.y = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_Label2"
		self.av = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_Label5"
		self.p = "ctl00_MPane_m_142_6657_ctnr_m_142_6657_grvACetvel_ctl{}_Label3"
		
		#haftanin maclarina ve tarih , saat bilgisine ulasmak icin gerekli html id'leri
		
		self.tarih = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_lblTarih"
		self.saat = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_lblSaat"
		self.takim_1 = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_Label4"
		self.takim_2 = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_Label1"
		self.takim_1_skor = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_Label5"
		self.takim_2_skor = "ctl00_MPane_m_142_6656_ctnr_m_142_6656_dtlHaftaninMaclari_ctl{}_Label6"
		
		self.takimlar = []
		self.haftaninmaclari = []
		self.kluplinkleri = {}
		
		soup = BeautifulSoup(self.site_html,"html.parser")
		
		self.siralama(soup,"ctl00_MPane_m_142_6657_ctnr_m_142_6657_Panel1")
		
		self.bu_hafta_maclari(soup)
		
		#self.takim_bilgileri()
	
	def siralama(self,soup,ids):
		
		self.artiran_puandurumu = 1
		
		self.siralama=soup.find_all(id = ids)
		
		for i in self.siralama[0].find_all("a"):
			
			self.kluplinkleri[re.split("[0-9]+\.",i.text)[1]] = "http://www.tff.org/" + i["href"]
			
			if self.artiran_puandurumu < 10:
				
				
				self.takimlar.append({"takim":i.text, 
										"oynanan":soup.find(id = self.o.format("0" + str(self.artiran_puandurumu))).text,
										"galibiyet":soup.find(id = self.g.format("0" + str(self.artiran_puandurumu))).text,
										"beraberlik":soup.find(id = self.b.format("0" + str(self.artiran_puandurumu))).text,
										"malubiyet":soup.find(id = self.m.format("0" + str(self.artiran_puandurumu))).text,
										"atilan":soup.find(id = self.a.format("0" + str(self.artiran_puandurumu))).text,
										"yenilen":soup.find(id = self.y.format("0" + str(self.artiran_puandurumu))).text,
										"avaraj":soup.find(id = self.av.format("0" + str(self.artiran_puandurumu))).text,
										"puan":soup.find(id = self.p.format("0" + str(self.artiran_puandurumu))).text})
						
						
						
						
				self.artiran_puandurumu += 1
						
						
			else:
				self.takimlar.append({"takim":i.text, 
										"oynanan":soup.find(id = self.o.format(str(self.artiran_puandurumu))).text,
										"galibiyet":soup.find(id = self.g.format(str(self.artiran_puandurumu))).text,
										"beraberlik":soup.find(id = self.b.format(str(self.artiran_puandurumu))).text,
										"malubiyet":soup.find(id = self.m.format(str(self.artiran_puandurumu))).text,
										"atilan":soup.find(id = self.a.format(str(self.artiran_puandurumu))).text,
										"yenilen":soup.find(id = self.y.format(str(self.artiran_puandurumu))).text,
										"avaraj":soup.find(id = self.av.format(str(self.artiran_puandurumu))).text,
										"puan":soup.find(id = self.p.format(str(self.artiran_puandurumu))).text})
						
				self.artiran_puandurumu += 1
		
		
		
		
	def bu_hafta_maclari(self,soup):
		
		self.artiran_haftaninmaclari = 1
		
		while self.artiran_haftaninmaclari < 10:
			
					
			self.haftaninmaclari.append({"takim_1":soup.find(id = self.takim_1.format("0" + str(self.artiran_haftaninmaclari))).text,
										"takim_1_skor":soup.find(id = self.takim_1_skor.format("0" + str(self.artiran_haftaninmaclari))).text, 
										"takim_2":soup.find(id = self.takim_2.format("0" + str(self.artiran_haftaninmaclari))).text,
										"takim_2_skor":soup.find(id = self.takim_2_skor.format("0" + str(self.artiran_haftaninmaclari))).text, 
										"tarih":soup.find(id = self.tarih.format("0" + str(self.artiran_haftaninmaclari))).text,
										"saat":soup.find(id = self.saat.format("0" + str(self.artiran_haftaninmaclari))).text})
						
						
						
			self.artiran_haftaninmaclari += 1
	
	def takim_bilgileri(self,link):
		
		self.takim = requests.get(link).text
		
		self.soup = BeautifulSoup(self.takim,"html.parser")
		
		
		self.bilgiler = {"klup_logo" : self.soup.find(id = "ctl00_MPane_m_395_190_ctnr_m_395_190_dtKulupBilgisi_ad")["src"],
		
						"klup_isim" : self.soup.find(id = "ctl00_Head").text,
		
						"klup_kodu" : self.soup.find(id = "ctl00_MPane_m_395_190_ctnr_m_395_190_dtKulupBilgisi_Label6").text,
		
						"klup_adres" : self.soup.find(id = "ctl00_MPane_m_395_190_ctnr_m_395_190_dtKulupBilgisi_Label2").text,
		
						"klup_sehir" : self.soup.find(id = "ctl00_MPane_m_395_190_ctnr_m_395_190_dtKulupBilgisi_Label3").text,
		
						"klup_baskan" : self.soup.find(id = "ctl00_MPane_m_395_190_ctnr_m_395_190_dtKulupBilgisi_Label7").text,
						
						"icsaha_1": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgIcSaha1")["src"],
						
						"icsaha_2": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgIcSaha2")["src"],
						
						"dissaha_1": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgDisSaha1")["src"],
						
						"dissaha_2": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgDisSaha2")["src"],
						
						"kaleci_1": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgKaleci1")["src"],
						
						"kaleci_2": self.soup.find(id = "ctl00_MPane_m_395_7188_ctnr_m_395_7188_imgKaleci2")["src"]}
		
		
		return self.bilgiler
		
		
				
		
		
		
		

if __name__ == "__main__":
	
	puan = PuanDurumu()
	
