import logging
from config import settings

# Configure module-level logging
logging.basicConfig(
    filename=settings.log_file,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.getLogger(__name__).info("App module initialized.")
