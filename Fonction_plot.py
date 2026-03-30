import matplotlib.pyplot as plt

def plot_surrepresentation(candidat_nom, score_departements, top_n=10):
    
    data = score_departements[score_departements['candidat'] == candidat_nom].copy()
    
    if data.empty:
        print(f"Candidat '{candidat_nom}' introuvable.")
        return
    
    # Top N en valeur absolue
    top = (
        data.reindex(data['surrepresentation'].abs().sort_values(ascending=False).index)
        .head(top_n)
        .sort_values('surrepresentation')
    )
    
    
    nom_court = candidat_nom.split()[-1]  
    
    fig, ax = plt.subplots(figsize=(9, 5))
    colors = ['#e74c3c' if v >= 0 else '#3498db' for v in top['surrepresentation']]
    
    ax.barh(top['code_departement'].astype(str), top['surrepresentation'], color=colors)
    ax.axvline(0, color='black', linewidth=0.6)
    ax.set_xlabel('Surreprésentation (%)')
    ax.set_ylabel('Département')
    ax.set_title(f'Top {top_n} des surreprésentations de {nom_court}', fontsize=13, fontweight='bold')
    
    # Annotations valeurs
    for i, (val, dep) in enumerate(zip(top['surrepresentation'], top['code_departement'])):
        ha = 'left' if val >= 0 else 'right'
        offset = 1 if val >= 0 else -1
        ax.text(val + offset, i, f"{val:.1f}%", va='center', ha=ha, fontsize=8)
    
    plt.tight_layout()
    plt.show() 



