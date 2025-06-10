# StreamX
Este repositorio contiene la implementación de StreamX, un pipeline de datos en tiempo real diseñado para capturar, procesar y almacenar información desde X

## Objetivo. 

Capturar datos en tiempo real desde X (Twitter), procesarlos y almacenarlos para su posterior análisis o visualización.

## Tecnologías empleadas. 

- Ingesta de datos: API de X (Twitter API v2).
- Procesamiento en tiempo real:	Apache Kafka o Apache Spark Streaming.
- Almacenamiento: MongoDB.
- Visualización: Power BI

## Arquitectura

Para este proyecto se empleará una arquitectura LAMBDA, ya que:

- Las redes sociales como X son altamente dinámicas: los datos cambian segundo a segundo.
- Se requiere procesar y reaccionar rápidamente ante menciones, hashtags o eventos relevantes (por ejemplo, alertas o tendencias virales).
- La capa de velocidad (Speed Layer) de la arquitectura Lambda permite procesar datos en tiempo real utilizando tecnologías como Apache Kafka y Spark Streaming.
- Twitter genera grandes cantidades de datos constantemente.
- La arquitectura Lambda está diseñada para ser escalable horizontalmente, lo que permite manejar tanto flujos en vivo como procesamiento de grandes datasets históricos.
- La capa de servicio (Serving Layer) unifica los resultados del procesamiento en tiempo real y por lotes.
- Esto permite que las visualizaciones o reportes consuman los datos más recientes y también los más fiables y refinados.

