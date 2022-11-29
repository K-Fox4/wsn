import math

# Describe the scenarios that will be simulated
# scenarios should be described in the following format:
# scenario_name = (routing_topology, sleep_scheduling, aggregation_model)
# where routing_topology may be:
#   'DC'   : Direct Communication
#   'MTE'  : Minimum Transmission Energy
#   'LEACH': LEACH
#   'FCM  ': Fuzzy C-Means
# and sleep_scheduling may be:
#   None                 : No sleep scheduling (mind that None is not a string)
#   'Pso'                : Particle Swarm Optimization
#   'ModifiedPso'        : Modified PSO
#   'GeneticAlgorithm'   : Genetic Algorithm
# and aggregation_model may be:
#   'zero'  : Zero cost
#   'total' : 100% cost
#   'linear': TODO spec
#   'log'   : log cost
# the 4th argument is the nickname of that plot, if not specified (None),
# then the name is: routing_topology + sleep_scheduling

# for convenience, the scenarios list also accepts commands that are
# executed in run.py

scenario0 = ('DC', None, 'zero', None)
scenario1 = ('LEACH', None, 'zero', "LEACH")
scenario2 = ('MTE', None, 'total', None)
scenario3 = ('FCM', None, 'zero', None)
scenario4 = ('FCM', 'ModifiedPso', 'zero', 'FCMMPSO')
scenario5 = ('FCM', 'Pso', 'zero', None)
scenario6 = ('FCM', 'Ecca', 'zero', 'ECCA')
scenario7 = ('FCM', 'GeneticAlgorithm', 'zero', None)
scenario31 = ('FCM', None, 'zero', 'BS at (125,125)')
scenario32 = ('FCM', None, 'zero', 'BS at (65,65)')
scenario33 = ('FCM', None, 'zero', 'BS at (0,0)')
scenario34 = ('FCM', None, 'zero', 'BS at (-65,-65)')
# list with all scenarios to simulate

# example of configuration to get first part of results
# scenarios = [
#              "cf.FITNESS_ALPHA=0.5",
#              "cf.FITNESS_BETA=0.5",
# scenario3,
#              "plot_clusters(network)",
#              scenario0,
# scenario1,
# scenario2,
# scenario5,
#              scenario4,
#              "plot_time_of_death(network)",
#              "plot_traces(traces)",
#              "network.get_BS().pos_y=-75.0",
#              scenario3,
#              scenario0,
#              scenario1,
#              scenario2,
#              scenario5,
#              scenario4,
#              "save2csv(traces)",
#            ]

# scenarios = [
#               "cf.FITNESS_ALPHA=0.7",
#               "cf.FITNESS_BETA=0.3",
#              scenario0,
#              scenario1,
#              scenario2,
#              scenario3,
#               scenario4,
#              "cf.FITNESS_ALPHA=0.34",
#              "cf.FITNESS_BETA=0.33",
#              "cf.FITNESS_GAMMA=0.33",
#               scenario6,
#              scenario6,
#              #'cf.BS_POS_X=65.0',
#              #'cf.BS_POS_Y=65.0',
#              #scenario32,
#              #'cf.BS_POS_X=0.0',
#              #'cf.BS_POS_Y=0.0',
#              #scenario33,
#              #'cf.BS_POS_X=-65.0',
#              #'cf.BS_POS_Y=-65.0',
#              #scenario34,
#               "save2csv_raw(traces)",
#               "plot_traces(traces)",
#             ]

# scenarios = [
#              "cf.FITNESS_ALPHA=0.5",
#              "cf.FITNESS_BETA=0.5",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.75",
#              "cf.FITNESS_BETA=0.25",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.25",
#              "cf.FITNESS_BETA=0.75",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=1.0",
#              "cf.FITNESS_BETA=0.0",
#              scenario4,
#              scenario5,
#              scenario6,
#              "cf.FITNESS_ALPHA=0.0",
#              "cf.FITNESS_BETA=1.0",
#              scenario4,
#              scenario5,
#              scenario6,
#              "save2csv(traces)",
#            ]

"""k-coverage protocols"""

# (TILE_NAME, K, IS_STOCHASTIC_SENSING ?, ALPHA, BETA, PTH)

# Existing scenarios
leach = ('LEACH', None, 'zero', "LEACH", ("", 0, False))
direct_comm = ('DC', None, 'zero', "Direct Comm.", ("", 0, False))
mte = ('MTE', None, 'total', "MTE", ("", 0, False))

# k-CSqu protocol of square tessellation
k_csqu_d = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, False, 0, 0, 0))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.7
k_csqu_s27 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 2, 0.025, 0.7))
k_csqu_s37 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 3, 0.025, 0.7))
k_csqu_s47 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 4, 0.025, 0.7))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.8
k_csqu_s28 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 2, 0.025, 0.8))
k_csqu_s38 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 3, 0.025, 0.8))
k_csqu_s48 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 4, 0.025, 0.8))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.9
k_csqu_s29 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 2, 0.025, 0.9))
k_csqu_s39 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 3, 0.025, 0.9))
k_csqu_s49 = ('LEACH', None, 'zero', "k-CSqu", ("square", 3, True, 4, 0.025, 0.9))

# k-InnRhom protocol of Irregular Hexagonal (Type 1) tessellation
k_indi = ('LEACH', None, 'zero', "k-InDi", ("irrhex1", 3, False, 0, 0, 0))

# DIRACCk protocol of Reuleaux triangle tessellation
diracck = ('LEACH', None, 'zero', "DIRACCk", ("triangle", 3, False, 0, 0, 0))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.7
diracck_s27 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 2, 0.025, 0.7))
diracck_s37 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 3, 0.025, 0.7))
diracck_s47 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 4, 0.025, 0.7))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.8
diracck_s28 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 2, 0.025, 0.8))
diracck_s38 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 3, 0.025, 0.8))
diracck_s48 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 4, 0.025, 0.8))

# ALPHA = [2, 3, 4], BETA = 0.025, PTH = 0.9
diracck_s29 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 2, 0.025, 0.9))
diracck_s39 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 3, 0.025, 0.9))
diracck_s49 = ('LEACH', None, 'zero', "k-CSqu", ("triangle", 3, True, 4, 0.025, 0.9))

scenarios = [
    # "plot_network(network)",
    k_csqu_s27,
    diracck_s27,
    # k_csqu_s29,
    # diracck_s29,
    "plot_traces(traces)",
]

# Tracer options
TRACE_ENERGY = 1
TRACE_ALIVE_NODES = 1
TRACE_COVERAGE = 1
TRACE_LEARNING_CURVE = 0

# Runtime configuration
MAX_ROUNDS = 1000000

# number of transmissions of sensed information
# to cluster heads or to
# base station (per round)
MAX_TX_PER_ROUND = 1

NOTIFY_POSITION = 0

# Network configurations:
# number of nodes
NB_NODES = 1000

# node sensor range
COVERAGE_RADIUS = 25  # meters

# node transmission range
TX_RANGE = 50  # meters
BSID = -1

# area definition
AREA_WIDTH = 100.0
AREA_LENGTH = 100.0

# base station position
BS_POS_X = 50.0
BS_POS_Y = 50.0

# packet configs
MSG_LENGTH = 4000  # bits
HEADER_LENGTH = 150  # bits

# initial energy at every node's battery
INITIAL_ENERGY = 70  # Joules

# Energy Configurations
# energy dissipated at the transceiver electronic (/bit)
E_ELEC = 50e-9  # Joules

# energy dissipated at the data aggregation (/bit)
E_DA = 5e-9  # Joules

# energy dissipated at the power amplifier (supposing a multi-path
# fading channel) (/bin/m^4)
E_MP = 0.0013e-12  # Joules

# energy dissipated at the power amplifier (supposing a line-of-sight
# free-space channel (/bin/m^2)
E_FS = 10e-12  # Joules

# energy dissipated for moving a sensor (J/m)
E_MOVE = (0.008, 0.012)

# Speed of the sensor (m/round)
SENSOR_SPEED = 1

THRESHOLD_DIST = math.sqrt(E_FS / E_MP)  # meters

# Routing configurations:
NB_CLUSTERS = 5

# FCM fuzziness coefficient
FUZZY_M = 2

# Sleep Scheduling configurations:
NB_INDIVIDUALS = 10
MAX_ITERATIONS = 50

# ALPHA and BETA are the fitness function' weights
# where ALPHA optimizes energy lifetime, BETA the coverage
FITNESS_ALPHA = 0.34
FITNESS_BETA = 0.33
FITNESS_GAMMA = 0.33
WMAX = 0.6
WMIN = 0.1

# Other configurations:
# grid precision (the bigger the faster the simulation)
GRID_PRECISION = 1  # in meters

# useful constants (for readability)
INFINITY = float('inf')
MINUS_INFINITY = float('-inf')

RESULTS_PATH = 'results/'
