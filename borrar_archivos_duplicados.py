import os

def find_and_remove_duplicates(root_dir):
    seen_files = {}  # Diccionario para almacenar nombres de archivos y sus rutas
    
    # Iterar sobre todas las carpetas dentro de la carpeta raíz
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        # Verificar si es una carpeta
        if os.path.isdir(folder_path):
            # Recorrer archivos en la carpeta actual
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                
                if os.path.isfile(file_path):
                    # Ignorar archivos sin extensión
                    if '.' not in file_name:
                        print(f"Archivo ignorado (sin extensión): {file_path}")
                        continue

                    if file_name in seen_files:
                        try:
                            os.remove(file_path)
                        except PermissionError as e:
                            print(f"Permiso denegado al eliminar {file_path}: {e}")
                        except FileNotFoundError as e:
                            print(f"Error al eliminar {file_path}: {e}")
                        except Exception as e:
                            print(f"Ocurrió un error inesperado al eliminar {file_path}: {e}")
                    else:
                        seen_files[file_name] = file_path

# Ruta a la carpeta raíz
root_directory = r'C:\path\to\your\folder'

# Ejecutar la función para encontrar y eliminar archivos duplicados
find_and_remove_duplicates(root_directory)