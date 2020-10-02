# AutoWeb
Automatización Descarga de imágenes y obtención de datos de la página "Seminuevos"

### Primeros Avances:
* [x] Obtención del Modelo del Auto.
* [x] Obtención del precio.
* [x] Obtención de la descripción.
* [x] Obtención de una imágen.

### Pasos siguientes:
* [ ] Crear contador para imágenes.
* [ ] Crear ciclo para la descarga de todas las imágenes.
* [ ] Crear funciones para poder manejar todo en "main.py".
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

### Datos útiles:
- "import urllib" Para descargas de links
- ".isalnum()" Para eliminar caracteres especiales
- Para clicks en background: https://forum.uipath.com/t/can-we-have-web-automation-working-in-background/122402/2

## Listado para Testear

* http://seminuevosmag.cl/car/ford-ranger-2016-3/
* http://seminuevosmag.cl/car/dodge-ram-1000-ano-2020/
* https://www.yapo.cl/magallanes_antartica/autos/mg_350_2017_72788286.htm
* http://seminuevosmag.cl/car/chevrolet-camaro-2010/
* http://seminuevosmag.cl/car/brillance-v3-2019/
* http://seminuevosmag.cl/car/chevrolet-sail-2016-2/
* http://seminuevosmag.cl/car/ford-f150-2015/
* http://seminuevosmag.cl/car/mitsubishi-lancer-2015-2/
* https://www.yapo.cl/magallanes_antartica/autos/jeep_wrangler_2013_72921113.htm
* https://www.yapo.cl/magallanes_antartica/autos/land_rover_evoque_2019_73389566.htm