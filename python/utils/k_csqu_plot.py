import numpy as np
import matplotlib.pyplot as plt
import math


def number_of_square_tiles_for_square_field(sensing_radius: int = 25, field_width: int = 250) -> int:
    sections = field_width//sensing_radius
    result = sections * sections
    return result


def equivalent_circle_radius(square_field_width: int = 250) -> float:
    square_area = square_field_width * square_field_width
    circle_radius = math.sqrt(square_area/math.pi)
    return round(circle_radius, 2)


def plot_lambda_vs_k(sensing_radius: int = 25) -> None:

    k = np.arange(1, 9, 1)
    planar_sensor_density = (0.734 * k)/(sensing_radius * sensing_radius)

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )
    calculated_sensor_density = (square_tiles * k * 0.76)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()
    ax.set(title=r'$\it{r_s}$ = 25 m',
           xlabel=r'$\it{k}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(k, planar_sensor_density, 'b-', label=r'$\lambda_{theo}$')
    plt.plot(k, calculated_sensor_density, 'r-.', label=r'$\lambda_{sim}$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=1, xmax=8)
    plt.ylim(ymin=0, ymax=0.014)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs(k: int = 3) -> None:

    sensing_radius = np.arange(15, 50, 5)
    planar_sensor_density = (0.734 * k)/(sensing_radius * sensing_radius)

    square_tiles = (250//sensing_radius)**2
    calculated_sensor_density = (square_tiles * k * 0.825)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()
    ax.set(title=r'$\it{k}$ = 3',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(sensing_radius, planar_sensor_density, 'b-', label=r'$\lambda_{theo}$')
    plt.plot(sensing_radius, calculated_sensor_density, 'r-.', label=r'$\lambda_{sim}$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0, ymax=0.014)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_k_for_square_vs_triangle(sensing_radius: int = 25) -> None:

    k = np.arange(1, 9, 1)

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )
    square_sensor_density = (square_tiles * k * 0.76)/(250 * 250)

    triangle_tiles = math.floor(250//(0.5*math.sqrt(3)*sensing_radius))*(2*(250//sensing_radius)+1)
    triangle_sensor_density = (triangle_tiles * k * 0.76)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()
    ax.set(title=r'$\it{r_s}$ = 25 m',
           xlabel=r'$\it{k}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(k, square_sensor_density, 'c--', marker='s', label=r'$\it{k}$-CSqu')
    plt.plot(k, triangle_sensor_density, 'g-.', marker='^', label=r'$DIRACC_k$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=1, xmax=8)
    plt.ylim(ymin=0, ymax=0.030)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs_for_square_vs_triangle(k: int = 3) -> None:

    sensing_radius = np.arange(15, 50, 5)

    square_tiles = (250//sensing_radius)**2
    square_sensor_density = (square_tiles * k * 0.825)/(250 * 250)

    triangle_tiles_list = []
    for radius in sensing_radius:
        triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * radius)) * (2 * (250 // radius) + 1)
        triangle_tiles_list.append(triangle_tiles)

    triangle_sensor_density = []
    for tile_count in triangle_tiles_list:
        sensor_density = (tile_count * k * 0.825) / (250 * 250)
        triangle_sensor_density.append(sensor_density)

    # Create plots
    fig, ax = plt.subplots()
    ax.set(title=r'$\it{k}$ = 3',
           xlabel=r'$\it{r_s}$',
           ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(sensing_radius, square_sensor_density, 'c--', marker='s', label=r'$\it{k}$-CSqu')
    plt.plot(sensing_radius, triangle_sensor_density, 'g-.', marker='^', label=r'$DIRACC_k$')
    plt.legend(fontsize=11)
    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0, ymax=0.03)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


if __name__ == "__main__":
    # plot_lambda_vs_k()
    # plot_lambda_vs_rs()
    plot_lambda_vs_k_for_square_vs_triangle()
    plot_lambda_vs_rs_for_square_vs_triangle()
