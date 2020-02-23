
import sys
import os

import pandas as pd
import numpy as np
import scipy 
from scipy.cluster import hierarchy as hc # for dendograms 

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import f1_score # f1_score(y_true, y_pred)
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectFromModel


df_train_pro = pd.read_table(f'{os.getcwd()}/raw_data/train_pro.tsv', 
                           delim_whitespace=True,
                           low_memory=False,).T
df_test_pro = pd.read_table(f'{os.getcwd()}/raw_data/test_pro.tsv', 
                           delim_whitespace=True,
                           low_memory=False,).T
df_train_rna = pd.read_table(f'{os.getcwd()}/raw_data/train_rna.tsv', 
                           delim_whitespace=True,
                           low_memory=False,).T
df_test_rna = pd.read_table(f'{os.getcwd()}/raw_data/test_rna.tsv', 
                           delim_whitespace=True,
                           low_memory=False,).T
df_train_cli = pd.read_csv(f'{os.getcwd()}/raw_data/train_cli.tsv', 
                           delim_whitespace=True,
                           low_memory=False,)
df_test_cli = pd.read_csv(f'{os.getcwd()}/raw_data/test_cli.tsv', 
                           delim_whitespace=True,
                           low_memory=False,)
df_train_mislabel = pd.read_csv(f'{os.getcwd()}/raw_data/sum_tab_1.csv', 
                           low_memory=False,)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)


# df_train_pro
# df_test_pro
# df_train_rna
# df_test_rna
# df_train_cli
# df_test_cli
# df_train_mislabel

train_pro = df_train_pro.copy(deep=True)
train_pro = train_pro.fillna(train_pro.median())
train_pro.index.name = 'sample'

test_pro = df_test_pro.copy(deep=True)
test_pro = test_pro.fillna(test_pro.median())
test_pro.index.name = 'sample'


train_rna = df_train_rna.copy(deep=True)
train_rna = train_rna.fillna(train_rna.median())
train_rna.index.name = 'sample'

test_rna = df_test_rna.copy(deep=True)
test_rna = test_rna.fillna(test_rna.median())
test_rna.index.name = 'sample'

# df_train_pro
# train_pro
# df_test_pro
# test_pro
# df_train_rna
# train_rna
# df_test_rna
# test_rna

train_cli = df_train_cli.copy(deep=True)
train_cli = train_cli.set_index('sample')
train_cli = train_cli.replace({'gender': {'Male':0, 'Female':1},
                               'msi': {'MSI-Low/MSS':0, 'MSI-High':1}})

test_cli = df_test_cli.copy(deep=True)
test_cli = test_cli.set_index('sample')
test_cli = test_cli.replace({'gender': {'Male':0, 'Female':1},
                             'msi': {'MSI-Low/MSS':0, 'MSI-High':1}})


# df_train_cli
# train_cli
# df_test_cli
# test_cli

train_mislabel = df_train_mislabel.copy(deep=True)
train_mislabel = train_mislabel.set_index('sample')

# df_train_mislabel
# train_mislabel

train_pro.reset_index(drop=True, inplace=True)
train_rna.reset_index(drop=True, inplace=True)
train_cli.reset_index(drop=True, inplace=True)
train_mislabel.reset_index(drop=True, inplace=True)

# train_pro
# train_rna
# train_cli
# train_mislabel

train_pro_combined = pd.concat([train_mislabel, train_cli, train_pro], 
                               axis=1)
train_rna_combined = pd.concat([train_mislabel, train_cli, train_rna], 
                               axis=1)
train_combined = pd.concat([train_mislabel, 
                            train_cli, 
                            train_rna, 
                            train_pro], 
                           axis=1)

# train_pro_combined
# train_rna_combined
# train_combined