import numpy as np
import matplotlib.pyplot as plt
import math

from python.k_coverage import *


def plot_lambda_vs_k_for_hexagon_and_triangle(sensing_radius: int = 25, n: int = 5) -> None:
    k = range(3, 10, 1)

    hexagon_grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    hexagon_simulation = []

    square_grid = Square(
        sensing_radius=sensing_radius,
        area_length=250,
    )

    square_simulation = []

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )
    triangle_simulation = []

    for i in k:
        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * i) / (250 * 250))
        square_simulation.append((square_grid.total_num_of_tiles * i) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * i) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(k, hexagon_simulation, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
    plt.plot(k, square_simulation, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(k, triangle_simulation, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=3, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs_for_hexagon_and_triangle(k: int = 3, n: int = 5) -> None:
    sensing_radius = range(15, 50, 5)

    hexagon_simulation = []
    square_simulation = []
    triangle_simulation = []

    for sensing_rad in sensing_radius:
        hexagon_grid = IrregularHexagon1(
            sensing_radius=sensing_rad,
            area_length=250,
            factor=n
        )

        square_grid = Square(
            sensing_radius=sensing_rad,
            area_length=250,
        )

        triangle_grid = ReuleauxTriangle(
            sensing_radius=sensing_rad,
            area_length=250
        )

        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * k) / (250 * 250))
        square_simulation.append((square_grid.total_num_of_tiles * k) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * k) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(sensing_radius, hexagon_simulation, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
    plt.plot(sensing_radius, square_simulation, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(sensing_radius, triangle_simulation, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3 & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_n_for_hexagon_and_triangle(sensing_radius: int = 25, k: int = 5) -> None:
    n = range(2, 10, 1)

    hexagon_simulation = []

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    triangle_simulation = []

    square_grid = Square(
        sensing_radius=sensing_radius,
        area_length=250,
    )

    square_simulation = []

    for n_val in n:
        hexagon_grid = IrregularHexagon1(
            sensing_radius=sensing_radius,
            area_length=250,
            factor=n_val
        )

        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * k) / (250 * 250))
        square_simulation.append((square_grid.total_num_of_tiles * k) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * k) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(n, hexagon_simulation, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
    plt.plot(n, square_simulation, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(n, triangle_simulation, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3 & Sensing Radius $(\it{r_s})$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'$\it{n}$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=2, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens_for_hexagon_vs_triangle(n: int = 5, sensing_radius: int = 25, k: int = 3) -> None:
    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    hexagon_grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    hexagon_active_sensors = [hexagon_grid.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    square_grid = Square(
        sensing_radius=sensing_radius,
        area_length=250,
    )

    square_active_sensors = [square_grid.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    triangle_active_sensors = [triangle_grid.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, hexagon_active_sensors, 'b-', linewidth=3, markersize=12, marker='h',
             label=r'$\it{k}$-InDi')
    plt.plot(deployed_sensors, square_active_sensors, 'r-', linewidth=3, markersize=12, marker='s',
             label=r'$\it{k}$-CSqu')
    plt.plot(deployed_sensors, triangle_active_sensors, 'g-', linewidth=3, markersize=12, marker='^',
             label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m, Degree of Coverage $\it{k}$ = 3 & $\it{n}$ = 5', fontsize=15,
              fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=100, ymax=400)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_k_for_hexagon_vs_triangle(n: int = 5, sensing_radius: int = 25, k: int = 3):
    k = [1, 2, 3, 4, 5, 6, 7, 8]

    hexagon_grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    square_grid = Square(
        sensing_radius=sensing_radius,
        area_length=250,
    )

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    hexagon_active_sensors = []
    square_active_sensors = []
    triangle_active_sensors = []

    for degree in k:
        hexagon_active_sensors.append(hexagon_grid.total_num_of_tiles * degree)
        square_active_sensors.append(square_grid.total_num_of_tiles * degree)
        triangle_active_sensors.append(triangle_grid.total_num_of_tiles * degree)

    fig, ax = plt.subplots()

    plt.plot(hexagon_active_sensors, k, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
    plt.plot(square_active_sensors, k, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(triangle_active_sensors, k, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=1, ymax=8)
    plt.xlim(xmin=0)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_rc_for_hexagon_vs_triangle(n: int = 5, sensing_radius: int = 25, k: int = 3) -> None:
    rc = range(50, 155, 5)

    hexagon_grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    hexagon_active_sensors_3 = [hexagon_grid.total_num_of_tiles * k for _ in range(len(rc))]
    # hexagon_active_sensors_2 = [hexagon_grid.total_num_of_tiles * 2 for _ in range(len(rc))]
    hexagon_active_sensors_4 = [hexagon_grid.total_num_of_tiles * 4 for _ in range(len(rc))]

    square_grid = Square(
        sensing_radius=sensing_radius,
        area_length=250,
    )

    square_active_sensors_3 = [square_grid.total_num_of_tiles * 3 for _ in range(len(rc))]
    square_active_sensors_4 = [square_grid.total_num_of_tiles * 4 for _ in range(len(rc))]

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    # triangle_active_sensors_2 = [triangle_grid.total_num_of_tiles * 2 for _ in range(len(rc))]
    triangle_active_sensors_3 = [triangle_grid.total_num_of_tiles * 3 for _ in range(len(rc))]
    triangle_active_sensors_4 = [triangle_grid.total_num_of_tiles * 4 for _ in range(len(rc))]

    fig, ax = plt.subplots()

    plt.plot(rc, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12,
             label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(rc, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12,
             label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(rc, square_active_sensors_4, 'b-', marker='s', linewidth=3, markersize=12,
             label=r'$\it{k}$-CSqu, $\it{k}$ = 4')
    plt.plot(rc, square_active_sensors_3, 'm-', marker='s', linewidth=3, markersize=12,
             label=r'$\it{k}$-CSqu, $\it{k}$ = 3')
    plt.plot(rc, hexagon_active_sensors_4, 'c-', marker='h', linewidth=3, markersize=12,
             label=r'$\it{k}$-InDi, $\it{k}$ = 4')
    plt.plot(rc, hexagon_active_sensors_3, 'g-', marker='h', linewidth=3, markersize=12,
             label=r'$\it{k}$-InDi, $\it{k}$ = 3')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Communication Radius $(\it{r_c})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=100)
    plt.xlim(xmin=50, xmax=150)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_rs_for_hexagon_vs_triangle(n: int = 5, k: int = 3) -> None:
    sensing_radius = np.arange(15, 75, 5)

    hexagon_active_sensors_3 = []
    hexagon_active_sensors_4 = []
    square_active_sensors_3 = []
    square_active_sensors_4 = []
    triangle_active_sensors_4 = []
    triangle_active_sensors_3 = []

    for radius in sensing_radius:
        hexagon_grid = IrregularHexagon1(
            sensing_radius=radius,
            area_length=250,
            factor=n
        )

        square_grid = Square(
            sensing_radius=radius,
            area_length=250,
        )

        triangle_grid = ReuleauxTriangle(
            sensing_radius=radius,
            area_length=250
        )

        hexagon_active_sensors_3.append(hexagon_grid.total_num_of_tiles * k)
        hexagon_active_sensors_4.append(hexagon_grid.total_num_of_tiles * 4)

        square_active_sensors_3.append(square_grid.total_num_of_tiles * k)
        square_active_sensors_4.append(square_grid.total_num_of_tiles * 4)

        triangle_active_sensors_4.append(triangle_grid.total_num_of_tiles * 4)
        triangle_active_sensors_3.append(triangle_grid.total_num_of_tiles * k)

    fig, ax = plt.subplots()

    plt.plot(sensing_radius, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12,
             label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(sensing_radius, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12,
             label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(sensing_radius, square_active_sensors_4, 'b-', marker='s', linewidth=3, markersize=12,
             label=r'$\it{k}$-CSqu, $\it{k}$ = 4')
    plt.plot(sensing_radius, square_active_sensors_3, 'm-', marker='s', linewidth=3, markersize=12,
             label=r'$\it{k}$-CSqu, $\it{k}$ = 3')
    plt.plot(sensing_radius, hexagon_active_sensors_4, 'c-', marker='h', linewidth=3, markersize=12,
             label=r'$\it{k}$-InDi, $\it{k}$ = 4')
    plt.plot(sensing_radius, hexagon_active_sensors_3, 'g-', marker='h', linewidth=3, markersize=12,
             label=r'$\it{k}$-InDi, $\it{k}$ = 3')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    plt.title(r'$\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=100, ymax=750)
    plt.xlim(xmin=15, xmax=70)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


if __name__ == "__main__":
    # plot_lambda_vs_k_for_hexagon_and_triangle()
    # plot_lambda_vs_rs_for_hexagon_and_triangle()
    # plot_lambda_vs_n_for_hexagon_and_triangle()
    # plot_active_sens_vs_deployed_sens_for_hexagon_vs_triangle()
    # plot_active_sensors_vs_k_for_hexagon_vs_triangle()
    # plot_active_sens_vs_rc_for_hexagon_vs_triangle()
    plot_active_sens_vs_rs_for_hexagon_vs_triangle()

