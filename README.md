# Siniestros Viales en Misiones desde los diários

El objetivo de este repositorio es gestionar el codigo de raspaje de datos con [scrapy](https://docs.scrapy.org/) de
reportajes periodísticos del diário de Misiones [Primera Edición](https://www.primeraedicion.com.ar/).
El resultado de dicho raspaje es un archivo `.csv` que contiene la siguiente información:

- `titulo`: título del artículo
- `subtitulo`: subtitulo del artículo
- `url`: link al artículo
- `fecha`: fecha de publicación del artículo
- `cuerpo`: cuerpo del artículo
- `tags`: etiquetas del artículo
- `url_imagenes`: urls de las imágenes del artículo

Los artículos raspados serán georreferenciados y analisados por estudiantes de
la [Tecnicatura Universitária en Sistemas de Información Geográfica y Teledetección (TUSIGyT)](https://www.fcf.unam.edu.ar/carreras/tec-univ-sist-infor-geo-tele/)
de
la [Facultad de Ciencias Forestales (FCF)](https://www.fcf.unam.edu.ar/) de la Universidad Nacional de Misiones (UNaM);

## Resultados ya obtenidos

- Claudia Vargas:
  `Geotecnologías aplicadas al análisis de siniestros viales ocurridos en Misiones durante los años 2022 y 2023, reportados por el diario Primera Edición`
    - [Tesis Final](https://tusigyt.github.io/lit/assets/publicaciones/2024_Claudia_Maria_Vargas.pdf)
    - [Datos producidos](https://tusigyt.github.io/lit/assets/datos/siniestros_viales_Misiones_2022-2023.gpkg)
    - [Mapa interactivo](https://tusigyt.github.io/lit/proyectos/siniestros_viales/siniestros_viales_Misiones_2022-2023.html)
    - [Tablero de control](https://development.demo.geonode.org/catalogue/#/dashboard/2399)

## Corriendo el raspador

```python
scrapy
crawl
primera_edicion - o
archivo.csv
```

## Al respecto de las configuraciones

Se deshabilitó la opción de seguir las autorizaciones de la página presentes en `robot.txt`, bien como se instaló [
`scrapy-fake-useragent`](https://github.com/alecxe/scrapy-fake-useragent) para que siempre que la página retorne error
403, se vuelva a ejecutar simulando un `agente` distinto;
