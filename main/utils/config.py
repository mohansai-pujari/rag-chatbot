import configparser

config = configparser.ConfigParser()
config.read('config.properties')

GEMINI_API_KEY = config.get('LLM_MODELS', 'GEMINI_API_KEY')
MODEL_NAME = config.get('LLM_MODELS', 'MODEL_NAME')

SAMPLE_ANGEL_ONE_WEB_LINKS = config.get('DATA_SOURCES', 'SAMPLE_ANGEL_ONE_WEB_LINKS')

CHUNK_SIZE = config.getint('PARTIOTION_PROPERTIES', 'CHUNK_SIZE')
CHUNK_OVERLAP = config.getint('PARTIOTION_PROPERTIES', 'CHUNK_OVERLAP')
TOP_K = config.getint('PARTIOTION_PROPERTIES', 'TOP_K')