
import os
import argparse
import subprocess

def save_and_version(csv_path, commit_msg, remote='datos'):
    """
    Guarda un archivo CSV, lo versiona con DVC y sincroniza los cambios 
    con el repositorio remoto de Git y el almacenamiento remoto configurado.

    Parámetros:
        csv_path (str)     : Ruta del archivo CSV a versionar.
        commit_msg (str)   : Mensaje del commit que se realizará en Git.
        remote (str)       : Nombre del almacenamiento remoto configurado en DVC (por defecto 'datos').
    """
    if not os.path.exists(csv_path):
        print(f"El archivo {csv_path} no existe.")
        return

    # 1) Agregar el archivo al control de versiones de DVC
    subprocess.run(["dvc", "add", csv_path], check=True)

    # 2) Preparar y confirmar los cambios en Git
    dvc_file = csv_path + ".dvc"
    subprocess.run(["git", "add", dvc_file, ".gitignore"], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

    # 3) Subir los datos al almacenamiento remoto y sincronizar con el repositorio Git
    subprocess.run(["dvc", "push", "-r", remote], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

    print("Archivo versionado con DVC y sincronizado con el repositorio remoto.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guardar y versionar un archivo CSV con DVC y Git.")
    parser.add_argument("csv_path", help="Ruta del archivo CSV a versionar.")
    parser.add_argument("commit_msg", help="Mensaje del commit de Git.")
    parser.add_argument("--remote", default="datos", help="Nombre del almacenamiento remoto de DVC (por defecto 'datos').")
    args = parser.parse_args()

    save_and_version(args.csv_path, args.commit_msg, args.remote)
