# Sistema de Control de Micrófono en Sala de Conferencias

Este es un sistema de control de micrófono para una sala de conferencias, implementado utilizando semáforos en Python. Permite que los asistentes utilicen los micrófonos para hacer preguntas al orador, asegurando que solo un micrófono esté activo a la vez para evitar confusiones.


Descripción del Problema

En una sala de conferencias, los asistentes desean utilizar los micrófonos para hacer preguntas al orador. Sin embargo, solo se permite un micrófono activo a la vez para evitar confusiones.


Solución Implementada

Utilizamos semáforos para controlar el acceso a los micrófonos, permitiendo que un asistente hable a la vez. Se implementa un semáforo para controlar el acceso al micrófono, otro semáforo para contar el número de asistentes que desean hablar y un tercero para sincronizar la salida de los asistentes que han hecho sus preguntas.


Funcionamiento del Código

El código está escrito en Python y utiliza la biblioteca `threading` para simular tanto a los asistentes como al orador. Cada asistente es un hilo (thread) que solicita acceso al micrófono, hace su pregunta y luego libera el micrófono. El orador, también representado como un hilo, responde a las preguntas de los asistentes.


