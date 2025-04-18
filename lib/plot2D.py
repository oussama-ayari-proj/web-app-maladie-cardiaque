import plotly.express as px
import streamlit as st
from scipy.stats import gaussian_kde
import numpy as np
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt



def distribution_de_target(data):
    st.header('Distribution en \% de la variable cible (Diagnostic des maladies cardiaque)')
    pourcentages = data['target'].value_counts(normalize=True).sort_index().reset_index()
    pourcentages.columns = ['valeur', 'proportion']
    pourcentages['proportion'] *= 100

    # Bar plot
    fig = px.bar(pourcentages, x='valeur', y='proportion', text='proportion',
                labels={'valeur': 'Valeur (0: < 50% | 1: > 50% Rétrécissement du diamètre des artères)', 'proportion': 'Pourcentage'},
                )

    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(yaxis_range=[0, 110])

    st.plotly_chart(fig)

def distribution_cols(data):
    st.header('Distribution des colonnes')
    mypal = ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA']
    cols = st.multiselect('Sélectionnez les colonnes :', data.columns, default=[], key='2')
    L = len(cols)
    if L>0:
        ncol = 2 if L > 1 else 1
        nrow = int(np.ceil(L / ncol))

        fig, axes = plt.subplots(nrow, ncol, figsize=(16, 14), facecolor='#F6F5F4')
        fig.subplots_adjust(hspace=0.4)

        axes = np.array(axes).reshape(nrow, ncol)

        idx = 0
        for row in range(nrow):
            for col_idx in range(ncol):
                if idx >= L:
                    axes[row, col_idx].axis('off')
                    continue

                col = cols[idx]
                ax = axes[row, col_idx]

                if col == 'num_major_vessels':
                    sns.countplot(data=data, x=col, hue="target", palette=mypal[1::4], ax=ax)
                    for p in ax.patches:
                        height = p.get_height()
                        ax.text(p.get_x() + p.get_width()/2., height + 0.5, f'{height:.0f}',
                                ha="center", va='bottom', fontsize=10,
                                bbox=dict(facecolor='none', edgecolor='black', boxstyle='round', linewidth=0.5))
                else:
                    sns.kdeplot(data=data, x=col, hue="target", multiple="stack",
                                palette=mypal[1::4], ax=ax)

                ax.set_xlabel(col, fontsize=14)
                ax.set_ylabel("Densité", fontsize=14)
                ax.set_facecolor('#F6F5F4')
                sns.despine(ax=ax)

                idx += 1

        st.pyplot(fig)


def pairplot(data):
    st.header('Pair plots:')
    cols = st.multiselect('Sélectionnez les colonnes :', data.columns, default=[], key='3')
    cols.append('target')
    data_ = data[cols]
    if len(cols)>1:
        g = sns.pairplot(data_, hue="target", corner=True, diag_kind='hist')
        st.pyplot(g)

def regplots(data):
    st.header('Relations Linéaires avec la colonne Age')
    mypal = ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA']
    cols=st.multiselect('Séléctionner colonne(s)',['cholesterol','max_heart_rate_achieved','resting_blood_pressure','st_depression'],default=[],key='100')
    L=len(cols)
    if L>0:
        fig, ax = plt.subplots(1,L, figsize=(25, 10))
        if L > 1:
            for i in range(L):
                sns.regplot(data=data[data['target'] ==1], x='age', y=cols[i], ax = ax[i], color=mypal[0], label='1')
                sns.regplot(data=data[data['target'] ==0], x='age', y=cols[i], ax = ax[i], color=mypal[5], label='0')
        elif L==1:
            sns.regplot(data=data[data['target'] ==1], x='age', y=cols[0], ax = ax, color=mypal[0], label='1')
            sns.regplot(data=data[data['target'] ==0], x='age', y=cols[0], ax = ax, color=mypal[5], label='0')
        
        st.pyplot(fig)


def distribution_variables(data):
    st.header('Distribution de variables catégorielles')
    cols = st.multiselect(
        'Séléctionner colonne(s)',
        ['sex','chest_pain_type','resting_electrocardiogram','st_slope','thalassemia','fasting_blood_sugar','exercise_induced_angina'],
        default=[],
        key='300'
    )
    
    L = len(cols)
    mypal = ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA']
    
    if L > 0:
        ncol = 2
        nrow = int(np.ceil(L / ncol))
        fig, axes = plt.subplots(nrow, ncol, figsize=(18, 7 * nrow), facecolor='#F6F5F4')
        fig.subplots_adjust(top=0.92, hspace=0.4)
        axes = axes.flatten()
        
        for i, col in enumerate(cols):
            ax = axes[i]
            sns.countplot(data=data, x=col, hue="target", palette=mypal[1::4], ax=ax)
            ax.set_xlabel(col, fontsize=20)
            ax.set_ylabel("Count", fontsize=20)
            ax.set_facecolor('#F6F5F4')
            sns.despine(ax=ax, right=True, offset=0, trim=False)
            ax.legend(facecolor='#F6F5F4')
            
            for p in ax.patches:
                height = p.get_height()
                ax.text(
                    p.get_x() + p.get_width() / 2.,
                    height + 3,
                    '{:1.0f}'.format(height),
                    ha="center",
                    fontsize=10,
                    bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=0.3', linewidth=0.5)
                )

        for j in range(L, len(axes)):
            axes[j].set_visible(False)

        st.pyplot(fig)

def matrice_corr(data):
    st.header("Matrice de corrélation")
    corr = data.corr()
    mypal = ['#FC05FB', '#FEAEFE', '#FCD2FC','#F3FEFA', '#B4FFE4','#3FFEBA']
    mask = np.triu(np.ones_like(corr, dtype=bool))
    f, ax = plt.subplots(figsize=(18, 15), facecolor=None)
    cmap = sns.color_palette(mypal, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1.0, vmin=-1.0, center=0, annot=True,
                square=False, linewidths=.5, cbar_kws={"shrink": 0.75})
    st.pyplot(f)