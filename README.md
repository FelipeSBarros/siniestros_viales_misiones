# Siniestros Viales en Misiones desde los diários

El objetivo de este repositorio es gestionar el codigo de raspaje de datos con [scrapy](https://docs.scrapy.org/) de reportajes periodísticos de los diários de Misiones.

## Corriendo el raspador

```python
scrapy crawl primera_edicion -o archivo.txt
```

## Al respecto de las configuraciones

Se deshabilitó la opción de seguir las autorizaciones de la página presentes en `robot.txt`, bien como se instaló [`scrapy-fake-useragent`](https://github.com/alecxe/scrapy-fake-useragent) para que siempre que la página retorne error 403, se vuelva a ejecutar simulando un `agente` distinto;
