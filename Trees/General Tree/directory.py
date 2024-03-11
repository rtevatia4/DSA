"""
directory structure
root - "folder-1"
directoryStructure = [["folder-1","folder-2"],["folder-1","folder-3"],["folder-1","folder-4"]]

            folder-1
        |        |        |
    folder-2   folder4  folder3
"""
def process_queries(directory_structure, queries):
    # Initialize directory dictionary
    directories = {"folder-1": set()}

    # Populate directory dictionary
    for parent, directory in directory_structure:
        if parent not in directories:
            directories[parent] = set()
            directories[parent].add(directory)
        directories[parent].add(directory)
        if directory not in directories:
            directories[directory] = set()
            directories[directory].add(parent)
        directories[directory].add(parent)
    
    # Function to count reachable directories recursively
    def count_reachable_directories(directory, visited):
        visited.add(directory)
        count = 1
        # print(directories)
        for subdirectory in directories[directory]:
            # print(subdirectory)
            if subdirectory not in visited:
                count += count_reachable_directories(subdirectory, visited)
        return count

    # Process queries
    for query in queries:
        parts = query.split(" ")
        command = parts[0]
        if command == "mkdir":
            parent, directory = parts[1], parts[2]
            if parent not in directories:
                directories[parent] = set()
                directories[parent].add(directory)
            directories[parent].add(directory)
            if directory not in directories:
                directories[directory] = set()
                directories[directory].add(parent)
            directories[directory].add(parent)
        elif command == "rmdir":
            directory = parts[1]
            if directory in directories:
                del directories[directory]
            # Remove the directory from its parent's set of children
            for parent, children in directories.items():
                if directory in children:
                    children.remove(directory)
                    break
        elif command == "count-dir":
            directory = parts[1]
            # print(directory)
            visited = set()
            print(count_reachable_directories(directory, visited))

# Given directory structure
directoryStructure = [["folder-1","folder-2"],["folder-1","folder-3"],["folder-2","folder-4"]]
# Queries to process
queries = ["mkdir folder-1 folder-5", "count-dir folder-2", "count-dir folder-1"]

# Process queries
process_queries(directoryStructure, queries)
