Tarea
=====================

**NOTA** No se te olvide crear una carpeta llamada `python` en tu carpeta de usuario en este repositorio.
**NOTA** Esta tarea se debe de entregar en un `Jupyter notebook`, debes de entregarlo como reporte en forma (Usa texto para explicar
lo que quieres hacer, usa secciones (Introducción, Ejercicios, Conclusiones), usa imágenes que den sentido a lo que dices, etc)

## Ejercicio 1

1. Modifica `Turista.py` para ejecutar 10000 partidas
4. Agrega a `Jugador` los métodos `comprar(posicion)` y `pagar_renta(posicion)` y modifica acordemente la clase `Turista` 
2. Arregla el *bug* de que el jugador se page renta así mismo.
2. Modifica la clase `País` agregando el método `disponible()` que indica si ese país se puede comprar o rentar.
2. Usando `turista.log`, crea un `pandas` `data frame` que contenga información para hacer el análisis que se te pedirá
   (i.e. transformar el `log` en un `data frame`.
3. Responde las preguntas 
   - ¿Cuánto dura la partida promedio? 
   - ¿Cuántos partidos gana cada jugador?¿Cuánto gana?¿Y si graficas por posición al finalizar el juego? 
       ¿Afecta la posición del jugador?¿Afecta su ganancia?
   - ¿Cuáles son las mejores casillas? ¿Qué características tienen?
  


## Ejercicio 2
1. Usando [herencia](http://www.python-course.eu/python3_inheritance.php) crea una clase llamada `Turista2(Turista)` 
(no estaba muy creativo el día de hoy). Agrega las siguientes reglas: 
    - Agrega la regla de que en la primera vuelta no es posible comprar.

2. Contesta la preguntas anteriores ¿Son diferentes los juegos? Justifica tus respuestas


## Ejercicio 3

1. Usando [herencia](http://www.python-course.eu/python3_inheritance.php) crea una clase llamada `Turista3(Turista2)` 
(sigo sin estar creativo). Agrega las siguientes reglas: 
    - La regla de *Deportación* (Si caes en "Deportación" el usuario va a Groelandia y debe de pagar 5000, si no tiene esa cantidad 
      se quedará ahí 3 turnos.
    - Cada vez que llega a *México* el jugador recibe 20000
    - Si cae en *Aduana* paga 1000

      
## Aclaración y Cultura general

En este ejercicio usamos *herencia*, la práctica recomendada actual es usar **Composicón** lo cual se hubiera traducido en 
una nuevas clases llamadas *Jugada* y *Regla* que *compondrían* a la clase Turista. 
      

## Referencias

- [Reglamento Turista Mundial](www.montecarlo.com.mx/assets/turista-mundial.pdf)
- [*Black and Whites*](https://boardgamegeek.com/boardgame/7245/blacks-whites)
