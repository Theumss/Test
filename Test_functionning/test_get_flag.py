import pytest
from unittest.mock import patch
from io import BytesIO
from PIL import Image

def test_get_flag_image_success():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/320px-Flag_of_France.svg.png"
    
    # Simuler une réponse valide de requests.get
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"fake image data"
        
        # Test de la fonction
        result = get_flag_image(url)
        assert isinstance(result, ImageTk.PhotoImage)  # Vérifie que l'image est bien retournée
        
def test_get_flag_image_failure():
    url = "https://invalid.url"
    
    # Simuler une réponse invalide de requests.get
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404  # Erreur de chargement
        
        # Test de la fonction
        result = get_flag_image(url)
        assert result is None  # La fonction doit retourner None en cas d'erreur