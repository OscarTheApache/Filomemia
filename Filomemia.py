#hecho con chatGPT
import spacy
from spacy import displacy
from IPython.display import display

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

def visualizar_relaciones(texto):
    doc = nlp(texto)
    entidades = []
    relaciones = []
    for token in doc:
        if token.ent_type_:
            entidades.append({'texto': token.text, 'tipo': token.ent_type_, 'posicion': token.i})
        if token.dep_ == 'nsubj' or token.dep_ == 'dobj':
            relaciones.append({'gobernante': token.head.i, 'dependiente': token.i, 'relacion': token.dep_})

    opciones = {'ents': entidades, 'dep': relaciones}
    displacy.serve(doc, style='dep', options=opciones)

texto = obtener_texto()
nlp = spacy.load('en_core_web_sm')
doc = nlp(texto)
oraciones = list(doc.sents)[8]
visualizar_relaciones(oraciones)

# Pedir al usuario que agregue o edite relaciones
opciones_usuario = input("¿Desea agregar o editar alguna relación? (s/n)")
relaciones_sugeridas = []
if opciones_usuario.lower() == 's':
    relacion = input("Ingrese la relación en el siguiente formato: 'gobernante, dependiente, relación' (sin comillas)")
    relaciones_sugeridas.append(relacion.split(','))

# Agregar relaciones sugeridas a la visualización
if len(relaciones_sugeridas) > 0:
    for relacion in relaciones_sugeridas:
        relaciones.append({'gobernante': int(relacion[0]), 'dependiente': int(relacion[1]), 'relacion': relacion[2]})
    opciones = {'ents': entidades, 'dep': relaciones}
    displacy.serve(doc, style='dep', options=opciones)






