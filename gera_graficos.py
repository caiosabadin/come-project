#!/bin/python3

from matplotlib import pyplot as plotter

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
divida = [2, 8, 4, 8, 6, 14]
lucro = [12, 10, 16, 10, 12, 4]
participacao = [35, 25, 30, 20, 30, 5]

fontdict = {
    'size': 22,
    'weight': 'bold',
    'color': '#550000',
}

fontdict_smaller = {
    'size': 20,
    'weight': 'bold',
    'color': '#550000',
}

plotter.figure(facecolor='#f2efea', figsize=(8.7, 7.5))
plotter.rcParams['font.size'] = 20
plotter.rcParams['font.weight'] = 'bold'
plotter.rcParams['axes.facecolor'] = '#f2efea'
plotter.rcParams["axes.spines.right"] = False
plotter.rcParams["axes.spines.top"] = False
plotter.plot(meses, divida, linewidth=3, color='#222222', marker='o', markeredgewidth=3, markerfacecolor='#950000', markeredgecolor='#550000')
plotter.grid(axis='y', color='#66635e')
plotter.title('Dívidas do último semestre', fontdict=fontdict, pad=20)
plotter.xlabel('Mês', fontdict=fontdict_smaller, labelpad=15)
plotter.ylabel('Dívidas (em milhares de reais)', fontdict=fontdict_smaller, labelpad=20)
plotter.show()

plotter.figure(facecolor='#f2efea', figsize=(8.7, 7.5))
plotter.rcParams['font.size'] = 20
plotter.rcParams['font.weight'] = 'bold'
plotter.rcParams['axes.facecolor'] = '#f2efea'
plotter.rcParams["axes.spines.right"] = False
plotter.rcParams["axes.spines.top"] = False
plotter.plot(meses, lucro, linewidth=3, color='#222222', marker='o', markeredgewidth=3, markerfacecolor='#950000', markeredgecolor='#550000')
plotter.grid(axis='y', color='#66635e')
plotter.title('Lucro do último semestre', fontdict=fontdict, pad=20)
plotter.xlabel('Mês', fontdict=fontdict_smaller, labelpad=15)
plotter.ylabel('Lucro (em milhares de reais)', fontdict=fontdict_smaller, labelpad=20)
plotter.show()

plotter.figure(facecolor='#f2efea', figsize=(8.7, 7.5))
plotter.rcParams['font.size'] = 20
plotter.rcParams['font.weight'] = 'bold'
plotter.rcParams['axes.facecolor'] = '#f2efea'
plotter.rcParams["axes.spines.right"] = False
plotter.rcParams["axes.spines.top"] = False
plotter.plot(meses, participacao, linewidth=3, color='#222222', marker='o', markeredgewidth=3, markerfacecolor='#950000', markeredgecolor='#550000')
plotter.grid(axis='y', color='#66635e')
plotter.title('Participação no mercado no último semestre', fontdict=fontdict, pad=20)
plotter.xlabel('Mês', fontdict=fontdict_smaller, labelpad=15)
plotter.ylabel('Participação no mercado (em %)', fontdict=fontdict_smaller, labelpad=20)
plotter.show()
