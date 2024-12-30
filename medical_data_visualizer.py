import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


# 1
df = pd.read_csv("medical_examination.csv")
# 
# 2

df['overweight'] = (df['weight'] / ((df['height']/100) ** 2)).apply(lambda x:1 if x > 25 else 0)
print(df)
# 3

df['cholesterol'] = df['cholesterol'].apply(lambda x:0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x:0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    
    

    # 6
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'],
                     var_name='variable',
                     value_name='value')
                       
    
    # 7
    print(df_cat)
    # df_cat["total"] = 1
    df_cat.groupby(["cardio", "variable", "value"], as_index =False).count()
    # 8
    fig = sns.catplot(x='variable',  hue='value', col='cardio', kind='count', data=df_cat)
    fig.set_axis_labels('variable', 'total')
    
    # 9
    for ax in fig.axes.flat:
        for rect in ax.get_children():
            if isinstance(rect, patches.Rectangle):
                print(f"Rectangle: {rect}, Position: {rect.get_xy()}, Width: {rect.get_width()}, Height: {rect.get_height()}")
    
    fig.savefig('catplot.png')
    return fig.fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &  # Diastolischer Druck (ap_lo) muss kleiner oder gleich systolischem Druck (ap_hi) sein
    (df['height'] >= df['height'].quantile(0.025)) &  # Höhe darf nicht unter dem 2,5. Perzentil liegen
    (df['height'] <= df['height'].quantile(0.975)) &  # Höhe darf nicht über dem 97,5. Perzentil liegen
    (df['weight'] >= df['weight'].quantile(0.025)) &  # Gewicht darf nicht unter dem 2,5. Perzentil liegen
    (df['weight'] <= df['weight'].quantile(0.975))     # Gewicht darf nicht über dem 97,5. Perzentil liegen
]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10, 8))  # Hier wird die Figur und die Achse erstellt

    # 15 Erstellen der Heatmap mit Seaborn
    sns.heatmap(corr, annot=True, fmt=".1f", cmap="coolwarm", mask=mask, linewidths=0.5, cbar_kws={"shrink": 0.8}, ax=ax)
    



    # 16
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()