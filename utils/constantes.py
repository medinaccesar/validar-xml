import os


class Configuracion:

    __slots__ = ()

    NOMBRE_AP = 'validar-xml'
    DESCRIPCION_APP = 'Permite validar un fichero xml a partir de un esquema sxd'
    VERSION = '1.0.0'
    AUTOR = 'César Medina'
    ANNO = '2024'
    CREDITOS = AUTOR + ' - ' + ANNO 
      
    # Directorios
    DIR_DOCUMENTOS = os.path.expanduser("~")
    DIR_ABS = os.path.dirname(os.path.abspath(__file__))+os.path.sep   
   
