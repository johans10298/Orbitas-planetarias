'''
*Universidad Sergio Arboleda
*Autor: Johan David Villalba Rodriguez
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:johan.villalba01@gmail.com
'''
import time
import cy_simulator
import simulator


def run_simulator(simulator):
    AU = (149.6e6 * 1000)
    sun = simulator.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = simulator.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000

    venus = simulator.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    simulator.loop([sun, earth, venus])


def main():
    start = time.time()
    run_simulator(simulator)
    total_time = time.time() - start

    start = time.time()
    run_simulator(cy_simulator)
    cy_total_time = time.time() - start

    speedUp = round(total_time/cy_total_time, 3)
    print(f"Python time: {total_time} \n")
    print(f"Cython time: {cy_total_time} \n")
    print(f"SpeedUp: {speedUp} \n")


if __name__ == '__main__':
    main()