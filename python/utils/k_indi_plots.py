import numpy as np
import matplotlib.pyplot as plt
import math

from python.k_coverage import *


def plot_lambda_vs_k(sensing_radius: int = 25, n: int = 5) -> None:
    k = range(3, 10, 1)
    total_coverage_area = (math.pow(sensing_radius, 2)) * (
            math.pi +
            ((math.sqrt(3) * ((3 * math.pow(n, 2)) - (6 * n) + 2)) / (4 * math.pow(n, 2))) -
            ((math.sqrt((4 * math.pow(n, 2)) - 1)) / math.pow(n, 2)) -
            4 * math.asin(1 / (2 * n))
    )

    excluded_total_coverage_area = (math.sqrt(3) * math.pow(sensing_radius, 2) * (
            (6 * math.pow(n, 2)) - (8 * n) + 2)) / (4 * math.pow(n, 2))

    grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    theoretical = []
    simulation = []
    excluded_theoretical = []

    for i in k:
        theoretical.append(i / total_coverage_area)
        simulation.append((grid.total_num_of_tiles * i) / (250 * 250))
        excluded_theoretical.append(i / excluded_total_coverage_area)

    # Create plots
    fig, ax = plt.subplots()
    
    plt.plot(k, theoretical, 'b-', marker='o', linewidth=3, markersize=12, label=r'$\lambda_{theo}$')
    # plt.plot(k, excluded_theoretical, 'g-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{X-theo}$')
    plt.plot(k, simulation, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{sim}$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=3, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs(k: int = 3, n: int = 5) -> None:
    sensing_radius = range(15, 50, 5)

    theoretical = []
    simulation = []
    excluded_theoretical = []

    for sensing_rad in sensing_radius:
        total_coverage_area = (math.pow(sensing_rad, 2)) * (
                math.pi +
                ((math.sqrt(3) * ((3 * math.pow(n, 2)) - (6 * n) + 2)) / (4 * math.pow(n, 2))) -
                ((math.sqrt((4 * math.pow(n, 2)) - 1)) / math.pow(n, 2)) -
                4 * math.asin(1 / (2 * n))
        )

        excluded_total_coverage_area = (math.sqrt(3) * math.pow(sensing_rad, 2) * (
                (6 * math.pow(n, 2)) - (8 * n) + 2)) / (4 * math.pow(n, 2))

        grid = IrregularHexagon1(
            sensing_radius=sensing_rad,
            area_length=250,
            factor=n
        )

        theoretical.append(k / total_coverage_area)
        simulation.append((grid.total_num_of_tiles * k) / (250 * 250))
        excluded_theoretical.append(k / excluded_total_coverage_area)

    # Create plots
    fig, ax = plt.subplots()
    
    plt.plot(sensing_radius, theoretical, 'b-', marker='o', linewidth=3, markersize=12, label=r'$\lambda_{theo}$')
    # plt.plot(sensing_radius, excluded_theoretical, 'g-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{X-theo}$')
    plt.plot(sensing_radius, simulation, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{sim}$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3 & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_n(sensing_radius: int = 25, k: int = 5) -> None:
    n = range(2, 10, 1)

    theoretical = []
    simulation = []
    excluded_theoretical = []

    for n_val in n:
        total_coverage_area = (math.pow(sensing_radius, 2)) * (
                math.pi +
                ((math.sqrt(3) * ((3 * math.pow(n_val, 2)) - (6 * n_val) + 2)) / (4 * math.pow(n_val, 2))) -
                ((math.sqrt((4 * math.pow(n_val, 2)) - 1)) / math.pow(n_val, 2)) -
                4 * math.asin(1 / (2 * n_val))
        )

        excluded_total_coverage_area = (math.sqrt(3) * math.pow(sensing_radius, 2) * (
                (6 * math.pow(n_val, 2)) - (8 * n_val) + 2)) / (4 * math.pow(n_val, 2))

        grid = IrregularHexagon1(
            sensing_radius=sensing_radius,
            area_length=250,
            factor=n_val
        )

        theoretical.append(k / total_coverage_area)
        simulation.append((grid.total_num_of_tiles * k) / (250 * 250))
        excluded_theoretical.append(k / excluded_total_coverage_area)

    # Create plots
    fig, ax = plt.subplots()
    
    plt.plot(n, theoretical, 'b-', marker='o', linewidth=3, markersize=12, label=r'$\lambda_{theo}$')
    # plt.plot(n, excluded_theoretical, 'g-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{X-theo}$')
    plt.plot(n, simulation, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\lambda_{sim}$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3 & Sensing Radius $(\it{r_s})$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'$\it{n}$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=2, xmax=8)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens(sensing_radius: int = 25, n: int = 5) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    active_sensors_3 = [grid.total_num_of_tiles * 3 for _ in range(len(deployed_sensors))]
    active_sensors_4 = [grid.total_num_of_tiles * 4 for _ in range(len(deployed_sensors))]
    active_sensors_5 = [grid.total_num_of_tiles * 5 for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, active_sensors_3, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$ = 3')
    plt.plot(deployed_sensors, active_sensors_4, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$ = 4')
    plt.plot(deployed_sensors, active_sensors_5, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$ = 5')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=250, ymax=650)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens_2(k: int = 3, n: int = 5) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    grid_20 = IrregularHexagon1(
        sensing_radius=20,
        area_length=250,
        factor=n
    )

    grid_25 = IrregularHexagon1(
        sensing_radius=25,
        area_length=250,
        factor=n
    )

    grid_30 = IrregularHexagon1(
        sensing_radius=30,
        area_length=250,
        factor=n
    )

    active_sensors_20 = [grid_20.total_num_of_tiles * k for _ in range(len(deployed_sensors))]
    active_sensors_25 = [grid_25.total_num_of_tiles * k for _ in range(len(deployed_sensors))]
    active_sensors_30 = [grid_30.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, active_sensors_20, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 20 m')
    plt.plot(deployed_sensors, active_sensors_25, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 25 m')
    plt.plot(deployed_sensors, active_sensors_30, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 30 m')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Degree of Coverage $\it{k}$ = 3 & $\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=100, ymax=500)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens_3(sensing_radius: int = 25, k: int = 5) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    grid_3 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=3
    )

    grid_5 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=5
    )

    grid_7 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=7
    )

    active_sensors_3 = [grid_3.total_num_of_tiles * k for _ in range(len(deployed_sensors))]
    active_sensors_5 = [grid_5.total_num_of_tiles * k for _ in range(len(deployed_sensors))]
    active_sensors_7 = [grid_7.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, active_sensors_3, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 3')
    plt.plot(deployed_sensors, active_sensors_5, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 5')
    plt.plot(deployed_sensors, active_sensors_7, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 7')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Degree of Coverage $\it{k}$ = 3 & Sensing Radius $(\it{r_s})$ = 25 m', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=100, ymax=500)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_k(n: int = 5):

    k = [1, 2, 3, 4, 5, 6, 7, 8]

    grid_20 = IrregularHexagon1(
        sensing_radius=20,
        area_length=250,
        factor=n
    )

    grid_25 = IrregularHexagon1(
        sensing_radius=25,
        area_length=250,
        factor=n
    )

    grid_30 = IrregularHexagon1(
        sensing_radius=30,
        area_length=250,
        factor=n
    )

    active_sensors_20 = []
    active_sensors_25 = []
    active_sensors_30 = []

    for degree in k:
        active_sensors_20.append(grid_20.total_num_of_tiles * degree)
        active_sensors_25.append(grid_25.total_num_of_tiles * degree)
        active_sensors_30.append(grid_30.total_num_of_tiles * degree)

    fig, ax = plt.subplots()

    plt.plot(active_sensors_20, k, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 20 m')
    plt.plot(active_sensors_25, k, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 25 m')
    plt.plot(active_sensors_30, k, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 30 m')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='lower right')
    plt.title(r'$\it{n}$ = 5', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=1, ymax=8)
    plt.xlim(xmin=0)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_k_2(sensing_radius: int = 25):

    k = [1, 2, 3, 4, 5, 6, 7, 8]

    grid_3 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=3
    )

    grid_5 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=5
    )

    grid_7 = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=7
    )

    active_sensors_3 = []
    active_sensors_5 = []
    active_sensors_7 = []

    for degree in k:
        active_sensors_3.append(grid_3.total_num_of_tiles * degree)
        active_sensors_5.append(grid_5.total_num_of_tiles * degree)
        active_sensors_7.append(grid_7.total_num_of_tiles * degree)

    fig, ax = plt.subplots()

    plt.plot(active_sensors_3, k, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 3')
    plt.plot(active_sensors_5, k, 'b-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 5')
    plt.plot(active_sensors_7, k, 'r-', marker='h', linewidth=3, markersize=12, label=r'$\it{n}$ = 7')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='lower right')
    plt.title(r'Sensing Radius $(\it{r_s})$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=1, ymax=8)
    plt.xlim(xmin=0)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_k_for_hexagon_and_triangle(sensing_radius: int = 25, n: int = 5) -> None:
    k = range(3, 10, 1)

    hexagon_grid = IrregularHexagon1(
        sensing_radius=sensing_radius,
        area_length=250,
        factor=n
    )

    hexagon_simulation = []

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )
    triangle_simulation = []

    for i in k:
        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * i) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * i) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(k, hexagon_simulation, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
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
    triangle_simulation = []

    for sensing_rad in sensing_radius:
        hexagon_grid = IrregularHexagon1(
            sensing_radius=sensing_rad,
            area_length=250,
            factor=n
        )

        triangle_grid = ReuleauxTriangle(
            sensing_radius=sensing_rad,
            area_length=250
        )

        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * k) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * k) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()
    
    plt.plot(sensing_radius, hexagon_simulation, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
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

    for n_val in n:

        hexagon_grid = IrregularHexagon1(
            sensing_radius=sensing_radius,
            area_length=250,
            factor=n_val
        )

        hexagon_simulation.append((hexagon_grid.total_num_of_tiles * k) / (250 * 250))
        triangle_simulation.append((triangle_grid.total_num_of_tiles * k) / (250 * 250))

    # Create plots
    fig, ax = plt.subplots()
    
    plt.plot(n, hexagon_simulation, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
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

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    triangle_active_sensors = [triangle_grid.total_num_of_tiles * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, hexagon_active_sensors, 'c-', linewidth=3, markersize=12, marker='h', label=r'$\it{k}$-InDi')
    plt.plot(deployed_sensors, triangle_active_sensors, 'g-', linewidth=3, markersize=12, marker='^', label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m, Degree of Coverage $\it{k}$ = 3 & $\it{n}$ = 5', fontsize=15, fontweight='bold')
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

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    hexagon_active_sensors = []
    triangle_active_sensors = []

    for degree in k:
        hexagon_active_sensors.append(hexagon_grid.total_num_of_tiles * degree)
        triangle_active_sensors.append(triangle_grid.total_num_of_tiles * degree)

    fig, ax = plt.subplots()

    plt.plot(hexagon_active_sensors, k, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi')
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
    hexagon_active_sensors_2 = [hexagon_grid.total_num_of_tiles * 2 for _ in range(len(rc))]
    hexagon_active_sensors_4 = [hexagon_grid.total_num_of_tiles * 4 for _ in range(len(rc))]

    triangle_grid = ReuleauxTriangle(
        sensing_radius=sensing_radius,
        area_length=250
    )

    triangle_active_sensors_2 = [triangle_grid.total_num_of_tiles * 2 for _ in range(len(rc))]
    triangle_active_sensors_3 = [triangle_grid.total_num_of_tiles * 3 for _ in range(len(rc))]
    triangle_active_sensors_4 = [triangle_grid.total_num_of_tiles * 4 for _ in range(len(rc))]

    fig, ax = plt.subplots()

    plt.plot(rc, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(rc, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(rc, triangle_active_sensors_2, 'b-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 2')
    plt.plot(rc, hexagon_active_sensors_4, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 4')
    plt.plot(rc, hexagon_active_sensors_3, 'g-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 3')
    plt.plot(rc, hexagon_active_sensors_2, 'm-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 2')

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

    hexagon_active_sensors_2 = []
    hexagon_active_sensors_3 = []
    hexagon_active_sensors_4 = []
    triangle_active_sensors_4 = []
    triangle_active_sensors_3 = []
    triangle_active_sensors_2 = []

    for radius in sensing_radius:
        hexagon_grid = IrregularHexagon1(
            sensing_radius=radius,
            area_length=250,
            factor=n
        )

        triangle_grid = ReuleauxTriangle(
            sensing_radius=radius,
            area_length=250
        )

        hexagon_active_sensors_2.append(hexagon_grid.total_num_of_tiles * 2)
        hexagon_active_sensors_3.append(hexagon_grid.total_num_of_tiles * k)
        hexagon_active_sensors_4.append(hexagon_grid.total_num_of_tiles * 4)

        triangle_active_sensors_4.append(triangle_grid.total_num_of_tiles * 4)
        triangle_active_sensors_3.append(triangle_grid.total_num_of_tiles * k)
        triangle_active_sensors_2.append(triangle_grid.total_num_of_tiles * 2)

    fig, ax = plt.subplots()

    plt.plot(sensing_radius, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(sensing_radius, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(sensing_radius, triangle_active_sensors_2, 'b-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 2')
    plt.plot(sensing_radius, hexagon_active_sensors_4, 'c-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 4')
    plt.plot(sensing_radius, hexagon_active_sensors_3, 'g-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 3')
    plt.plot(sensing_radius, hexagon_active_sensors_2, 'm-', marker='h', linewidth=3, markersize=12, label=r'$\it{k}$-InDi, $\it{k}$ = 2')

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
    # plot_lambda_vs_k()
    # plot_lambda_vs_rs()
    plot_lambda_vs_n()
    # plot_active_sens_vs_deployed_sens()
    # plot_active_sens_vs_deployed_sens_2()
    # plot_active_sens_vs_deployed_sens_3()
    # plot_active_sensors_vs_k()
    # plot_active_sensors_vs_k_2()
    # plot_lambda_vs_k_for_hexagon_and_triangle()
    # plot_lambda_vs_rs_for_hexagon_and_triangle()
    # plot_lambda_vs_n_for_hexagon_and_triangle()
    # plot_active_sens_vs_deployed_sens_for_hexagon_vs_triangle()
    # plot_active_sensors_vs_k_for_hexagon_vs_triangle()
    # plot_active_sens_vs_rc_for_hexagon_vs_triangle()
    # plot_active_sens_vs_rs_for_hexagon_vs_triangle()
    # for n_val in range(2, 25):
    #     value = (
    #             math.pi +
    #             ((math.sqrt(3) * ((3 * math.pow(n_val, 2)) - (6 * n_val) + 2)) / (4 * math.pow(n_val, 2))) -
    #             ((math.sqrt((4 * math.pow(n_val, 2)) - 1)) / math.pow(n_val, 2)) -
    #             4 * math.asin(1 / (2 * n_val))
    #     )

    #     excluded_value = (2 * math.pow(n_val, 2))/(math.sqrt(3) * (n_val - 1) * ((3 * n_val) - 1))

    #     print(f"For n = {n_val}, the value is {round(1/value, 4)} and the excluded value is {round(excluded_value, 4)}")
