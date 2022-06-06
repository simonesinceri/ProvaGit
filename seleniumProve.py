from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# if preventivo su giorno attuale così posso fare prenotazione dei due succesivi

matricola = "0300392"
psw = "mraC69?!"
urlEntered = "https://delphi.uniroma2.it/totem/jsp/Iscrizioni/sStudentiRegolariLogin.jsp"
#metto xpath delle aule 
aulaB12 = ""
aulaB13 = ""
aulaTDG = ""

driver = webdriver.Chrome('/Users/simon/OneDrive/Desktop/prg/chromedriver')
driver.get("https://delphi.uniroma2.it/totem/jsp/homeStudenti.jsp")

accedi = driver.find_element_by_xpath('//*[@id="areapersonale"]/tbody/tr[2]/td/a')
accedi.click()

matricForm = driver.find_element_by_xpath('//*[@id="tre"]/input')
matricForm.send_keys(matricola)
tokenForm = driver.find_element_by_xpath('//*[@id="due"]/input')
tokenForm.send_keys(psw)
accediBtn = driver.find_element_by_xpath('//*[@id="quattro"]/p/input[1]')
accediBtn.click()

currentUrl = driver.current_url

if(currentUrl !=urlEntered):
    #do something
    # eventuale accettazione dichiarazione covid
    pippo = "pippo"

aulePrenotBtn = driver.find_element_by_xpath('//*[@id="adempi"]/tbody/tr[7]/td[2]/span[1]/a')
aulePrenotBtn.click()
#selectDay = driver.find_elements_by_xpath('//*[@id="corpoPrincipale_contenuti_contenuto_corpo_001"]/form/table[1]/tbody/tr/td/select')

date1 = driver.find_element_by_xpath('//*[@id="corpoPrincipale_contenuti_contenuto_corpo_001"]/form/table[1]/tbody/tr/td/select/option[1]').click()

avantitBtn = driver.find_element_by_xpath('//*[@id="corpoPrincipale_contenuti_contenuto_corpo_001"]/form/table[2]/tbody/tr[2]/td/input[2]')
avantitBtn.click()

#aula1 = driver.find_element_by_xpath(aulaB12)

# manca selezione orario
# click tasto prenota
#click tasto indietro
# ripeti procedura per eventuale seconda lezione

#ripeti procedura per secondo giorno
#date2 = driver.find_element_by_xpath('//*[@id="corpoPrincipale_contenuti_contenuto_corpo_001"]/form/table[1]/tbody/tr/td/select/option[2]').click()

driver.close()