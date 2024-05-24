import gettext 
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

raiz_dir = Path('.')

if getattr(sys, 'frozen', False):
    # Si se ejecuta como un ejecutable    
    raiz_dir = sys._MEIPASS 
  
locale_dir = Path(raiz_dir) / 'locale'      
env_path = Path(raiz_dir) / '.env'
load_dotenv(dotenv_path=env_path) 


lang = os.getenv('IDIOMA', 'es')

t = gettext.translation('programa', locale_dir, [lang], fallback=True)
_ = t.gettext

def custom_gettext(s):  
  current_dict = {
              'usage: ': _('Uso: '),
              'optional arguments': _('argumentos opcionales'),
              'options': _('opciones'),
              'show this help message and exit': _('muestra este mensaje de ayuda y sale'),
              'positional arguments': _('argumentos posicionales'),
              'the following arguments are required: %s': _('los siguientes argumentos son requeridos: %s'),
              'show program''s version number and exit': _('muestra la versión del programa y sale'),
              'expected one argument': _('se espera un valor para el parámetro'),
              'expected at least one argument': _('se espera al menos un valor para el parámetro')
  }
 
  if s in current_dict:
      return current_dict[s]
  return s
gettext.gettext = custom_gettext
