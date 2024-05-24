
from service.fichero_service import Fichero
from utils.espannol_string_argparse import *
import argparse
from utils.locale_manager import _
from utils.constantes import Configuracion as conf
from service.xml_service import XmlService


class ValidarXml():

    def __init__(self):               
   
        self._xml_service = XmlService()       
        self._fichero_service = Fichero()       
           
        parser = self._get_parser()       
        self._procesar_argumentos(parser)   

    # Se ejecuta en modo consola
    def _ejecutar_modo_consola(self, args):   

        if args.validar is not None:
            esquema_sxd, archivo = args.validar
            self._validar(esquema_sxd, archivo)   
      
        elif args.crear is not None:
                       
            self._crear_xsd(args.crear)     
            
        elif args.acerca is not None:          
           
            self._acerca_de() 
                           
        else:
            print(_('No se ha especificado ninguna opción'))
    
    
    def _validar(self, archivo, esquema ):                
             
        self._comprobar_fichero_existe(esquema)
        self._comprobar_fichero_existe(archivo)
        
        if self._xml_service.validar( archivo, esquema):
            print(_('El documento es válido'))
        else:        
            print(_('El documento XML no es válido.'))
       
        
    def _crear_xsd(self, nombre_archivo):       
                
        self._comprobar_fichero_existe(nombre_archivo)   

        esquema = self._xml_service.crear_xsd(nombre_archivo)
        nombre = self._fichero_service.annadir_marca_temporal(nombre_archivo,'.sxd')
        self._fichero_service.escribir_archivo(nombre, esquema)        
        print(_('Se ha creado el esquema:'),nombre,'\n')        
    
        
    def _comprobar_fichero_existe(self, nombre_archivo):
        
        if not self._fichero_service.existe(nombre_archivo):
            print(_('El archivo no existe:', nombre_archivo), '\n')
            sys.exit(1)
            
    def _acerca_de(self):      
        print(conf.NOMBRE_AP,'v'+conf.VERSION)        
        print(_(conf.DESCRIPCION_APP), '\n')
        print(conf.CREDITOS, '\n')        
             
   
    def _get_parser(self):
        
        parser = argparse.ArgumentParser(
            description=conf.NOMBRE_AP+" "+str(conf.VERSION) ) 
        group = parser.add_mutually_exclusive_group()         
        group.add_argument('-v', '--validar', nargs=2,
                           metavar=(_('ARCHIVO_XML'), _('ARCHIVO_SXD')), help=_('Valida un fichero xml a partir del esquema sxd'))                      
        group.add_argument('-c', '--crear', type=str,
                           metavar=(_('ARCHIVO')), help=_('Crea el esquema sxd a partir de un fichero xml'))         
        parser.add_argument('--version', action='version', version='%(prog)s ' +
                            conf.VERSION, help=_('Muestra la versión del programa'))
        parser.add_argument("--acerca", action='store_true', help=argparse.SUPPRESS)
        
        return parser

    def _procesar_argumentos(self, parser):
        
        args = parser.parse_args()     
        self._ejecutar_modo_consola(args)



if __name__ == "__main__":
     
    ValidarXml()
