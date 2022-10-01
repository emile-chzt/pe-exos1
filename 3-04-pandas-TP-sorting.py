# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     cell_metadata_json: true
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: TP sur le tri d'une dataframe
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Valérie Roy & Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(url="https://raw.githubusercontent.com/ue12-p22/python-numerique/main/notebooks/_static/style.html")



# %% [markdown]
# # TP sur le tri d'une dataframe

# %% [markdown]
# **Notions intervenant dans ce TP**
#
# * tri de `pandas.DataFrame` par ligne, par colonne et par index
#
# **N'oubliez pas d'utiliser le help en cas de problème.**

# %% [markdown]
# ## import des librairies et des données
#
# 1. Importez les librairies `pandas`et `numpy`
# <br>
#
# 1. Importez la librairie `matplotlib.pyplot`  
# <br>
#
# 1. lors de la lecture du fichier de données `titanic.csv`  
#    1. gardez uniquement les colonnes `cols` suivantes `'PassengerId'`, `'Survived'`, `'Pclass'`, `'Name'`, `'Sex'`, `'Age'` et `'Fare'`
#
#    1. mettez la colonne `PassengerId` comme index des lignes
#    1. besoin d'aide ? faites `pd.read_csv?`
# <br>
#
# 1. affichez le type des colonnes de la dataframe  
# en utilisant l'attribut `dtypes` des objets `pandas.DataFrame`
# <br>
#
# 1. sur le même graphique, et en utilisant `matplotlib.pyplot.plot`
#    1. plotez avec le paramètre `'rs'` la colonne des ages en fonctions des index  
#    (`r` pour rouge et `s` pour le style de point ici square)  
#    1. plotez avec paramètre `'b.'` et sans indiquer les abscisses, la colonne des ages
#    1. Que constatez-vous ?
#    <br>
#    1. Si vous n'indiquez pas l'axe des abscisses de votre dessin que choisit `plt` ? 
#
# <br>

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('titanic.csv', index_col='PassengerId', usecols=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age' ,'Fare']) 
df.dtypes
df.head()
plt.plot(df.index, df.Age,'rs')
plt.show()
plt.plot(df.Age,'b')
plt.show()
#il relie par défaut, et ça n'a pas d'ordre apparent


# %% [markdown]
# ## tri des lignes d'une dataframe
#
# Le but de cet exercice est d'organiser les lignes d'une dataframe suivant l'ordre d'une ou de plusieurs colonnes.
#
# Utilisez la méthode `df.sort_values()`
#
# 1. pour créer une **nouvelle** dataframe  
# dont les lignes sont triées dans l'ordre croisant des classes des passagers  
# on veut être sûr d'avoir une nouvelle dataframe sans considération de ce que retourne la fonction `sort_values`
# <br>
#
# 1. pour constater qu'elles sont triées, affichez les 3 premières lignes de la dataframe  
# vous devez voir que la colonne des `Pclass` est triée  
# que les lignes ont changé de place dans la table  
# et que leur indexation a été conservée
# <br>
#
# 1. triez la dataframe précédente dans l'ordre des ages des passagers  
# elle doit être modifiée sans utiliser d'affectation Python  
# (on veut faire ce qu'on appelle en informatique un *tri en place*)
# <br>
#
# 1. constater que les lignes de la dataframe sont triées  
# en affichant les 3 premières lignes de la dataframe
# <br>
#
# 1. plotez la colonne des ages de la  dataframe  
# Que constatez-vous ?
# <br>
#
# 1. plotez la colonne dans l'ordre des ages croissants
# <br>

# %%
df.sort_values('Pclass')

# %%
df.sort_values(by='Age',inplace=True)
df.iloc[700]

# %%
plt.plot(range(len(df)),df.Age,'r')
plt.show()
#c'est lié à peu près bien

# %% [markdown]
# ## tri des lignes *égales* au sens d'un premier critère d'une dataframe
#
# On reprend la dataframe d'origine
#
# 1. Affichez les ages des passagers d'index `673` et `746`  
# Que constatez-vous ?
# <br>
#
# 1. Utilisez le paramètre `by` de `df.sort_values()`  
# afin d'indiquer aussi une seconde colonne - par exemple `Fare`  
# pour trier les lignes identiques au sens de la première colonne  
# rangez dans une nouvelle dataframe
# <br>
#
# 1. Sélectionnez, dans la nouvelle dataframe, la sous-dataframe dont les ages ne sont pas définis  
# <br>
#
# 1. Combien manque-il d'ages ?
# <br>
#
# 1. Où sont placés ces passagers dans la data-frame triée ?  
# en début (voir avec `head`) ou en fin (voir avec `tail`) de dataframe ?
# <br>
#
# 1. Trouvez le paramètre de `sort_values()`  
# qui permet de mettre ces lignes en début de dataframe lors du tri
# <br>
#
# 1. produire une nouvelle dataframe en ne gardant que les ages connus,
#    et triée selon les ages, puis les prix de billet

# %% {"scrolled": true}
df.iloc[[673,756]]

# %% {"scrolled": true}
df2=df.sort_values(['Age','Fare'])
df2

# %%
#3 
df3=df2[df2.Age.isna()]
#4 
print(f' il manque {len(df3)} ages')


# %%
#5
df2.head()
df2.tail()
#on remarque que les ages inconnnus sont tout à la fin

# %% {"scrolled": true}
df2_bis=df.sort_values(['Age','Fare'],na_position='first')
df2_bis.head()

# %%
#7 ages connus triés selon age et prix
df[~df.Age.isna()].sort_values(['Age','Fare'])


# %% [markdown] {"tags": ["level_intermediate"]}
# ## tri d'une dataframe selon une colonne
#
# En utilisant `pandas.DataFrame.sort_values` il est possible de trier une dataframe  
# dans l'axe de ses colonnes
#
# 1. Créez une dataframe de 4 lignes et 5 colonnes de valeurs entières aléatoires entre 0 et 100  
#    mettez comme index (par exemple):  
#    aux lignes  `'un'`, `'deux'`, `'trois'` et `'quatre'`  
#    aux colonnes `'a'`, `'b'`, `'c'`, `'d'` et `'e'`  
#    **indice**: voyez la documentation de `pd.DataFrame` 
#    pour construire une dataframe  
#    par programme
#    <br>
#
# 1. affichez la dataframe
# <br>
#
# 1. Triez la dataframe en place dans l'ordre de la ligne d'index `trois`
# <br>
#
# 1. Affichez la dataframe
# <br>

# %%
L=np.random.randint(0,101,(4,5))
df=pd.DataFrame(data=L, columns=['a','b','c','d','e'], index=['un','deux','trois','quatre'])
print(df)
df.sort_values('trois', axis=1, inplace=True)
df

# %% [markdown] {"tags": ["level_intermediate"]}
# ## tri d'une dataframe selon l'index
#
# En utilisant `pandas.DataFrame.sort_index` il est possible de trier une dataframe  
# dans l'axe de ses index de ligne ou de colonnes  
# Utilisez le même genre de dataframe qu'à l'exercice précédent
# <br>
#
# 1. affichez la dataframe
# <br>
#
# 1. Trier la dataframe par index de ligne croissant  
# et affichez la dataframe
# <br>
#
# 1. Triez la dataframe par index de colonne croissant
# et affichez la dataframe
# <br>
#
# Cela peut, par exemple, servir à réordonner la dataframe du Titanic  
# qui a été triée en place dans l'ordre des `Age`, `Fare` croissants  
# par ordre d'index de ligne croissants

# %%
df=pd.DataFrame(data=L, columns=['a','b','c','d','e'], index=range(4))
print(df)
df.sort_index(axis=1)
