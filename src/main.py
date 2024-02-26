import argparse
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from .filetalk.utils.file_system_utils import FolderNode, build_tree, print_tree, fetch_parents, embedding_model

def main():
    '''
    main function for project
    '''
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Search for relevant folder based on query")
    parser.add_argument("query", type=str, help="Query to search for")
    args = parser.parse_args()

    # Specify the root directory you want to analyze
    root_directory = os.path.dirname(os.path.abspath(__file__))

    # Build the tree
    tree_root = build_tree(root_directory)

    # Search and print relevant README paths
    search_and_read_readmes(tree_root, args.query)

def search_and_read_readmes(root, query):
    '''
    Search for relevant folder based on the query and print the path.
    '''
    query_vector = embedding_model.encode(query)
    closest_node, _ = find_closest_node(root, query_vector)

    # Read READMEs from the closest node to the root
    current_node = closest_node
    while current_node is not None:
        if current_node.readme_content:
            print(f"Folder path: {os.path.abspath(current_node.path)}")
        current_node = current_node.parent

def find_closest_node(root, query_vector, max_similarity=-np.inf, closest_node=None):
    """
    Finds the node whose README vector is closest (most similar) to the query vector.
    """
    if root.readme_vector is not None:
        # Calculate cosine similarity
        similarity = np.dot(query_vector, root.readme_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(root.readme_vector))
        if similarity > max_similarity:  # Look for maximum similarity
            max_similarity = similarity
            closest_node = root

    for child in root.children:
        closest_node, max_similarity = find_closest_node(child, query_vector, max_similarity, closest_node)

    return closest_node, max_similarity

if __name__ == "__main__":
    main()