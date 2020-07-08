# tellmeyourwifi
Aplicación que muestra las redes WiFi y sus contraseñas, guardadas en un ordenador Windows. Se debe ejecutar con un usuario administrador.

Sencilla aplicación creada en Python que nos muestra las redes WiFi guardadas en un ordenador Windows, así como sus contraseñas. 

También podemos realizar una búsqueda más detallada utilizando los parámetros -t o --target. 

Por ejemplo, para ver todas las redes WiFi guardadas en el equipo:

    python.exe tellmeyourwifi.py

O para ver todas las redes WiFi guardadas en el equipo que contengan la cadena "bar".

    python.exe tellmeyourwifi.py --target bar
