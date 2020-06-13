# plot_mesh
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
def plot_mesh(F, V, color = None):
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_axes()
    ax.plot_trisurf(V[0],V[1],V[2], triangles=F, cmap=plt.cm.Spectral)