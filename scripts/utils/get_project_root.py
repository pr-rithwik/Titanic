from pathlib import Path

current_file = Path(__file__)

# Search for a known file or folder that signifies the project root
def find_project_root(current_path, root_marker):
    for parent in current_path.parents:
        if (parent / root_marker).exists():
            return parent
    return None

def get_project_root():
    project_root = find_project_root(current_file, 'README.md') or \
        find_project_root(current_file, '.git')

    if project_root:
        print("Project root found:", project_root)
    else:
        print("Project root not found.")
    return project_root
