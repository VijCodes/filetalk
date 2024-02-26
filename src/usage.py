import numpy as np
import os
import sys
from sentence_transformers import SentenceTransformer
import importlib.util

sys.path.append('/Users/vijaykatta/Documents/Projects/local_doc_search')
sys.path.append('/Users/vijaykatta/Documents/Projects/local_doc_search/utils')
from utils.file_system_utils import FolderNode, build_tree, print_tree, fetch_parents, embedding_model

# Specify the root directory you want to analyze
root_directory = '/Users/vijaykatta/Documents/Projects/local_doc_search'

# Build the tree
tree_root = build_tree(root_directory)

# Print the tree structure
print_tree(tree_root)

def find_closest_node(root, query_vector, min_similarity=np.inf, closest_node=None):
    """
    Finds the node whose README vector is closest to the query vector.
    """
    if root.readme_vector is not None:
        similarity = np.dot(query_vector, root.readme_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(root.readme_vector))
        if similarity < min_similarity:
            min_similarity = similarity
            closest_node = root

    for child in root.children:
        closest_node, min_similarity = find_closest_node(child, query_vector, min_similarity, closest_node)

    return closest_node, min_similarity

def search_and_read_readmes(root, query):
    '''
    search for relevant folder
    '''
    query_vector = embedding_model.encode(query)
    closest_node, _ = find_closest_node(root, query_vector)

    # Read READMEs from the closest node to the root
    current_node = closest_node
    while current_node is not None:
        if current_node.readme_content:
            print(f"folder_path: {os.path.abspath(current_node.path)}")
        current_node = current_node.parent

# Usage
tree_root = build_tree(root_directory)  # Build the tree
search_and_read_readmes(tree_root, "where did i implement recommender")