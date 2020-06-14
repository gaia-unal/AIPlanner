<template>
  <div style="margin-top:80px">
    <h5>AG Planning</h5>
    <p>AG Planning es un editor en línea para crear y ejecutar programas de planificación STRIPS y HTN. Para el planificador STRIPS se utilizó un repositorio de <a href="https://github.com/tansey/strips">Github</a> creado por <a href="https://github.com/tansey">Wesley Tansey</a>.</p>
    <p>El planificador HTN (basado en la implementación de SHOP2 de (Sirin, Parsia, Wu, Hendler, & Nau, 2004)) y el sistema en general, fueron desarrollados por Mauricio Rodriguez Vinasco como Trabajo de Grado en la Universidad Nacional de Colombia sede Manizales.</p>
    <h5>¿Qué es STRIPS?</h5>
    <p>Es un algoritmo de planificación en el que se define una sintaxis para expresar las acciones, compuestas por unas condiciones previas y posteriores, el objetivo a alcanzar, compuesto por varios estados o sub-metas, y una condición o situación inicial, que representa los estados iniciales del problema.</p>
    <p>A partir de lo anterior, el algoritmo toma el objetivo a conseguir y determina que acción debe ejecutar para alcanzarlo, teniendo en cuenta que ésta cumpla con las precondiciones necesarias para su ejecución; al ejecutar una acción, se actualiza el estado actual del problema y se toman nuevas metas a alcanzar.</p>
    <h5>¿Qué es HTN?</h5>
    <p>Es un algoritmo de planificación que se basa en la descomposición jerárquica de tareas, partiendo de un nivel abstracto a un nivel concreto de detalle, para producir una secuencia de acciones que desarrollen alguna actividad o tarea predefinida. Las tareas pueden ser primitivas (directamente ejecutables) y no primitivas (compuestas por mas tareas) (Lekavý & Návrat, 2007). “Estas tareas, junto con otras restricciones se denomina red de tareas” (Lekavý & Návrat, 2007).</p>
    <h5>Aspectos a tener en cuenta</h5>
    <p>Cada que se ejecuta un problema, este se almacena con el nombre que se le indica, esto quiere decir que los problemas con el mismo nombre se sobreescribirán en la base de datos.</p>
    <p>Por otro lado, cada usuario desde el momento de su registro cuenta con dos problemas de prueba, uno de STRIPS y otro de HTN que pueden encontrar en el Tablero, que es el lugar donde se mostrarán todos los problemas creados por el usuario.</p>
    <hr>
    <h5>Bibliografía</h5>
    <p>Lekavý, M., & Návrat, P. (2007). Expressivity of STRIPS-Like and HTN-Like Planning. <a href="https://doi.org/10.1007/978-3-540-72830-6_13">https://doi.org/10.1007/978-3-540-72830-6_13</a></p>
    <p>Sirin, E., Parsia, B., Wu, D., Hendler, J., & Nau, D. (2004). HTN planning for Web Service composition using SHOP2. Journal of Web Semantics, 1(4), 377–396. <a href="https://doi.org/10.1016/J.WEBSEM.2004.06.005">https://doi.org/10.1016/J.WEBSEM.2004.06.005</a></p>
  </div>
</template>
