import json
import os

# Caminho para o arquivo JSON
DATA_FILE_PATH = os.getenv('JOKES_FILE_PATH', os.path.join('data', 'jokes.json'))

def load_jokes():
    try:
        with open(DATA_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"en": {}, "pt-br": {}}  # Retorna um dicionário vazio se o arquivo não for encontrado
    except json.JSONDecodeError:
        raise ValueError("Erro ao decodificar o arquivo JSON de piadas.")

def get_joke(language, level):
    jokes = load_jokes()

    # Verifica se o nível de humor existe na lista
    if level not in jokes[language]:
        level = 'medium'

    return jokes[language][level][0]
