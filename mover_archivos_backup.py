import os
import shutil

def move_files_to_parent_folder(folder):
    # Iterar sobre todas las subcarpetas en la carpeta actual
    for subfolder_name in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder_name)
        
        # Verificar si es una subcarpeta
        if os.path.isdir(subfolder_path):
            for root, dirs, files in os.walk(subfolder_path, topdown=False):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    parent_folder = os.path.basename(folder)
                    destination_folder = folder
                    
                    # Crear la carpeta de destino si no existe
                    os.makedirs(destination_folder, exist_ok=True)
                    
                    destination = os.path.join(destination_folder, file_name)

                    try:
                        # Mover el archivo a la carpeta raíz correspondiente
                        shutil.move(file_path, destination)
                        print(f"Archivo movido: {file_path} -> {destination}")
                    except FileNotFoundError as e:
                        print(f"Error al mover {file_path}: {e}")
                    except Exception as e:
                        print(f"Ocurrió un error inesperado al mover {file_path}: {e}")

def process_all_folders(root_dir):
    # Iterar sobre todas las carpetas dentro de la carpeta raíz
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        # Verificar si es una carpeta
        if os.path.isdir(folder_path):
            move_files_to_parent_folder(folder_path)

# Ruta a la carpeta raíz
root_directory = r'C:\path\to\your\folder'

# Ejecutar la función para procesar todas las carpetas
process_all_folders(root_directory)