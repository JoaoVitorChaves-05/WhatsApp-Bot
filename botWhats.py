from selenium import webdriver
import time

class WhatsappBot:
    #FUNÇÃO Nº 1
    def __init__(self):
        self.mensagem = input("Digite a sua mensagem: ")
        self.grupos = input("Insira o(s) contato(s) ou grupo(s): ").split(",")
        self.typeTimer = input("Qual é a frequência de mensagens? [Dias, Horas, Minutos, Segundos]: ")

        if self.typeTimer == "Dias":
            self.timeInput = float(input("Qual intervalo em dias?: "))

        elif self.typeTimer == "Horas":
            self.timeInput = float(input("Qual intervalo em horas?: "))

        elif self.typeTimer == "Minutos":
            self.timeInput = float(input("Qual intervalo em minutos?: "))

        elif self.typeTimer == "Segundos":
            self.timeInput = float(input("Qual intervalo em segundos?: "))

        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

        self.OpenChrome()
        print(self.grupos)

    # FUNÇÃO Nº 2
    def OpenChrome(self):
        print("OpenChrome() is running...")
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        self.EnviarMensagens()

    # FUNÇÃO Nº 3
    def EnviarMensagens(self):
        # <span dir="auto" title="GRUPO DA FAMÍLIA" class="_3ko75 _5h6Y_ _3Whw5">GRUPO DA FAMÍLIA</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        print("EnviarMensagens() is running...")

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            time.sleep(1)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
        self.CountTime(self.typeTimer)

    # FUNÇÃO Nº 4
    def CountTime(self, timer):
        print("CountTime() is running...")
        if self.typeTimer == "Dias":
            time.sleep(self.timeInput*24*60*60)
            self.EnviarMensagens()
        elif self.typeTimer == "Horas":
            time.sleep(self.timeInput*60*60)
            self.EnviarMensagens()
        elif self.typeTimer == "Minutos":
            time.sleep(self.timeInput*60)
            self.EnviarMensagens()
        elif self.typeTimer == "Segundos":
            time.sleep(self.timeInput)
            self.EnviarMensagens()

bot = WhatsappBot()