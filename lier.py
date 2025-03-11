#!/usr/bin/env python
from rplidar import RPLidar
import time

PORT_NAME = '/dev/ttyUSB0'

def run():
    # Création de l'instance RPLidar
    lidar = RPLidar(PORT_NAME)
    
    print('Connecté sur le port:', PORT_NAME)
    print('Informations sur le LIDAR :')
    print(lidar.get_info())
    print('État du LIDAR :')
    print(lidar.get_health())
    
    try:
        # Itération sur les scans en continu
        for scan in lidar.iter_scans():
            # Chaque scan est une liste de tuples (angle, distance, qualité)
            print(scan)
    except KeyboardInterrupt:
        print('Arrêt demandé par l’utilisateur.')
    finally:
        # Arrêt et déconnexion du LIDAR proprement
        lidar.stop()
        lidar.disconnect()

if __name__ == '__main__':
    run()
