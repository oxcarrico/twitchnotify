from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import webbrowser

# Configuración de Selenium
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Puedes comentar esta línea si quieres ver el navegador en acción
chrome_options.add_argument("--window-size=1200,800")  # Establece el tamaño de la ventana
webdriver_path = 'D:/Deberes/General/proyectos.py/chromedriver.exe'  # Ruta a chromedriver

# El nombre del streamer que quieres monitorear
streamer = 'cockxcar'
url = f'https://www.twitch.tv/{streamer}'

def is_stream_live(streamer_url):
    try:
        # Iniciar el navegador con Selenium
        service = Service(executable_path=webdriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(streamer_url)
        
        # Esperar a que el contenido se cargue
        time.sleep(5)
        
        # Buscar los elementos que indican que el streamer está en vivo
        try:
            live_element = driver.find_element(By.ID, 'live-channel-stream-information')
            is_live = live_element.is_displayed()
        except:
            is_live = False
        
        driver.quit()
        return is_live
    except Exception as e:
        print(f"Error al verificar el estado del stream: {e}")
        driver.quit()
        return False

while True:
    if is_stream_live(url):
        print(f"{streamer} está en vivo. Abriendo el stream en el navegador...")
        webbrowser.open(url)
        time.sleep(60)  # Espera un minuto antes de verificar nuevamente
    else:
        print(f"{streamer} no está en vivo. Reintentando en 60 segundos...")
    time.sleep(60)  # Espera un minuto antes de la siguiente verificación
