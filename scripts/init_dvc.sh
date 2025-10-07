
# Bloque de inicialización y configuración de DVC con almacenamiento remoto en Google Drive

echo "Inicializando DVC..."
dvc init

echo "Agregando remote 'datos' en Google Drive..."
dvc remote add -d datos gdrive://1VnjNYOpP2uSaaUtFdRzW45iwZJUbt-5v

echo "Configurando credenciales OAuth..."
dvc remote modify datos gdrive_client_id '426582966437-3ni4029llgejof826h2pktmkk4elcm6j.apps.googleusercontent.com'
dvc remote modify datos gdrive_client_secret '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'

echo "Lista de remotes configurados:"
dvc remote list

echo "Agregando archivos al área de preparación de Git..."
git add .

echo "Creando commit de inicialización..."
git commit -m "Init DVC"
