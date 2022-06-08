import numpy as np
import matplotlib.pyplot as plt
import math

from python.k_coverage import *


def plot_lambda_vs_k(sensing_radius: int = 25, n: int = 5) -> None:
    k = range(2, 9, 1)
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
    ax.set(title=r'$\it{r_s}$ = 25 m and $\it{n}$ = 5',
           xlabel=r'$\it{k}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(k, theoretical, 'b-', label=r'$\lambda_{theo}$')
    plt.plot(k, excluded_theoretical, 'g--', label=r'$\lambda_{theoX}$')
    plt.plot(k, simulation, 'r-.', label=r'$\lambda_{sim}$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=2, xmax=8)
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
    ax.set(title=r'$\it{k}$ = 3 and $\it{n}$ = 5',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(sensing_radius, theoretical, 'b-', label=r'$\lambda_{theo}$')
    plt.plot(sensing_radius, excluded_theoretical, 'g--', label=r'$\lambda_{theoX}$')
    plt.plot(sensing_radius, simulation, 'r-.', label=r'$\lambda_{sim}$')
    plt.legend(fontsize=11)
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
    ax.set(title=r'$\it{k}$ = 3 and $\it{r_s}$ = 25 m',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(n, theoretical, 'b-', label=r'$\lambda_{theo}$')
    plt.plot(n, excluded_theoretical, 'g--', label=r'$\lambda_{theoX}$')
    plt.plot(n, simulation, 'r-.', label=r'$\lambda_{sim}$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=2, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_k_for_hexagon_and_triangle(sensing_radius: int = 25, n: int = 5) -> None:
    k = range(2, 9, 1)

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
    ax.set(title=r'$\it{r_s}$ = 25 m and $\it{n}$ = 5',
           xlabel=r'$\it{k}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(k, hexagon_simulation, 'c--', marker='h', label=r'$\it{k}$-InDi')
    plt.plot(k, triangle_simulation, 'g-.', marker='^', label=r'$DIRACC_k$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=2, xmax=8)
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
    ax.set(title=r'$\it{k}$ = 3 and $\it{n}$ = 5',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(sensing_radius, hexagon_simulation, 'c--', marker='h', label=r'$\it{k}$-InDi')
    plt.plot(sensing_radius, triangle_simulation, 'g-.', marker='^', label=r'$DIRACC_k$')
    plt.legend(fontsize=11)
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
    ax.set(title=r'$\it{k}$ = 3 and $\it{r_s}$ = 25 m',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(n, hexagon_simulation, 'c--', marker='h', label=r'$\it{k}$-InDi')
    plt.plot(n, triangle_simulation, 'g-.', marker='^', label=r'$DIRACC_k$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=2, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


if __name__ == "__main__":
    # plot_lambda_vs_k()
    # plot_lambda_vs_rs()
    # plot_lambda_vs_n()
    # plot_lambda_vs_k_for_hexagon_and_triangle()
    # plot_lambda_vs_rs_for_hexagon_and_triangle()
    plot_lambda_vs_n_for_hexagon_and_triangle()
