# Curso de Machine Learning Thincrs

Instructor: [Alan Badillo Salas](mailto:alan@nomadacode.com)

## Ejercicios

Las siguientes series de ejercicios permiten profundizar y madurar los temas vistos en clase.
Cada serie tiene 3 niveles de dificultad (Básica, Intermedia y Avanzada).

Es obligatorio mandar por correo los ejercicios básicos (mínimo).
Los demás ejercicios serán considerados para ponderar el alumno de mayor aprovechamiento del curso.

### Serie I - Dominio de Python

> **E101** - Manejo de listas

Define una lista de 10 valores enteros y la lista con cada valor elevado al cuadrado.

> **E102** - Manejo de tuplas

Define una función que reciba una lista y devuelva el mínimo y máximo de la lista al mismo tiempo.

> **E103** - Manejo de Listas de tuplas

Define una lista de tuplas con los datos de puntos `(x, y)`.
Determina cuál es el promedio de las `x`, cuál es el promedio de las `y`.

### Serie II - Dominio de Numpy

> **E201** - Manejo de arreglos

Crea un arreglo de 20 puntos con valores aleatorios bajo 
la distribución normal con media `5` y desviación estándar `2.5`.

> **E202** - Operaciones de arreglos

Crea un arreglo de 100 puntos y determina la suma, el promedio,
el mínimo, el máximo, la desviación estándar y los cuantiles 25%, 50% y 75%.

> **E203** - Operaciones de matrices

Crea una matriz de `10x5` y recupera el arreglo con los valores
de la primera columna, la segunda columna, la tercera columna, 
la cuarta columna y la quinta columna.

Ejemplo:

```text
1 4 8 7 6
3 9 2 1 3
6 1 4 8 6
5 4 5 6 3
1 2 3 4 2
1 4 8 7 6
3 9 2 1 3
6 1 4 8 6
5 4 5 6 3
1 2 3 4 2
```

Primera columna:

```text
1 3 6 5 1 1 3 6 5 1
```

### Serie III - Dominio de Pandas

> **E301** - Leer un DataFrame desde un CSV

Descarga un archivo CSV y cárgalo en un DataFrame. 
Muestra la información del DataFrame y su descripción (estadísticos principales).

> **E302** - Extraer las columnas de análisis

Dado un DataFrame, crea un nuevo DataFrame que contenga solo las columnas de análisis.

> **E303** - Limpieza y transformación de columnas

Dado un DataFrame, define una función que limpie y transforme los valores,
considera que estos pueden ser `nan`.

Por ejemplo, si la columna contiene categorías como el SEXO,
sustituye los valores `nan` por `X`. Luego convierte los valores a categorías numéricas.

### Serie IV - Dominio de Matplotlib y Seaborn

> **E401** - Visualización de puntos

Define un arreglo o serie `x` y un arreglo o serie `y`.
Visualiza la gráfica de puntos usando el color rojo y líneas punteadas que los conecten.

> **E402** - Histograma y Pastel

Dada una columna de un DataFrame, muestra el histograma de dicha columna si es un valor continuo
o una gráfica de Pastel si es categórico, en este último caso tendrás que
contar cuántas veces aparece cada categoría.

> **E403** - Visualización de puntos coloreados

Dado un DataFrame, selecciona dos columnas continuas para contrastar dichos ejes,
luego selecciona una tercera columna que represente el objetivo y sea
utilizada para colorear la gráfica.

Genera la gráfica de puntos usando el tercer eje como el color.

### Serie V - Dominio de Aprendizaje Supervisado por Regresión

> **E501** - Regresión lineal

Dado un DataFrame, selecciona las columnas de análisis (1 o más) y forma
la matriz `X` con los valores numéricos de las características (columnas seleccionadas).

Selecciona una columna adicional que será el objetivo a aprender,
esta columna debe tener valores continuos (no categóricos). 
Y extrae los valores como `y`.

Crea un regresor lineal usando los modelos lineal y ajusta la matriz
`X` y el vector `y` al regresor.

Obtén el indicador `score` para `X` y `y`.

> **E502** - Predicción de valores en la regresión lineal

Crea una regresión lineal sobre una sola variable y
predice los valores que tendría todo un eje de datos.

Por ejemplo, si el eje `x` es `ESTATURA` y el eje `y` es `PESO`,
entonces predice todos pesos para los valores para estaturas desde `1.0` 
hasta los `2.0` metros.

Visualiza los puntos reales y las predicciones en una misma gráfica.

> **E503** - Regresión lineal multivariable

Crea una regresión lineal sobre dos variables y
visualiza el plano de los valores de predicción.

Por ejemplo, si el eje `x1` es `PRECIO`, el eje `x2` es `EXISTENCIAS`,
y el eje `y` es `DEMANDA`, entonces visualiza los puntos en 3 dimensiones
para diferentes precios, existencias y demandas de productos.

Luego genera las predicciones para los precios desde el menor hasta el mayor
de `0.5` en `0.5` y las existencias desde `0` hasta la máxima existencia
de `1` en `1`. Por último deberías graficar en 3 dimensiones el plano y los puntos
reales para visualizar que tanto se aproxima el plano de predicción a
los valores reales.

### Serie VI - Dominio de Aprendizaje Supervisado por Clasificación

> **E601** - Clasificación del Conjunto de datos de la planta Iris

Carga el DataFrame del `Iris` y construye las matrices `X` y el vector `y`
(con la variedad o especie de la planta, es decir, la familia que se busca aprender).

Carga el modelo de clasificación por árboles de decisión y muestra
el indicador `score` de aprendizaje para `X` y `y`.

> **E602** - Clasificación de Diabetes

Busca un Dataset que contenga registros de pacientes diabéticos y no diabéticos
y entrena un clasificador para determinar si dadas las características de un paciente
desarrollará o no diabetes.

Compara la tasa de aprendizaje del clasificador con otro clasificador distinto.

> **E603** - Clasificación de dígitos

Carga el Dataset con las imágenes de dígitos escritos a mano llamado `MNIST`.

Sigue algún tutorial o intuye cómo convertir cada imagen en un vector de 784 valores.

Usa un modelo de clasificación para aprender a reconocer los dígitos.

Grafica un dígito del Dataset, su clase real y la que fue predicha.

### Serie VII - Dominio de Reducción de la dimensionalidad

> **E701** - Reducción de variables del `Iris`

Carga el Dataset del `Iris` y extrae la matriz `X` de características
y el vector `y` de objetivos.

Grafica la columna `sepal.length` contra `sepal.width` en puntos,
usando `variety` como el color.

Crea una matriz `Xp` con los primeros 2 componentes principales de `X`.

Grafica la columna del primer componente de `Xp` contra
el segundo componente de `Xp` en puntos,
usando `variety` como el color.

Contrasta ambas gráficas indicando visualmente si es posible separar
las clases con una recta en ambas gráficas (usa una captura de pantalla
y dibuja a mano las rectas).

> **E702** - Reducción de muchas características

Busca un Dataset con muchas características numéricas, por ejemplo,
las reseñas de usuarios o datos de personas.

Extrae los primeros 2 componentes principales y genera la gráfica de puntos.

Dibuja manualmente elipsoides que separarían los datos.

Determina visualmente el centro de uno de los elipsoides.

Calcula la distancia de los 2 componentes al centro del elipsoide seleccionado.

Obtén el índice del registro en la matriz de los 2 componentes más cercano al elipsoide.

Muestra todas las características del registro de la matriz original en ese índice.

Este debería representar la muestra más cercana al elipsoide.

> **E703** - Regresión lineal de la característica principal

Usa el Dataset con muchas características numéricas para reducir
un solo componente principal y aplicar una regresión lineal hacia un objetivo.

Determina si el $R^2$ es mayor o igual a `0.3` para considerarse suficiente.

### Serie VIII - Dominio de Aprendizaje No Supervisado por Agrupación

> **E801** - Agrupación del `Iris`

Replica el caso de uso visto en clase para encontrar las etiquetas
usando el algoritmo de `K-Means` y grafica las etiquetas reales y las encontradas.

Modifica el ejercicio para usar el algoritmo de `DBSCAN` en lugar
del algoritmo de `K-Means`.

> **E802** - Agrupación de muchas características

Busca un Dataset con muchas características numéricas, por ejemplo,
las reseñas de usuarios o datos de personas.

Determina un máximo de 5 grupos distintos y agrega la predicción
del grupo para cada registro.

> **E803** - Agrupación de muchas características usando 2 componentes principales

Repite el ejercicio anterior, pero utilizando los primeros 2 componentes principales.

Visualiza las categorías coloreadas.

## Bienvenida

Bienvenidos al curso de Machine Learning 🤖 con Python 🐍 de Thincrs.

Hola a Todos.

Es un gusto darles la bienvenida al curso de Machine Learning de TAE.

Mediante este correo estaré resolviendo sus dudas.

Les dejo algunos puntos importantes que se dieron en la primera clase:

Punto 1 - Repositorio del curso

Todo el contenido del curso está en un repositorio público en la siguiente liga:

https://github.com/dragonnomada/thincrs-machine-learning-2023-oct/tree/main

Punto 2 - Evaluación

Cada semana se dejará entre ejercicios que determinarán el nivel de aprovechamiento en diferentes dificultades. Son libres de hacer mínimo los de dificultad baja, no menos.

Al final habrá un examen final.

Punto 3 - Plataforma y grabaciones

Tienen una plataforma dónde podrán consultar cosas adicionales. También tendrán acceso a las grabaciones (preguntar al mentor).

https://drive.google.com/drive/folders/1Atx121hXAbvdWTE_dZVKxz4bcZk3nJaO?usp=sharing

Punto 4 - Asistencia

La asistencia es obligatoria (75% me parece), por lo que si faltan a una sesión tienen que enviarme correo aquí y copia al mentor. Según las indicaciones que me hicieron llegar:

Nota: Para avisos de ausentismo, deberán avisarle al mentor y enviar correo a educacion@thincrs.com con copia al mentor.

Por el momento es todo.

Cualquier duda quedo al pendiente.

Mucho éxito a todos en su curso.

Nota: Cualquier comentario que no quieran expresar en clase será bien recibido y tomado en cuenta.

## Ficha Técnica

    Curso: Machine Learning

    Duración: 20 Hrs

En este curso aprenderás:

> Comprender los conceptos básicos de machine learning y su importancia
en el análisis de datos.

> Familiarizarse con las bibliotecas y herramientas esenciales para
machine learning en Python, como scikit-learn, NumPy, SciPy,
matplotlib y pandas.

> Aprender a utilizar algoritmos supervisados y no supervisados para
clasificación, regresión y agrupación de datos.

> Desarrollar habilidades en la evaluación y mejora de modelos de
machine learning mediante técnicas de validación cruzada, búsqueda en
cuadrícula y selección de características.

> Aplicar machine learning a problemas reales, como la clasificación de
especies de iris y el análisis de sentimientos de reseñas de
películas.

> Obtener una visión general de temas avanzados en machine learning y
las direcciones futuras en el campo.


Prerrequisitos:

* Fundamentos del lenguaje Python y su sintaxis (uso de variables, condicionales, iteradores, funciones). 

* Nociones de programación en cualquier lenguaje de programación.

* Nociones matemáticas de álgebra y cálculo (es recomendable, más no necesario haber cursado álgebra discreta, álgebra lineal, cálculo diferencial y optimización)

* Tener una formación técnica, de licenciatura o ingeniería computacional, matemáticas o afín


Temario:

> Módulo 1: Introducción

- ¿Por qué machine learning?
- ¿Por qué Python?
- scikit-learn
- Bibliotecas y Herramientas Esenciales
- Una Primera Aplicación: Clasificación de Especies de Iris

> Módulo 2: Aprendizaje Supervisado

- Clasificación y Regresión
- Generalización, Sobreajuste y Subajuste
- Algoritmos de machine learning Supervisado
- Estimaciones de Incertidumbre de los Clasificadores

> Módulo 3: Aprendizaje No Supervisado y Preprocesamiento

- Tipos de Aprendizaje No Supervisado
- Desafíos en el Aprendizaje No Supervisado
- Preprocesamiento y Escalado
- Reducción de Dimensionalidad, Extracción de Características y
- Aprendizaje de Manifolds
- Agrupamiento (Clustering)

> Módulo 4: Representación de Datos e Ingeniería de Características

- Variables Categóricas
- OneHotEncoder y ColumnTransformer: Variables Categóricas con
- scikit-learn
- Creación Conveniente de ColumnTransformer con make_columntransformer
- Agrupamiento, Discretización, Modelos Lineales y Árboles
- Interacciones y Polinomios
- Transformaciones Univariables No Lineales
- Selección Automática de Características
- Utilizando el Conocimiento de Expertos

> Módulo 5: Evaluación y Mejora de Modelos

- Validación Cruzada (Cross-Validation)
- Búsqueda en Rejilla (Grid Search)
- Métricas de Evaluación y Puntuación

> Módulo 6: Trabajando con Datos de Texto

- Tipos de Datos Representados como Cadenas de Texto
- Ejemplo de Aplicación: Análisis de Sentimientos de Reseñas de Películas
- Representación de Datos de Texto como un Conjunto de Palabras (Bag of Words)
- Palabras Vacías (Stopwords)
- Reescalado de Datos con tf-idf
- Investigación de Coeficientes del Modelo
- Bag-of-Words con Más de una Palabra (n-Gramas)
- Tokenización Avanzada, Stemming y Lemmatization
- Modelado de Temas y Agrupamiento de Documentos

