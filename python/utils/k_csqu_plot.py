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
    calculated_sensor_density = (square_tiles * k)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(k, planar_sensor_density, 'b-', marker='o', linewidth=3, markersize=12, label=r'$\lambda_{theo}$')
    plt.plot(k, calculated_sensor_density, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\lambda_{sim}$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=1, xmax=8)
    plt.ylim(ymin=0, ymax=0.014)
    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs(k: int = 3) -> None:

    sensing_radius = np.arange(15, 50, 5)
    planar_sensor_density = (0.734 * k)/(sensing_radius * sensing_radius)

    square_tiles = (250//sensing_radius)**2
    calculated_sensor_density = (square_tiles * k)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()

    plt.plot(sensing_radius, planar_sensor_density, 'b-', marker='o', linewidth=3, markersize=12, label=r'$\lambda_{theo}$')
    plt.plot(sensing_radius, calculated_sensor_density, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\lambda_{sim}$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0, ymax=0.014)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens(sensing_radius: int = 25) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )

    active_sensors_3 = [square_tiles * 3 for _ in range(len(deployed_sensors))]
    active_sensors_4 = [square_tiles * 4 for _ in range(len(deployed_sensors))]
    active_sensors_5 = [square_tiles * 5 for _ in range(len(deployed_sensors))]
    active_sensors_6 = [square_tiles * 6 for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, active_sensors_3, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$ = 3')
    plt.plot(deployed_sensors, active_sensors_4, 'b-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$ = 4')
    plt.plot(deployed_sensors, active_sensors_5, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$ = 5')
    plt.plot(deployed_sensors, active_sensors_6, 'g-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$ = 6')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=250, ymax=650)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens_2(k: int = 3) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    square_tiles_20 = number_of_square_tiles_for_square_field(
        sensing_radius=20,
        field_width=250
    )

    square_tiles_25 = number_of_square_tiles_for_square_field(
        sensing_radius=25,
        field_width=250
    )

    square_tiles_30 = number_of_square_tiles_for_square_field(
        sensing_radius=30,
        field_width=250
    )

    square_tiles_35 = number_of_square_tiles_for_square_field(
        sensing_radius=35,
        field_width=250
    )

    active_sensors_20 = [square_tiles_20 * k for _ in range(len(deployed_sensors))]
    active_sensors_25 = [square_tiles_25 * k for _ in range(len(deployed_sensors))]
    active_sensors_30 = [square_tiles_30 * k for _ in range(len(deployed_sensors))]
    active_sensors_35 = [square_tiles_35 * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, active_sensors_20, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 20 m')
    plt.plot(deployed_sensors, active_sensors_25, 'b-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 25 m')
    plt.plot(deployed_sensors, active_sensors_30, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 30 m')
    plt.plot(deployed_sensors, active_sensors_35, 'g-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 35 m')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Degree of Coverage $\it{k}$ = 3', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=100, ymax=500)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_k():

    k = [1, 2, 3, 4, 5, 6, 7, 8]

    square_tiles_20 = number_of_square_tiles_for_square_field(
        sensing_radius=20,
        field_width=250
    )

    square_tiles_25 = number_of_square_tiles_for_square_field(
        sensing_radius=25,
        field_width=250
    )

    square_tiles_30 = number_of_square_tiles_for_square_field(
        sensing_radius=30,
        field_width=250
    )

    square_tiles_35 = number_of_square_tiles_for_square_field(
        sensing_radius=35,
        field_width=250
    )

    active_sensors_20 = []
    active_sensors_25 = []
    active_sensors_30 = []
    active_sensors_35 = []

    for degree in k:
        active_sensors_20.append(square_tiles_20 * degree)
        active_sensors_25.append(square_tiles_25 * degree)
        active_sensors_30.append(square_tiles_30 * degree)
        active_sensors_35.append(square_tiles_35 * degree)

    fig, ax = plt.subplots()

    plt.plot(active_sensors_20, k, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 20 m')
    plt.plot(active_sensors_25, k, 'b-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 25 m')
    plt.plot(active_sensors_30, k, 'r-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 30 m')
    plt.plot(active_sensors_35, k, 'g-', marker='s', linewidth=3, markersize=12, label=r'$\it{r_s}$ = 35 m')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='lower right')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=1, ymax=8)
    plt.xlim(xmin=0)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_k_for_square_vs_triangle(sensing_radius: int = 25) -> None:

    k = np.arange(1, 9, 1)

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )
    square_sensor_density = (square_tiles * k)/(250 * 250)

    triangle_tiles = math.floor(250//(0.5*math.sqrt(3)*sensing_radius))*(2*(250//sensing_radius)+1)
    triangle_sensor_density = (triangle_tiles * k)/(250 * 250)

    # Create plots
    fig, ax = plt.subplots()
    # ax.set(title=r'$\it{r_s}$ = 25 m',
    #        xlabel=r'$\it{k}$',
    #        ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(k, square_sensor_density, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(k, triangle_sensor_density, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=1, xmax=8)
    plt.ylim(ymin=0, ymax=0.035)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_lambda_vs_rs_for_square_vs_triangle(k: int = 3) -> None:

    sensing_radius = np.arange(15, 50, 5)

    square_tiles = (250//sensing_radius)**2
    square_sensor_density = (square_tiles * k)/(250 * 250)

    triangle_tiles_list = []
    for radius in sensing_radius:
        triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * radius)) * (2 * (250 // radius) + 1)
        triangle_tiles_list.append(triangle_tiles)

    triangle_sensor_density = []
    for tile_count in triangle_tiles_list:
        sensor_density = (tile_count * k) / (250 * 250)
        triangle_sensor_density.append(sensor_density)

    # Create plots
    fig, ax = plt.subplots()
    # ax.set(title=r'$\it{k}$ = 3',
    #        xlabel=r'$\it{r_s}$',
    #        ylabel=r'Planar Sensor Density $(\lambda)$')
    plt.plot(sensing_radius, square_sensor_density, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(sensing_radius, triangle_sensor_density, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)

    plt.title(r'Degree of Coverage $\it{k}$ = 3', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Planar Sensor Density $(\lambda)$', fontsize=15, fontweight='bold')

    plt.xlim(xmin=15, xmax=45)
    plt.ylim(ymin=0, ymax=0.035)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_deployed_sens_for_square_vs_triangle(sensing_radius: int = 25, k: int = 3) -> None:

    deployed_sensors = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )

    square_active_sensors = [square_tiles * k for _ in range(len(deployed_sensors))]

    triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * sensing_radius)) * (2 * (250 // sensing_radius) + 1)

    triangle_active_sensors = [triangle_tiles * k for _ in range(len(deployed_sensors))]

    fig, ax = plt.subplots()

    plt.plot(deployed_sensors, square_active_sensors, 'c-', linewidth=3, markersize=12, marker='s', label=r'$\it{k}$-CSqu')
    plt.plot(deployed_sensors, triangle_active_sensors, 'g-', linewidth=3, markersize=12, marker='^', label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m and Degree of Coverage $\it{k}$ = 3', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Deployed Sensors $(\it{n_d})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=100, ymax=750)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sensors_vs_k_for_square_vs_triangle(sensing_radius: int = 25):

    k = [1, 2, 3, 4, 5, 6, 7, 8]

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )

    triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * sensing_radius)) * (2 * (250 // sensing_radius) + 1)

    square_active_sensors = []
    triangle_active_sensors = []

    for degree in k:
        square_active_sensors.append(square_tiles * degree)
        triangle_active_sensors.append(triangle_tiles * degree)

    fig, ax = plt.subplots()

    plt.plot(square_active_sensors, k, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu')
    plt.plot(triangle_active_sensors, k, 'g-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15)
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m', fontsize=15, fontweight='bold')
    plt.xlabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.ylabel(r'Degree of Coverage $(\it{k})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=1, ymax=8)
    plt.xlim(xmin=0)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_rc_for_square_vs_triangle(sensing_radius: int = 25, k: int = 3) -> None:

    rc = range(50, 155, 5)

    square_tiles = number_of_square_tiles_for_square_field(
        sensing_radius=sensing_radius,
        field_width=250
    )

    square_active_sensors = [square_tiles * k for _ in range(len(rc))]
    square_active_sensors_2 = [square_tiles * 2 for _ in range(len(rc))]
    square_active_sensors_4 = [square_tiles * 4 for _ in range(len(rc))]

    triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * sensing_radius)) * (2 * (250 // sensing_radius) + 1)

    triangle_active_sensors_2 = [triangle_tiles * 2 for _ in range(len(rc))]
    triangle_active_sensors_3 = [triangle_tiles * 3 for _ in range(len(rc))]
    triangle_active_sensors_4 = [triangle_tiles * 4 for _ in range(len(rc))]

    fig, ax = plt.subplots()

    plt.plot(rc, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(rc, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(rc, triangle_active_sensors_2, 'b-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 2')
    plt.plot(rc, square_active_sensors_4, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 4')
    plt.plot(rc, square_active_sensors, 'g-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 3')
    plt.plot(rc, square_active_sensors_2, 'm-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 2')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right', bbox_to_anchor=(1, 0.7))
    plt.title(r'Sensing Radius $\it{r_s}$ = 25 m', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Communication Radius $(\it{r_c})$', fontsize=15, fontweight='bold')

    plt.ylim(ymin=100)
    plt.xlim(xmin=50, xmax=150)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


def plot_active_sens_vs_rs_for_square_vs_triangle(k: int = 3) -> None:

    sensing_radius = np.arange(15, 75, 5)

    square_active_sensors_2 = []
    square_active_sensors_3 = []
    square_active_sensors_4 = []
    triangle_active_sensors_4 = []
    triangle_active_sensors_3 = []
    triangle_active_sensors_2 = []

    for radius in sensing_radius:
        square_tiles = number_of_square_tiles_for_square_field(
            sensing_radius=radius,
            field_width=250
        )

        square_active_sensors_2.append(square_tiles * 2)
        square_active_sensors_3.append(square_tiles * k)
        square_active_sensors_4.append(square_tiles * 4)

        triangle_tiles = math.floor(250 // (0.5 * math.sqrt(3) * radius)) * (2 * (250 // radius) + 1)

        triangle_active_sensors_4.append(triangle_tiles * 4)
        triangle_active_sensors_3.append(triangle_tiles * k)
        triangle_active_sensors_2.append(triangle_tiles * 2)

    fig, ax = plt.subplots()

    plt.plot(sensing_radius, triangle_active_sensors_4, 'k-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 4')
    plt.plot(sensing_radius, triangle_active_sensors_3, 'r-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 3')
    plt.plot(sensing_radius, triangle_active_sensors_2, 'b-', marker='^', linewidth=3, markersize=12, label=r'$DIRACC_k$, $\it{k}$ = 2')
    plt.plot(sensing_radius, square_active_sensors_4, 'c-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 4')
    plt.plot(sensing_radius, square_active_sensors_3, 'g-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 3')
    plt.plot(sensing_radius, square_active_sensors_2, 'm-', marker='s', linewidth=3, markersize=12, label=r'$\it{k}$-CSqu, $\it{k}$ = 2')

    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)

    plt.legend(fontsize=15, loc='center right')
    # plt.title(r'Degree of Coverage $\it{k}$ = 3', fontsize=15, fontweight='bold')
    plt.ylabel(r'Number of Active Sensors $(\it{n_a})$', fontsize=15, fontweight='bold')
    plt.xlabel(r'Sensing Radius $(\it{r_s})$', fontsize=15, fontweight='bold')

    # plt.ylim(ymin=100, ymax=750)
    plt.xlim(xmin=15, xmax=70)

    plt.grid(b=True, which='major', color='0.6', linestyle='--')
    plt.show()


if __name__ == "__main__":
    # plot_lambda_vs_k()
    # plot_lambda_vs_rs()
    # plot_active_sens_vs_deployed_sens()
    # plot_active_sens_vs_deployed_sens_2()
    # plot_active_sensors_vs_k()
    # plot_lambda_vs_k_for_square_vs_triangle()
    # plot_lambda_vs_rs_for_square_vs_triangle()
    # plot_active_sens_vs_deployed_sens_for_square_vs_triangle()
    # plot_active_sensors_vs_k_for_square_vs_triangle()
    # plot_active_sens_vs_rc_for_square_vs_triangle()
    plot_active_sens_vs_rs_for_square_vs_triangle()
