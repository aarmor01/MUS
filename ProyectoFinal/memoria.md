# Música adaptativa con FMOD Studio

## Propuesta inicial
Investigar el uso de la herramienta FMOD Studio para la creación de música adaptativa en videojuegos. Aplicación de esta herramienta en un prototipo de escena 3D en Unity para generar un entorno con música adaptativa.

## Desarrollo de la propuesta
Se utilizará la herramienta FMOD Studio para crear un entorno 3D con música adaptativa con estas características:
    • Un personaje jugable, con vida.
    • Dos zonas de juego diferenciadas entre sí.
    • Dos enemigos “torreta” en una de las zonas, que quitarán vida cuando el jugador esté a la vista.

Además, se usará una composición propia, hecha en Reaper, para la música en las distintas zonas/condiciones.

## Reaper (Composición)
Para la composición de Reaper, en un primer momento se han seguido los pasos de composición vistos en el último ejercicio de clase (fondo, melodía, percusión, progresiones, etc; de manera progresiva):
    • Para las melodías, se usan las escalas de La menor y Mi menor.
    • Para las progresiones, se usa (I-IV-V-I) para la progresión de piano en combate; y (I-IV-II-V-IV) para la melodía de flauta de muerte.

Tras haber conseguido una composición aceptable, se han adaptado las pistas para una posterior exportación a FMOD, dividiendo esta en las cuatro secciones principales usadas en este proyecto:
    • Intro: Música de la primera zona (sin enemigos). Contiene ambiente, melodía de piano, y percusión.
    • OtherZone: Música de la segunda zona. Contiene el mismo ambiente, melodía de piano, y percusión que en la primera zona, pero aplicando instrumentos virtuales distintos.Música adaptativa con FMOD Studio
    • Combate: Música de la primera zona, cuando uno o más enemigos son visibles. Contiene ambiente, progresión (usando el mismo piano usado en las melodías anteriores), melodía de flauta, acompañamiento de trombón, y percusión (esta última sonará cuando haya más de un enemigo atacando a la vez).
    • Death: Música que suena al perder toda la vida. Contiene melodía de flauta (con progresión), un sample de latido de corazón, y violines que acompañan al latido.

## FMOD Studio
Tras la composición hecha en Reaper, se aplicará las pistas en FMOD Studio, con estas características:
    • Habrán tres variables (Enemies, Health y OtherZone) de las que dependen las variaciones en las pistas.
    • Región de inicio: tiene tres pistas, una de ellas de ambiente y las otras dos que variarán dependiendo si el usuario se encuentra en la primera o en la segunda zona.
    • Región de combate: dispone de una pista principal y una secundaria con percusiones. La primera pista entrará cuando “Enemies” sea mayor que 0, mientras que la segunda cobrará cada vez más fuerza a partir de que “Enemies” sea igual a 2.
    • Región de muerte: entrará en escena en cualquier momento de las pistas anteriores si la vida llega a 0.
    • Todas las pistas menos la que empieza en el marcador “Death” tienen un filtro de paso bajo que se aplica con más intensidad cuanta menor sea el valor de “Health”. Además, se incrementará el volumen de la pista “Heartbeat”, que hará sonar latidos de corazón para generar tensión.
    • Disparo: En una nota menos importante, ya que no tiene que ver con la composición musical, se puede destacar el sonido de disparo, que funciona como un evento de FMOD Studio que es llamado desde los enemigos de la escena cuando éstos atacan al usuario.

## Resultado Final
Tras la implementación de FMOD Studio, se ha conseguido hacer un pequeño prototipo en Unity que aplica la música adaptativa en un entorno 3D.
[Video y ejecutable adjuntos en la entrega del proyecto]

## Posibles Mejoras/Avances
A nivel del proyecto, posibles avances que se pueden hacer sobre él son, sobre todo, desarrollar el entorno con más elementos que permitan añadir más adaptabilidad a la música (coberturas, “spawns” de enemigos, etc,). Además, se puede mejorar la composición de
manera que el cambio entre regiones de bucle de FMOD Studio no tenga que esperar a saltar a otra región cuando varíe un parámetro.

## Herramientas
    • Reaper
        ◦ Sitala
        ◦ Kontakt
        ◦ Spitfire Discover
        ◦ ReaDelay
    • FMOD Studio
    • Unity