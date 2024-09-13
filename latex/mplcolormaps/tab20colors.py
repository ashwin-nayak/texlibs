
import matplotlib.cm as mpc

colors = mpc.tab20.colors

output = []
for i, color in enumerate(colors):
    output.append('\definecolor{tab20_' + f'{i+1}'+ "}{rgb}{"+ ','.join([str(component) for component in color])+"}")

with open('colorstab20.sty', 'w') as file:
    file.write('\n'.join(output))
