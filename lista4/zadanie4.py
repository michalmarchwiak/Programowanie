import matplotlib.pyplot as plt
import networkx as nx
import random
from matplotlib.animation import FuncAnimation

# Tworzenie grafu Watts-Strogatza
n = 30
k = 4
p = 0.2
G = nx.watts_strogatz_graph(n, k, p)

# Inicjacja pozycji wierzchołków
pos = nx.spring_layout(G)

# Inicjacja agenta
agent = random.choice(list(G.nodes()))


# Funkcja rysująca graf
def draw_graph():
    plt.clf()
    nx.draw(G, pos=pos, node_color='lightblue', with_labels=True)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[agent], node_color='red')


# Funkcja animacji
def animate(i):
    global agent
    draw_graph()
    neighbors = list(G.neighbors(agent))
    if len(neighbors) > 0:
        agent = random.choice(neighbors)
    else:
        agent = random.choice(list(G.nodes()))
    plt.title('Step {}'.format(i))


# Inicjacja animacji
ani = FuncAnimation(plt.gcf(), animate, frames=100, interval=500)

# Zapis animacji do pliku gif
ani.save('watts_strogatz.gif', writer='pillow')
