import gettext
import locale
import sys
import os
from dotenv import load_dotenv
from pathlib import Path

raiz_dir = Path('.')
if getattr(sys, 'frozen', False):
    # Si se ejecuta como un ejecutable    
    raiz_dir = sys._MEIPASS  

locale_dir = Path(raiz_dir) / 'locale'  
env_path = Path(raiz_dir) / '.env'
load_dotenv(dotenv_path=env_path) 

lang =  os.getenv('IDIOMA')

if lang is None:
    # Configura el idioma de la aplicación según la configuración del sistema
    locale.setlocale(locale.LC_ALL, '')
    lang, encoding = locale.getlocale() 
       
# Carga los archivos de traducción para el idioma configurado
t = gettext.translation('programa', locale_dir, [lang], fallback=True)
_ = t.gettext

def p(cadena):
    print(_(cadena))