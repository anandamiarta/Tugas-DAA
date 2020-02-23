import numpy as np
# from random import randint
import networkx as nx
import matplotlib.pyplot as plt
import time

adj_mtx =  [[0,1,1,1,0],
            [1,0,0,1,1],
            [1,0,0,1,0],
            [1,1,1,1,1],
            [0,1,0,1,0]]
node = len(adj_mtx)
print(adj_mtx)
    
#-------------------------- inti program begin -------------------------    
def isSafe(co,list_color,n):
    for i in range(node-1): #untuk setiap node lain
        if adj_mtx[n][i] == 1 and list_color[i] == co: #jika bertetangga dan warnanya sama
            return False
    return True

def findSolution(list_color,n):
    if(n == node): #kalo udah semua node di warnai
        return True
    for co in range(1,mc+1): #coba setiap warna
        if(isSafe(co,list_color,n)): #if warna bisa di pakai
            list_color[n] = co #assign dengan warna co
            if findSolution(list_color,n+1): #pindah ke node lain
                return True
            list_color[n] = 0 #kalo gabisa, hapus warna sekarang
    return False

def graphColoring(mtx,mc):
    list_color = np.zeros(node,dtype=int)
    print('>> Maximum color :', mc)
    if not(findSolution(list_color,0)): #kalo ga ada solusi
        print('>> Solution not found')
        return False
    print('>> Solution Found :',list_color)
    print('>> Minimum color needed :', max(list_color))
    draw_graph(hubungan,list_color)
    
def draw_graph(hubungan,color): #untuk menampilkan graph
    t = time.process_time()
    G=nx.Graph()
    G.add_edges_from(hubungan)
    co = [color[i] for i in G.nodes()]
    nx.draw(G, node_size=1000/(len(hubungan)/10),node_color=co,
            with_labels=True,font_color='white')
    print(time.process_time()-t)
    plt.show()
#-------------------------- inti program ends ------------------------------
# adjency matrix 13x13
# adj_mtx = [[0,1,1,0,0,0,0,0,0,0,0,0,0],
#            [1,0,0,0,1,0,0,0,0,0,0,0,0],
#            [1,0,0,1,1,0,0,0,0,0,0,0,0],
#            [0,0,1,0,0,1,0,0,0,0,0,0,0],
#            [0,1,0,0,0,1,0,0,0,0,0,0,0],
#            [0,0,0,1,1,0,1,1,0,0,0,0,0],
#            [0,0,0,0,0,1,0,0,1,0,0,0,0],
#            [0,0,0,0,0,1,0,0,0,1,0,0,0],
#            [0,0,0,0,0,0,1,0,0,1,1,0,0],
#            [0,0,0,0,0,0,0,1,1,0,0,1,0],
#            [0,0,0,0,0,0,0,0,1,0,0,0,1],
#            [0,0,0,0,0,0,0,0,0,1,0,0,1],
#            [0,0,0,0,0,0,0,0,0,0,1,1,0]]

# adjency matrix 11x11
# adj_mtx =  [[0,0,0,0,0,0,0,0,1,1,0],
#             [0,1,0,0,0,0,0,0,0,0,1],
#             [0,1,0,0,0,0,0,0,1,0,0],
#             [0,0,0,0,0,0,1,1,0,0,0],
#             [0,0,0,0,0,1,0,0,1,0,0],
#             [0,0,0,0,1,0,1,0,0,0,0],
#             [0,0,0,1,0,1,0,0,0,0,0],
#             [0,0,0,1,0,0,0,0,1,0,0],
#             [1,0,1,0,1,0,0,1,0,0,0],
#             [1,0,0,0,0,0,0,0,0,0,0],
#             [0,1,0,0,0,0,0,0,0,0,0]]

# adjency matrix 7x7
# adj_mtx =  [[0,1,0,0,1,1,0],
#             [1,0,1,0,0,0,1],
#             [0,1,0,1,0,0,0],
#             [0,0,1,0,1,0,1],
#             [1,0,0,1,0,1,1],
#             [1,0,0,0,1,0,0],
#             [0,1,0,1,1,0,0]]

# adjency matrix 9x9
# adj_mtx =  [[0,1,1,1,0,0,0,0,0],
#             [1,0,0,0,1,1,0,0,0],
#             [1,0,0,1,0,0,1,0,0],
#             [1,0,1,0,0,0,1,1,0],
#             [0,1,0,0,0,0,0,0,1],
#             [0,1,0,0,0,0,0,0,0],
#             [0,0,1,1,0,0,0,0,0],
#             [0,0,0,1,0,0,0,0,0],
#             [0,0,0,0,1,0,0,0,0]]

# adjency matrix 5x5


#cari keterhubungan
hubungan = []
for i in range(len(adj_mtx)):
    for j in range(len(adj_mtx[i])):
        if adj_mtx[i][j] == 1 and (i,j) not in hubungan and (j,i) not in hubungan:
            hubungan.append((i,j))
            
mc = node  #max color

graphColoring(adj_mtx,mc)
