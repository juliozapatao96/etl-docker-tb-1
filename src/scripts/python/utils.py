import shutil
import os

def move_file(file, source_folder, destination_folder):
    """
    Moves a file from one folder to another.

    :param file: Name of the file to move.
    :param source_folder: Path of the source folder.
    :param destination_folder: Path of the destination folder.
    """
    # Create the complete paths
    path_source = os.path.join(source_folder, file)
    path_destination = os.path.join(destination_folder, file)

    try:
        # Move the file
        shutil.move(path_source, path_destination)
        print(f'Archivo movido de {source_folder} a {destination_folder}')
    except FileNotFoundError:
        print('El archivo no se encuentra en la carpeta origen')
    except PermissionError:
        print('No tienes permiso para mover este archivo')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

def list_csv_files(directory):
    """
    Returns a list of CSV file names (without extension) in the specified directory.

    :param directory: The path of the directory to search for CSV files.
    :return: List of CSV file names without their extension.
    """
    csv_files = []
    
    # Check if the path is a valid directory
    if os.path.isdir(directory):
        for file in os.listdir(directory):
            if file.endswith('.csv'):
                # Add the file name without extension
                csv_files.append(os.path.splitext(file)[0])
    else:
        print(f'La ruta "{directory}" no es un directorio válido.')
    
    return csv_files