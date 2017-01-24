import inspyred
import time

from os import getcwd
from subprocess import call
from random import Random

from inspyred import ec
from inspyred.ec import terminators

from .handler import replace_word, copy_file, remove_file

MAX_ERROR = 100
ACTUAL_ELECTRICITY = []
ACTUAL_HEATING = []


# Design variable generator to use genetic algorithm
def generate_variable(random, args):
    size = args.get('num_inputs', 1)
    return [(random.uniform(18.0, 22.0), random.uniform(24.0, 28.0), random.uniform(300, 600)) for i in range(size)]
    # return [random.uniform(-90, 90) for i in range(size)]


def evaluate_optimization(candidates, args):

    global MAX_ERROR

    fitness = []
    idf_path = getcwd() + "\energyplus\EnergyPlusV8-1-0\ProcessFiles\Progress\84m2\TestCase3.idf"
    idf_path_template = getcwd() + "\energyplus\EnergyPlusV8-1-0\ProcessFiles\Template\84m2\Calibration\TestCase3.idf"

    for cs in candidates:

        for i in cs:
            var1 = round(i[0], 1)
            var2 = round(i[1], 1)
            var3 = round(i[2], 1)

        replace_word(idf_path, 'cali_1', str(var1))
        replace_word(idf_path, 'cali_2', str(var2))
        replace_word(idf_path, 'cali_3', str(var3))

        call(getcwd() + "\energyplus\EnergyPlusV8-1-0\RunEPlus.bat TestCase3 KOR_Inchon.471120_IWEC")

        # err_energy = calculate_cvrmse()

        remove_file(idf_path)
        copy_file(idf_path_template, idf_path)

        # fitness.append(err_energy)
        fitness.append(MAX_ERROR)

        if MAX_ERROR > min(fitness):
            MAX_ERROR = min(fitness)

    return fitness


def optimization_core():
    rand = Random()
    rand.seed(int(time.time()))
    es = ec.GA(rand)

    es.terminator = terminators.evaluation_termination
    es.observer = inspyred.ec.observers.stats_observer
    final_pop = es.evolve(generator=generate_variable,
                          evaluator=evaluate_optimization,
                          pop_size=100,
                          mutation_rate=0.2,
                          maximize=False,
                          bounder=inspyred.ec.Bounder([18.0, 24.0, 300], [22.0, 28.0, 600]),
                          max_evaluations=5000,
                          num_inputs=1)


def cvrmse_optimization(year_electricity, year_heating):

    global ACTUAL_ELECTRICITY
    global ACTUAL_HEATING

    ACTUAL_ELECTRICITY = year_electricity
    ACTUAL_HEATING = year_heating

    optimization_core()


def calculate_energy():
    pass


def calculate_cvrmse():
    pass


def average(values):
    pass
