
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

class PortaleDelDipendente(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint=(0.8, 0.9)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}
        Window.size = (360,640)
        self.window.add_widget(Image(source="logo.jpeg"))
        
         
        self.bottone = Button(text="Area Dipendenti", size_hint=(1,0.2),bold=True,background_color='#0099ff')
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press=self.portale)
        
        self.bottone1 = Button(text="Posta Elettronica", size_hint=(1,0.2),bold=True,background_color='#0099ff')
        self.window.add_widget(self.bottone1)
        self.bottone1.bind(on_press=self.posta)
        
        self.etichetta = Label(text='''                Asl Avellino
        Via degli Imbimbo, 10/12
           83100 Avellino (AV)''',font_size='20sp',color='#007dd1')
        self.window.add_widget(self.etichetta)
        
        return self.window
    
    def portale(self, instance):
        import webbrowser
        webbrowser.open("https://dipendenti.aslavellino.it/web/portaledeldipendente/home?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=false&_58_struts_action=%2Flogin%2Flogin")
        
    def  posta(self, instance):
        import webbrowser
        webbrowser.open("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=16&ct=1698332819&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fnlp%3d1%26state%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC9pbmJveC8%26RpsCsrfState%3d79b847a2-7e34-ba7e-aebe-aa939bafe93d&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
PortaleDelDipendente().run()
