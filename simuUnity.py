from views import Terrain
from models import TerrainContinu, Robot, Polygone, Serializer
from controllers import StrategieAvancerDroit, StrategieTourner, StrategiePolygone
import threading
import time
import sys
import socket

stop_thread = True


def unity(robot, s, conn, fps):
    while stop_thread:
        while True:
            data = conn.recv(1024)
            if not data:
                time.sleep(1./fps)
                continue
            break

        robot_s = Serializer.serialize(robot).encode()
        conn.send(robot_s)
        time.sleep(1./fps)

    conn.send(b"ok")
    s.close()


def updateStrats(stratavance, fps):
    stratavance.start()
    while not stratavance.stop():
        stratavance.step()
        time.sleep(1./fps)
    global stop_thread
    stop_thread = False


def updateRobot(robot, tc, fps):
    while stop_thread:
        robot.update(tc)
        time.sleep(1./fps)


def run(cote):
    tc = TerrainContinu.Carre(20)
    tc_s = Serializer.serialize(tc).encode()

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432
    fps = 60

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            time.sleep(1./fps)
            continue
        break

    conn.send(tc_s)

    robot = Robot.Robot(-3, -3, 0., 0.)
    startAvancer = StrategieAvancerDroit.StrategieAvancerDroit(robot, 7., 15.)
    startTourner = StrategieTourner.StrategieTourner(robot, 0., 0.)
    stratPolygone = StrategiePolygone.StrategiePolygone(
        startAvancer, startTourner, int(cote))
    t1 = threading.Thread(target=unity, args=(robot, s, conn, fps))
    t2 = threading.Thread(target=updateStrats, args=(stratPolygone, fps))
    t3 = threading.Thread(target=updateRobot, args=(robot, tc, fps))
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    run(sys.argv[1])
