# <ins>**TPI - BIENAL**</ins> 😉




## Integrantes

**Irala Damian**
**Enzo Coschiza**
**Fabricio Jerez**
**Chiara Diez**
**Felipe Fidanzas**
**Juan Ignacio Drose**

### Clases
- `Proceso`: Representa un proceso con atributos como tamaño, tiempo de llegada, y tiempo de irrupción.
- `Particion`: Representa una partición de memoria con atributos como tamaño y estado de ocupación.

### <ins>Funciones Principales</ins>
- `cargar_procesos`: Carga la lista de procesos desde un archivo de texto.
- `actualizar_estado`: Actualiza el estado de los procesos y las particiones de memoria.
- `asignar_memoria`: Asigna memoria a los procesos utilizando el algoritmo de **Worst Fit**.
- `ejecutar_proceso`: Ejecuta los procesos en la cola de listos.
- `liberar_memoria`:  Libera la memoria ocupada por los procesos completados.
- `round_robin`: Implementa el algoritmo de planificación **Round Robin** para la ejecución de procesos.
- `mostrar_estado`: Muestra el estado actual de la memoria y los procesos.
- `mostrar_resultado`: Genera un informe estadístico con el tiempo de retorno promedio, tiempo de espera promedio, y rendimiento del sistema.

### Funcion Principal
`main`: Es el punto de entrada del programa. Su flujo incluye:
   1. Carga de procesos.
      
   3. Muestra del estado inicial de los procesos y la memoria.
      
   5. Ejecución del algoritmo de **Round Robin** mostrando el estado de la memoria por cada proceso.
      
   6. Muestra del estado final.
      
   7. Presentación de los resultados estadísticos.

## <ins>Uso</ins> 💯
Para usar el simulador, simplemente ejecuta el archivo <code>simulador.py</code> con Python. Debes tener un archivo <code>procesos.txt</code> en el mismo directorio que <code>simulador.py</code> , con una lista de procesos en el formato correcto.

Además, este script utiliza la biblioteca <code>prettytable</code>. Si no la tienes instalada, puedes hacerlo utilizando pip, el administrador de paquetes de Python, con el siguiente comando:

    pip install prettytable
  
Una vez que hayas verificado que Python está instalado correctamente y que has instalado prettytable, puedes ejecutar el script de Python con el siguiente comando:

    python simulador.py

### Uso con .exe 
1. Ingresar a la carpeta `ejecutable`
2. Abrir el ejecutable `simulador.exe`
> Si se desea cambiar los procesos.
> El archivo `procesos.txt` tiene procesos de ejemplo para modificarlos, se debe de *respetar el formato* de la carga de procesos mencionado.

## Formato de los procesos 🧱
Cada línea del archivo <code>procesos.txt</code> debe tener el formato `id_proceso` ,`tamano` ,`tiempo_arribo` ,`tiempo_irrupcion`, donde:

- <code>id_proceso</code> es un número entero que identifica al proceso.
- <code>tamano</code> es el tamaño del proceso.
- <code>tiempo_arribo</code> es el tiempo en que el proceso llega al sistema.
- <code>tiempo_irrupcion</code> es el tiempo que el proceso necesita para completarse.
