#Application qui permet de generer un examen et son correctum sur commande
import os.path
import sqlite3

#La base de donnees
def database():
    if os.path.isfile('examBank.db'):
        dbfile = r'C:\Users\berle\PycharmProjects\ExamGenerator\examBank.db'
    else :
        conn = sqlite3.connect('examBank.db')
        dbfile = r'C:\Users\berle\PycharmProjects\ExamGenerator\examBank.db'

#Creation d'une Fonction qui permet de stocker les questions, leurs types.
#Commencons par les questions a choix multiples
'''Puisqu'il existe 3 types de questions, on pourrait d'abord considerer chacun de ces types comme un objet.
Et ainsi creer pour chacun une fonction qui fera la gestion de son comportement'''

def quest_choix():
    question = input("Saisir le libelle de votre question: ")
    #stocker la question.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database()
   # quest_choix()

