import configparser
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()

try:
    config.read('config.properties')
except configparser.MissingSectionHeaderError as e:
    logger.error(f"Config file error: Missing section headers in 'config.properties'. Please add section headers. Details: {e}")

def get_config_value(section, key, fallback=None, value_type=str):
    try:
        if value_type == int:
            return config.getint(section, key, fallback=fallback)
        elif value_type == float:
            return config.getfloat(section, key, fallback=fallback)
        elif value_type == bool:
            return config.getboolean(section, key, fallback=fallback)
        else:
            return config.get(section, key, fallback=fallback)
    except configparser.NoSectionError as e:
        logger.warning(f"Config section [{section}] not found: {e}. Using fallback for {key}: {fallback}")
        return fallback
    except configparser.NoOptionError as e:
        logger.warning(f"Config key '{key}' not found in section [{section}]: {e}. Using fallback: {fallback}")
        return fallback
    except Exception as e:
        logger.error(f"Unexpected error retrieving config [{section}] -> {key}: {e}. Using fallback: {fallback}")
        return fallback


# Example usage (unchanged)
GEMINI_API_KEY = get_config_value('LLM_MODELS', 'GEMINI_API_KEY', fallback='AIzaSyA1rWAGh_SQTZdiYcno2-3NuTMSkpmuohY')
MODEL_NAME = get_config_value('LLM_MODELS', 'MODEL_NAME', fallback='gemini-1.5-flash')
SAMPLE_ANGEL_ONE_WEB_LINKS = get_config_value('DATA_SOURCES', 'SAMPLE_ANGEL_ONE_WEB_LINKS', fallback='https://www.angelone.in/support')
CHUNK_SIZE = get_config_value('PARTIOTION_PROPERTIES', 'CHUNK_SIZE', fallback=1000, value_type=int)
CHUNK_OVERLAP = get_config_value('PARTIOTION_PROPERTIES', 'CHUNK_OVERLAP', fallback=100, value_type=int)
TOP_K = get_config_value('PARTIOTION_PROPERTIES', 'TOP_K', fallback=5, value_type=int)
