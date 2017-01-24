import inspyred
import time

from os import path
from subprocess import call
from random import Random

from inspyred import ec
from inspyred.ec import terminators

from .handler import replace_word, copy_file, remove_file


# Design variable generator to use genetic algorithm
def generate_variable(random, args):
    size = args.get('num_inputs', 1)
    return [(random.uniform(26.0, 28.0), random.uniform(18.0, 20.0), random.uniform(0.085, 0.099), random.uniform(0, 0.034), random.uniform(0.070, 0.079), random.uniform(0.035, 0.04), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0), random.uniform(0, 1.0)) for i in range(size)]
    # return [random.uniform(-90, 90) for i in range(size)]


def evaluate_optimization(candidates, args):

    fitness = []
    idf_path = path.abspath("elementABS.idf")
    idf_path_template = path.abspath("TemplateFile\\elementABS.idf")

    for cs in candidates:
        trial = trial + 1

        for i in cs:
            var1 = round(i[0], 1)
            var2 = round(i[1], 1)

        replace_word(idf_path, 'zebra', str(var1))
        replace_word(idf_path, 'penguin', str(var2))

        call("C:\\EnergyPlusV8-1-0\\RunEPlus.bat elementABS KOR_Inchon.471120_IWEC")

        err_energy = calculation_cvrmse()

        scenario_list = [trial, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, err_energy]
        result_list.append(scenario_list)

        remove_file(idf_path)
        copy_file(idf_path_template, idf_path)

        fitness.append(err_energy)

        if(MAX_ERROR > min(fitness)):
            MAX_ERROR = min(fitness)
            result_step = [trial, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16, var17, var18, var19, err_energy]
            optimization_step_list.append(result_step)


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
                          bounder=inspyred.ec.Bounder([26.0, 18.0, 0.085, 0, 0.070, 0.035, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [28.0, 20.0, 0.099, 0.034, 0.079, 0.04, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),
                          max_evaluations=5000,
                          num_inputs=1)