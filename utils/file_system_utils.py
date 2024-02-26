import os
from .model_utils import embedding_model

class FolderNode:
    '''
    Each folder will correspond to a FolderNode
    '''
    def __init__(self, name, path, is_directory, parent=None):
        self.name = name
        self.path = os.path.abspath(path)
        self.is_directory = is_directory
        self.parent = parent
        self.children = []
        self.readme_content = None  # Add attribute to store README content
        self.readme_vector = self._embed_readme() if is_directory else None

    def add_child(self, child):
        self.children.append(child)

    def _embed_readme(self):
        '''
        Creates an embedding based on text in readme, with case-insensitive file name comparison.
        '''
        # Convert all file names in the directory to lowercase and check for 'readme.md'
        for entry in os.listdir(self.path):
            if entry.lower() == 'readme.md':  # Direct comparison after converting to lowercase
                readme_path = os.path.join(self.path, entry)
                with open(readme_path, 'r') as file:
                    content = file.read()
                    self.readme_content = content  # Store README content
                    # Generate the embedding for the README content
                    return embedding_model.encode(content)
        return None

def build_tree(path, parent=None):
    '''
    Builds a file system tree
    
    Args:
        path: Starting folder (root of file system tree)
        
    Returns:
        Root foldernode
    ''' 
    name = os.path.basename(path)
    if os.path.isdir(path):
        node = FolderNode(name, path, is_directory=True, parent=parent)
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            node.add_child(build_tree(full_path, parent=node))
    else:
        node = FolderNode(name, path, is_directory=False, parent=parent)
    return node

def print_tree(node, level=0):
    '''
    Prints the file system tree
    
    Args:
        FileNode
        
    Prints:
        file system tree
    '''
    prefix = '  ' * level + ('[D] ' if node.is_directory else '[F] ')
    print(prefix + node.name)
    for child in node.children:
        print_tree(child, level + 1)

def fetch_parents(node):
    ''''
    returns all ancestors of a FolderNode
    
    Args:
        FileNode
        
    Returns:
        List of parent FolderNodes
    '''
    parents = []
    current = node
    while current.parent is not None:
        parents.append(current.parent)
        current = current.parent
    return parents