import matplotlib.pyplot as plt


def get_candidate_data(candidat_nom, score_departements):
    """
    Restreint les données score_departements pour un candidat spécifique.
    
    Paramètres:
    - candidat_nom: nom du candidat
    - score_departements: dataframe avec tous les scores
    
    Sortie:
    - dataframe filtrée pour le candidat
    """
    return score_departements[score_departements['candidat'] == candidat_nom].copy()


def carte_candidat(candidat_nom, score_departements, departement_borders):
    """
    Crée une carte de surreprésentation pour un candidat spécifique.
    
    Paramètres:
    - candidat_nom: nom du candidat
    - score_departements: dataframe avec tous les scores par département
    - departement_borders: GeoDataFrame avec les frontières des départements
    
    Sortie:
    - affiche la carte
    """
    
    # Récupérer les données du candidat
    candidate_data = get_candidate_data(candidat_nom, score_departements)
    
    # Convertir le geojson en GeoDataFrame
    gdf_departments = departement_borders.copy()
    gdf_departments['code'] = gdf_departments['INSEE_DEP'].astype(str).str.zfill(2)
    
    # On merge les données avec le fond de carte
    candidate_map = gdf_departments.merge(
        candidate_data,
        left_on='code',
        right_on='code_departement',
        how='left'
    )
    
    # Création de la carte
    fig, ax = plt.subplots(figsize=(14, 10))
    candidate_map.plot(
        column='surrepresentation',
        ax=ax,
        legend=True,
        cmap='RdBu_r',
        edgecolor='black',
        linewidth=0.5,
        legend_kwds={'label': '(% par rapport à la moyenne nationale)', 'orientation': 'vertical'}
    )
    ax.set_title(f'Surreprésentation de {candidat_nom} par département', fontsize=14, fontweight='bold')
    ax.axis('off')
    plt.tight_layout()
    plt.show()
