#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 20/07/2019
# Tellmeyourwifi.py por Misael Aranda Téllez (misael_aranda@hotmail.com).
# Con esta aplicación podremos ver las redes wifi guardadas en un ordenador
# con Windows, así como sus contraseñas.

import os, time, argparse, glob
from xml.dom import minidom

# Definición de colores.
G, B, R, W, M, C, end = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m'
info = end + W + "[-]" + W
good = end + G + "[+]" + W
bad = end + R + "[!]" + W

def cabecera():

    print(G,'''
 _____    _ _                                                      _  __ _
|_   _|  | | |                                                    (_)/ _(_)
  | | ___| | |  _ __ ___   ___   _   _  ___  _   _ _ __  __      ___| |_ _
  | |/ _ \ | | | '_ ` _ \ / _ \ | | | |/ _ \| | | | '__| \ \ /\ / / |  _| |
  | |  __/ | | | | | | | |  __/ | |_| | (_) | |_| | |     \ V  V /| | | | |
  \_/\___|_|_| |_| |_| |_|\___|  \__, |\___/ \__,_|_|      \_/\_/ |_|_| |_|
                                  __/ |
                                 |___/
                                                                    v 1.0

    ''',W)

def leerxml(nombrexml):
    # Extrae los datos de los XML y los muestra en pantalla.
    if args.target == None:
        try:
            # Redes WiFi con contraseña.
            doc = minidom.parse(nombrexml)
            ssid = doc.getElementsByTagName('name')[0].firstChild.data
            password = doc.getElementsByTagName('keyMaterial')[0].firstChild.data
            print(good + ' {0:30} : {1} '.format(ssid, password))
            exito = True
            return exito
        except:
            # Redes WiFi sin contraseña.
            print(bad + ' {0:30} : - - - - - -'.format(ssid))
            exito = False
            return exito
    else:
        try:
            # Redes WiFi con contraseña.
            doc = minidom.parse(nombrexml)
            ssid = doc.getElementsByTagName('name')[0].firstChild.data
            if ssid.lower().find(args.target.lower()) != -1:
                password = doc.getElementsByTagName('keyMaterial')[0].firstChild.data
                print(good + ' {0:30} : {1} '.format(ssid, password))
                exito = True
            else:
                exito = None
            return exito
        except:
            # Redes WiFi sin contraseña.
            print(bad + ' {0:30} : - - - - - -'.format(ssid))
            exito = False
            return exito

# Inicio.
if __name__ == '__main__':
    # Borra la pantalla y muestra cabecera.
    os.system('cls')
    cabecera()

    # Ayuda y parámetros.
    parser = argparse.ArgumentParser(prog='tellmeyourwifi.py')
    parser.add_argument('-t', '--target', help='name of the WiFi network you are looking for')
    args = parser.parse_args()

    # Se crea la carpeta "profiles" si es necesario.
    directorioinicial = os.getcwd()
    if not os.path.exists('profiles'):
        os.mkdir('profiles')
    os.chdir('profiles')

    # Se eliminan los archivos XML si los hubiera.
    for archivo in os.listdir():
        os.remove(archivo)

    # Se crean los archivos XML con las información de las redes WiFi.
    print(info + 'Extrayendo información. Un momento, por favor.\n\n')
    os.popen('netsh wlan export profile key=clear')

    # Dado que el tiempo que se tarda en crear los XML dependerá de la cantidad
    # de redes WiFi que haya en el equipo escaneado, he creado esta rutina
    # para que el flujo del programa no continue hasta que esté todos los
    # XML creados.
    descarga = 0
    time.sleep(1)
    while len(glob.glob(directorioinicial + '/profiles/*.*')) != descarga:
        descarga = len(glob.glob(directorioinicial + '/profiles/*.*'))
        time.sleep(1)

    # Se pasan los datos a la función leerxml para que extraiga los datos
    # y nos dice si ha encontrado la contraseña de la red o no.
    totalredes = 0
    conpassword = 0
    sinpassword = 0
    for xml in os.listdir():
        totalredes = totalredes + 1
        resultado = leerxml(xml)
        if resultado == True:
            conpassword = conpassword + 1
        elif resultado == False:
            sinpassword = sinpassword + 1

    # Se muestran el resumen de los resultados obtenidos.
    print('\n')
    print(info + ' Total redes WiFi encontradas:                 ' + str(totalredes))
    if args.target != None:
        print(info + ' Total redes WiFi según criterios del usuario: ' + str(conpassword + sinpassword))
    print(info + ' Redes WiFi con contraseña:                    ' + str(conpassword))
    print(info + ' Redes Wifi sin contraseña:                    ' + str(sinpassword))

    # Se eliminan los archivos XML.
    for archivo in os.listdir():
        os.remove(archivo)
    os.chdir(directorioinicial)
    os.rmdir('profiles')

    # Finaliza el programa.
    exit(-1)