import numpy as np
import ga
from Mochila import Mochila


def main():

    pop_size = 6

    saco_de_dormir = Mochila('Saco de dormir', 15, 15)
    corda = Mochila('Corda', 3, 10)
    canivete = Mochila('Canivete', 2, 10)
    tocha = Mochila('Tocha', 5, 5)
    garrafa = Mochila('Garrafa', 9, 8)
    comida = Mochila('Comida', 20, 17)

    itens = [saco_de_dormir, corda, canivete, tocha, garrafa, comida]

    num_weights = 6

    sol_per_pop = 8

    # população tem sol_per_pop cromossomos com num_weights gens
    pop_size = (sol_per_pop, num_weights)

    # População inicial
    new_population = np.random.randint(2, size=pop_size)
    # Algoritmo genético
    num_generations = 100
    num_parents_mating = 4

    for generation in range(num_generations):
        print(f"Geração: {generation}")

        # medir o ‘fitness’ de cada cromossomo na população
        fitness = ga.cal_pop_fitness(itens, new_population)

        print("Valores de fitness:")
        print(fitness)

        # Selecionar os melhores pais na população para o cruzamento
        parents = ga.select_mating_pool(new_population, fitness, num_parents_mating)

        print("Genitores selecionados(pais):")
        print(parents)

        # formar a próxima geração usando crossover
        offspring_crossover = ga.crossover(parents, offspring_size=(
            pop_size[0] - parents.shape[0], num_weights
        ))
        print("Resultado do crossover:")
        print(offspring_crossover)

        # adicionar variações aos filhos usando mutação
        offspring_mutation = ga.mutation(offspring_crossover)
        print("Resultado da mutação:")
        print(offspring_mutation)

        # criar a nova população baseada nos pais e filhos
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation

        # best_result = np.max(np.sum(new_population*equation_inputs, axis=1))
        # print(f"Melhor resultado depois da geração {generation}: {best_result}")

    fitness = ga.cal_pop_fitness(itens, new_population)
    best_match_idx = np.where(fitness == np.max(fitness))[0][0]

    print("Melhor solução: ", new_population[best_match_idx, :])
    print("Fitness da melhor solução: ", fitness[best_match_idx])
    printar_nome_itens_selecionados(best_match_idx, itens, new_population)


def printar_nome_itens_selecionados(best_match_idx, itens, new_population):
    for idx, item in enumerate(itens):
        if new_population[best_match_idx, idx] == 1:
            print(item.nome)


if __name__ == '__main__':
    main()
