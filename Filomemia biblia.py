#hecho con chatGPT
import spacy
from prettytable import PrettyTable
import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import display
from spacy import displacy

def obtener_texto():
    # root = tk.Tk()
    # root.withdraw()
    # ruta_archivo = filedialog.askopenfilename()
    ruta_archivo = "C:/Users/chej_/Documents/Filomemia/corpus/Genesis.txt"

    if ruta_archivo.lower().endswith('.txt'):
        with open(ruta_archivo, 'r') as archivo:
            texto = archivo.read()
    else:
        texto = None
        print("El archivo no es válido. Debe ser un archivo TXT.")
    return texto

# Cargar modelo de spaCy

def identificar_entidades(doc):
    entidades = []
    for token in doc:
        if token.pos_ in ['NOUN','PROPN']:
            entidades.append({'texto': token.text, 'inicio': token.idx, 'fin': token.idx + len(token)})
    return entidades

def definir_relaciones(doc, entidades):
    relaciones = []
    for ent1 in entidades:
        for ent2 in entidades:
            if ent1['inicio'] < len(doc) and ent1['fin'] < len(doc) and ent2['inicio'] < len(doc) and ent2['fin'] < len(doc) and ent1 != ent2:
                span1 = doc[ent1['inicio']:ent1['fin']]
                span2 = doc[ent2['inicio']:ent2['fin']]
                for i in range(len(doc)):
                    token = doc[i]
                    if token in [span1.root, span2.root]:
                        continue
                    if token.head in [span1.root, span2.root] and token.dep_ in ['nsubj', 'dobj', 'iobj', 'pobj', 'poss', 'attr', 'ccomp', 'xcomp', 'conj']:
                        relaciones.append(
                            {'entidad1': ent1['texto'], 'entidad2': ent2['texto'], 'relacion': token.dep_, 'conector': token.text})
    return relaciones

def crear_grafo(entidades, relaciones, dim_x):
    # Crear grafo vacío
    G = nx.DiGraph()

    # Añadir nodos al grafo
    for entidad in entidades:
        # Calcular posición x del nodo en función de su posición en el texto
        pos_x = (entidad['inicio'] + entidad['fin']) / 2
        # Asignar posición y constante para todas las entidades
        pos_y = 1
        # Añadir nodo al grafo con su posición
        G.add_node(entidad['texto'], pos=(pos_x, pos_y))

    # Añadir arcos al grafo
    for relacion in relaciones:
        G.add_edge(relacion['entidad1'], relacion['entidad2'], label=relacion['relacion'])

    # Calcular posiciones de los nodos para visualización
    pos = {}
    for nodo in G.nodes():
        pos[nodo] = (G.nodes[nodo]['pos'][0], G.nodes[nodo]['pos'][1])

    # Dibujar grafo
    plt.figure(figsize=(dim_x/10, len(entidades)/2))
    nx.draw(G, pos, with_labels=True, font_size=10, node_color='lightblue', edge_color='gray', arrowsize=20, node_size=800)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='red')

    # Mostrar grafo
    plt.show()

def actualizar_grafo(entidades, relaciones, nuevas_entidades, nuevas_relaciones, dim_x):
    # Unir las listas de entidades y relaciones
    todas_entidades = entidades + nuevas_entidades
    todas_relaciones = relaciones + nuevas_relaciones

    # Crear el grafo actualizado
    crear_grafo(todas_entidades, todas_relaciones, dim_x)

def contar_pos_tags(doc):
    pos_tags = {}
    for token in doc:
        if token.pos_ not in pos_tags:
            pos_tags[token.pos_] = 1
        else:
            pos_tags[token.pos_] += 1

    tabla = PrettyTable()
    tabla.field_names = ['POS Tag', 'Frecuencia']
    for tag, freq in pos_tags.items():
        tabla.add_row([tag, freq])

    print(tabla)

texto = obtener_texto()
nlp = spacy.load('en_core_web_sm')
doc = nlp(texto)
oraciones = list(doc.sents)[8]
# entidades = []
# relaciones = []
# entidades_totales = []
# relaciones_totales = []
# for oracion in oraciones:
#     entidades = identificar_entidades(oracion)
#     relaciones = definir_relaciones(oracion, entidades)
#     entidades_totales.append(entidades)
#     relaciones_totales.append(relaciones)
#     contar_pos_tags(oracion)
#     print(oracion)
#
# crear_grafo(entidades, relaciones, len(oracion))
# arbol = displacy.render(oracion, style = 'dep')
# display(arbol)

# for token in oraciones:
#     print(token.text, token.pos_,token.dep_, token.head.text)

# nuevas_entidades = ...
# nuevas_relaciones = ...
# actualizar_grafo(entidades, relaciones, nuevas_entidades, nuevas_relaciones, len(oracion))
