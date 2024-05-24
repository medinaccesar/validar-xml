import xmlschema
from xmltoxsd import XSDGenerator
import os
from utils.constantes import Configuracion as conf

class XmlService():
           
    # Calcula el hash del archivo
    def validar(self, fichero, esquema):
        
        validar =  False
        xsd = xmlschema.XMLSchema(esquema)

        if xsd.is_valid(fichero):
            validar = True

        return validar

    def crear_xsd(self, fichero):
        
        generator = XSDGenerator()
        esquema_xsd = generator.generate_xsd(fichero, min_occurs="0")
        return esquema_xsd
    
  