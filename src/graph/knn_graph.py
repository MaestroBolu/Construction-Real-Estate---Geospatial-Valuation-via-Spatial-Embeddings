# src/graph/knn_graph.py

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


def build_knn_graph(
    df: pd.DataFrame,
    k: int = 15,
    lat_col: str = "lat",
    lon_col: str = "long"
) -> pd.DataFrame:
    """
    Build a K-Nearest Neighbor graph using haversine distance.

    Returns an edge list with:
    - src: source node index
    - dst: neighbor node index
    - distance: distance in radians
    """

    coords = df[[lat_col, lon_col]].values

    # Convert degrees → radians (required for haversine)
    coords_rad = np.radians(coords)

    knn = NearestNeighbors(
        n_neighbors=k + 1,  # +1 because the closest point is itself
        metric="haversine"
    )

    knn.fit(coords_rad)
    distances, indices = knn.kneighbors(coords_rad)

    edges = []

    for src_idx in range(len(df)):
        for neighbor_pos in range(1, k + 1):
            dst_idx = indices[src_idx, neighbor_pos]
            dist = distances[src_idx, neighbor_pos]

            edges.append({
                "src": src_idx,
                "dst": dst_idx,
                "distance": dist
            })

    return pd.DataFrame(edges)