# AutoWeb
Automatización Descarga de imágenes y obtención de datos de la página "Seminuevos"

Primeros Avances:
* [x] Obtención del Modelo del Auto.
* [x] Obtención del precio.
* [x] Obtención de la descripción.
* [x] Obtención de Imágenes.

Pasos siguientes:
* [ ] Crear archivos separados incluyendo un "Main" para ejecución de ciclos, etc.
* [ ] Creación de carpeta general de lista con nombre "Autos" + fecha del sistema. (El path debería de ser /AutosSeminuevos/Autos x.x.x)
* [ ] Creación de ciclo para una lista de URL.
* [ ] Posiblemente hacer una pequeña UI para el ingreso de URL.
* [ ] Creación de Carpeta con modelo del auto.
* [ ] Guardado de Info en txt.
* [ ] Guardado de Imágenes en carpeta.



Ciclo al descargar
Click y descargar en imágen principal, verificar si es igual a la anterior, de otro modo,
luego hacer click en siguiente imágen, descargar, verificación, siguiente, descargar...

Datos útiles:
- "import urllib" Para descargas de links
- ".isalnum()" Para eliminar caracteres especiales
