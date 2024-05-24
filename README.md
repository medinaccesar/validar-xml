# validar-xml
Permite validar un fichero XML con su esquema SXD, genera, también, un fichero de esquema a partir de un fichero XML. 

# Requisitos
 Python 3.
 
# Instalación de dependencias
Se instalan las dependencias:
```
 pip install -r requirements.txt
 ```
Se compilan los archivos de idiomas:
```
python utils/compile_lang.py 
```
# Uso
```
Uso: validar-xml.py [-h] [-v ARCHIVO_XML ARCHIVO_SXD | -c ARCHIVO] [--version]

validar-xml 0.1.0

opciones:
  -h, --help            muestra este mensaje de ayuda y sale
  -v ARCHIVO_XML ARCHIVO_SXD, --validar ARCHIVO_XML ARCHIVO_SXD
                        Valida un fichero xml a partir del esquema sxd
  -c ARCHIVO, --crear ARCHIVO
                        Crea el esquema sxd a partir de un fichero xml
  --version             Muestra la versión del programa
```
Por ejemplo:
* **Validar que un fichero XML cumple con un esquema XSD:**
 ```
python validar-xml.py -v ./rec/ejemplo.xml ./rec/esquema.sxd 
El documento es válido
```
* **Generar un esquema SXD a partir de un fichero XML:**
 ```
python validar-xml.py -c ./rec/ejemplo.xml  
Se ha creado el esquema: ./rec/ejemplo_240525_004132.sxd 
```
# Traducciones / Translations
Se puede usar como base ./locale/programa.po y con «poedit» u otro editor rellenar las traducciones.  El archivo se coloca dentro de la carpeta correspondiente, por ejemplo para portugués en ./locale/pt/LL_MESSAGES/:

```
validar-xml/
├─ README.md
├─ validar-xml.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        └─programa.po
│  ├─ ...
|
├─ ...  
```
Posteriormente se compila el archivo de traducción ejecutando:
```
python utils/compile_lang.py 
```
El idioma de la aplicación, (distinto de español), se fija en el archivo .env, (renombrar .env.template):
```
IDIOMA = 'pt'
```

[EN] You can use as a base ./locale/programa.po and with "poedit" or another editor fill in the translations.  The file is placed inside the corresponding folder, for example for Portuguese in ./locale/pt/LL_MESSAGES/:
```
validar-xml/
├─ README.md
├─ validar-xml.py
├─ ...
├─ locale/
│  ├─ pt/    
│  │   └─ LL_MESSAGES/
│  │        └─programa.po
│  ├─ ...
|
├─ ...  
```
Subsequently, the translation file is compiled by executing:
```
python utils/compile_lang.py 
```
The application language is set in the .env file, (remane .env.template):
```
IDIOMA = 'pt'
```

# Ejecutables para linux ubuntu y windows

Se puede crear el ejecutable con «pyinstaller».
