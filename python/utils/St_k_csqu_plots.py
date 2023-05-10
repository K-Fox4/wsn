import numpy as np
import matplotlib.pyplot as plt
import math

from python.k_coverage import *
from python.constants import calculate_stochastic_rs_min


def number_of_square_tiles_for_square_field(sensing_radius: int = 25, field_width: int = 250) -> float:
    sections = field_width/sensing_radius
    result = sections * sections
    return result


def plot_lambda_vs_k() -> None:

    k = range(3, 10, 1)
    alpha = 4
    beta = 0.025

    # planar_sensor_density = (0.734 * k)/(sensing_radius * sensing_radius)

    planar_sensor_density_7 = []
    planar_sensor_density_8 = []
    planar_sensor_density_9 = []

    for k_val in k:
        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.7)
        planar_sensor_density_7.append((0.734 * k_val) / (sensing_radius * sensing_radius))

        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.8)
        planar_sensor_density_8.append((0.734 * k_val) / (sensing_radius * sensing_radius))

        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.9)
        planar_sensor_density_9.append((0.734 * k_val) / (sensing_radius * sensing_radius))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(k, planar_sensor_density_7, 'r-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.7')
    plt.plot(k, planar_sensor_density_8, 'g-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.8')
    plt.plot(k, planar_sensor_density_9, 'b-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.9')

    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)

    plt.legend(fontsize=20)

    plt.title(r'$\alpha$=4', fontsize=20, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=20, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda^*)$', fontsize=20, fontweight='bold')

    plt.xlim(xmin=3, xmax=9)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_k_vs_active_sensors() -> None:

    k = range(3, 10, 1)
    alpha = 4
    beta = 0.025

    active_sensors_7 = []
    active_sensors_8 = []
    active_sensors_9 = []

    for k_val in k:
        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.7)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_7.append(square_tiles * k_val)

        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.8)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_8.append(square_tiles * k_val)

        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=0.9)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_9.append(square_tiles * k_val)

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(active_sensors_7, k, 'r-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.7')
    plt.plot(active_sensors_8, k, 'g-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.8')
    plt.plot(active_sensors_9, k, 'b-', marker='s', linewidth=3, markersize=12, label=r'$p_{th}$=0.9')

    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)

    plt.legend(fontsize=20)

    plt.title(r'$\alpha$=4', fontsize=20, fontweight='bold')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=20, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=20, fontweight='bold')

    plt.ylim(ymin=3, ymax=9)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_beta() -> None:

    k = 3
    alpha = 4
    beta = 0.005

    active_sensors_7 = []
    active_sensors_8 = []
    active_sensors_9 = []
    beta_l = []

    while beta <= 0.5:

        beta_l.append(beta)

        sensing_radius = calculate_stochastic_rs_min(k=k, alpha=alpha, beta=beta, pth=0.7)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_7.append(square_tiles * k)

        sensing_radius = calculate_stochastic_rs_min(k=k, alpha=alpha, beta=beta, pth=0.8)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_8.append(square_tiles * k)

        sensing_radius = calculate_stochastic_rs_min(k=k, alpha=alpha, beta=beta, pth=0.9)
        square_tiles = number_of_square_tiles_for_square_field(sensing_radius=sensing_radius,
                                                               field_width=100)
        active_sensors_9.append(square_tiles * k)

        beta += 0.005

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(beta_l, active_sensors_7, 'r-', marker='s', linewidth=2, markersize=4, label=r'$p_{th}$=0.7')
    plt.plot(beta_l, active_sensors_8, 'g-', marker='s', linewidth=2, markersize=4, label=r'$p_{th}$=0.8')
    plt.plot(beta_l, active_sensors_9, 'b-', marker='s', linewidth=2, markersize=4, label=r'$p_{th}$=0.9')

    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)

    plt.legend(fontsize=20)

    plt.title(r'$\alpha$=4 and $\it{k}$=3', fontsize=20, fontweight='bold')
    plt.xlabel(r'Sensor characteristics $(\beta)$', fontsize=20, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=20, fontweight='bold')

    plt.xlim(xmin=0, xmax=0.5)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_k_for_square_and_triangle() -> None:
    k = range(3, 9, 1)
    alpha = 2
    beta = 0.025
    pth = 0.7

    # planar_sensor_density = (0.734 * k)/(sensing_radius * sensing_radius)

    square_simulation = []
    triangle_simulation = []

    for k_val in k:
        sensing_radius = calculate_stochastic_rs_min(k=k_val, alpha=alpha, beta=beta, pth=pth)
        square_simulation.append((0.734 * k_val) / (sensing_radius * sensing_radius))
        triangle_simulation.append((0.814 * k_val) / (sensing_radius * sensing_radius))

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(k, square_simulation, 'r-', marker='s', linewidth=3, markersize=12, label=r'St-$\it{k}$-CSqu')
    plt.plot(k, triangle_simulation, 'g-', marker='^', linewidth=3, markersize=12, label=r'$SCP_k$')

    ax.tick_params(axis='both', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'$\alpha$=2 and $p_{th}$=0.7', fontsize=15, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=3, xmax=8)
    plt.ylim(ymin=0)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


if __name__ == '__main__':
    plot_lambda_vs_k()
    # plot_k_vs_active_sensors()
    # plot_active_sensors_vs_beta()
    # plot_lambda_vs_k_for_square_and_triangle()
