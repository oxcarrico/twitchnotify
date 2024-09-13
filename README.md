
# Twitch Live Stream Monitor

Este proyecto te permite monitorear si un streamer en Twitch está en vivo y abrir automáticamente el stream en el navegador cuando lo esté. Utiliza Selenium y ChromeDriver para verificar el estado de la transmisión.

## Características

- Monitorea automáticamente si un streamer está en vivo en Twitch.
- Abre el stream en el navegador cuando el streamer esté en vivo.
- Personalizable con el nombre del streamer que deseas monitorear.
- Configuración del tamaño de la ventana del navegador a través de Selenium.

## Requisitos

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Google Chrome

## Instalación

1. Clona este repositorio o descarga el código.
   ```bash
   git clone https://github.com/tuusuario/twitchnotify.git
   ```

2. Instala las dependencias de Python.
   ```bash
   pip install selenium
   ```

3. Descarga ChromeDriver y asegúrate de que esté en tu PATH o especifica su ubicación en el script.

4. Configura el nombre del streamer en el archivo del script.

## Uso

1. Edita el script y cambia el valor de `streamer` por el nombre del streamer que deseas monitorear.

   ```python
   streamer = 'nombreDelStreamer'
   ```

2. Ejecuta el script.
   ```bash
   python twitchnotify.py
   ```

3. El script verificará cada 60 segundos si el streamer está en vivo. Si lo está, abrirá el stream en el navegador.

## Personalización

- **Tamaño de la ventana:** El tamaño predeterminado de la ventana del navegador es `1200x800`. Puedes modificar esto en el script cambiando la línea:
  ```python
  chrome_options.add_argument("--window-size=1200,800")
  ```

- **Tiempo de espera:** El script verifica cada minuto si el streamer está en vivo. Puedes ajustar este intervalo cambiando el valor de `time.sleep(60)`.
