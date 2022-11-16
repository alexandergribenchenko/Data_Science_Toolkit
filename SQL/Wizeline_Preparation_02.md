

- https://www.simplilearn.com/data-modeling-interview-question-and-answers-article

- https://career.guru99.com/top-50-datawarehousing-questions-answers/

- https://hevodata.com/learn/data-engineering-tools/

- https://verneacademy.com/blog/articulos-data/que-es-data-warehouse-data-marts-diferencias/

## ¿Qué es una vista?
Una vista es una tabla virtual cuyo contenido está definido por una consulta. Al igual que una tabla, una vista consta de un conjunto de columnas y filas de datos con un nombre. Sin embargo, a menos que esté indizada, una vista no existe como conjunto de valores de datos almacenados en una base de datos.

## ¿Qué es una OLTP y OLAP?
Aunque son similares y son ambos sistemas de procesamiento de datos en línea, hay una gran diferencia entre ambos. OLTP permite la ejecución en tiempo real de un gran número de transacciones por parte de un gran número de personas, mientras que el procesamiento analítico en línea (OLAP) suele implicar la consulta de estas transacciones (también denominadas registros) en una base de datos con fines analíticos. OLAP ayuda a las empresas a extraer información de sus datos de transacción para que puedan utilizarla para tomar decisiones más informadas.

# What is a Data Model?

Un modelo de datos **organiza diferentes elementos de datos y estandariza cómo se relacionan entre sí** y las propiedades de la entidad del mundo real. Entonces, lógicamente, el modelado de datos es el proceso de creación de esos modelos de datos.

Los modelos de datos se componen de **entidades**, y las entidades son los objetos y conceptos cuyos datos queremos rastrear. Ellos, a su vez, se convierten en tablas que se encuentran en una base de datos. Los clientes, productos, fabricantes y vendedores son entidades potenciales.

Cada entidad tiene **atributos**: detalles que los usuarios desean rastrear. Por ejemplo, el nombre de un cliente es un atributo.


# Basic Data Modeling Interview Questions

## 1. What Are the Three Types of Data Models?

- **Modelo de datos físicos:** aquí es donde el marco o esquema describe cómo se almacenan físicamente los datos en la base de datos.
- **Modelo de datos conceptuales:** este modelo se centra en la vista de usuario de alto nivel de los datos en cuestión.
- **Modelos de datos lógicos:** se extienden entre los modelos de datos físicos y teóricos, lo que permite que la representación lógica de los datos exista aparte del almacenamiento físico.


## 2.  What is a Table?
Una tabla consta de datos almacenados en filas y columnas. Las columnas, también conocidas como campos, muestran datos en alineación vertical. Las filas, también denominadas registros o tuplas, representan la alineación horizontal de los datos.

## 3. What is Normalization?
La normalización de la base de datos es el proceso de diseñar la base de datos de tal manera que **reduzca la redundancia de datos sin sacrificar la integridad**.

## 4. What Does a Data Modeler Use Normalization For?
- Eliminar datos inútiles o redundantes
- Reducir la complejidad de los datos
- Garantizar las relaciones entre las tablas además de los datos que residen en las tablas
- Asegure las dependencias de datos y que los datos se almacenen lógicamente.

## 5. So, What is Denormalization, and What is its Purpose?
La desnormalización es una técnica en la que se agregan datos redundantes a una base de datos ya normalizada. El procedimiento mejora el rendimiento de lectura al sacrificar el rendimiento de escritura.

## 6. What Does ERD Stand for, and What is it?
ERD significa Diagrama de relación de entidad y es una representación de entidad lógica, que define las relaciones entre las entidades. Las entidades residen en cajas y las flechas simbolizan las relaciones.

## 7. What’s the Definition of a Surrogate Key?
Una clave sustituta, también conocida como clave principal , impone atributos numéricos. Esta clave sustituta reemplaza las claves naturales. En lugar de tener claves primarias o compuestas, los modeladores de datos crean la clave sustituta, que es una herramienta valiosa para identificar registros, crear consultas SQL y mejorar el rendimiento.

## 8. What Are the Critical Relationship Types Found in a Data Model? Describe Them.

## 9. What is an Enterprise Data Model?
Este es un modelo de datos que consta de todas las entradas requeridas por una empresa.

# Intermediate Data Modeling Interview Questions

## 10. What Are the Most Common Errors You Can Potentially Face in Data Modeling?
- **Falta el propósito:** pueden surgir situaciones en las que el usuario no tenga idea de la misión o el objetivo de la empresa. Es difícil, si no imposible, crear un modelo comercial específico si el modelador de datos no tiene una comprensión viable del modelo comercial de la empresa.
- **Desnormalización inapropiada:** los usuarios no deben usar esta táctica a menos que haya una excelente razón para hacerlo. La desnormalización mejora el rendimiento de lectura, pero crea datos redundantes, lo cual es un desafío para mantener.

## 11. Explain the Two Different Design Schemas (Star schema and Snowflake schema.)
El esquema de dos diseños se denomina esquema de estrella y esquema de copo de nieve. El esquema de estrella tiene una tabla de hechos centrada con varias tablas de dimensiones que la rodean. Un esquema de copo de nieve es similar, excepto que el nivel de normalización es más alto, lo que hace que el esquema parezca un copo de nieve.


## 12. What is a Slowly Changing Dimension?


## 13. What is Data Mart?
Un data mart es el conjunto más sencillo de almacenamiento de datos y se utiliza para centrarse en un área funcional de cualquier negocio determinado. Los data marts son un subconjunto de almacenes de datos orientados a una línea de negocio o área funcional específica de una organización (p. ej., marketing, finanzas, ventas). Los datos ingresan a los data marts mediante una variedad de sistemas transaccionales, otros almacenes de datos o incluso fuentes externas.

## 14. What is Granularity?
La granularidad representa el nivel de información almacenada en una tabla. La granularidad se define como alta o baja. Los datos de alta granularidad contienen datos de nivel de transacción. La granularidad baja solo tiene información de bajo nivel, como la que se encuentra en las tablas de hechos.

15. What is Data Sparsity, and How Does it Impact Aggregation?


16. What Are Subtype and Supertype Entities?

17. In the Context of Data Modeling, What is the Importance of Metadata?


# Advanced-Data Modeling Interview Questions
18. Should All Databases Be Rendered in 3NF?

19. What’s the Difference Between forwarding and Reverse Engineering, in the Context of Data Models?

20. What Are Recursive Relationships, and How Do You Rectify Them?

21. What’s a Confirmed Dimension?

## 22. Why Are NoSQL Databases More Useful than Relational Databases?
- Pueden almacenar datos estructurados, semiestructurados o no estructurados.
- Tienen un esquema dinámico, lo que significa que pueden evolucionar y cambiar tan rápido como sea necesario.
- Las bases de datos NoSQL tienen fragmentación, el proceso de dividir y distribuir datos a bases de datos más pequeñas para un acceso más rápido
- Ofrecen failover y mejores opciones de recuperación gracias a la replicación
- Es fácilmente escalable, crece o se reduce según sea necesario.


23. What’s a Junk Dimension?

24. If a Unique Constraint Gets Applied to a Column, Will It Generate an Error If You Attempt to Place Two Nulls in It?






