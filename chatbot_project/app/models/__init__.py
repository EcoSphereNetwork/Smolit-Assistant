# models/__init__.py

# This file initializes the models package and can be used to import
# the relevant classes or functions to make them available at the package level.

# Import the router model so it's available directly via models.router_model
from .router_model import RouterModel

# Initialize and possibly configure logging if needed
import logging
logging.getLogger(__name__).info("Models package initialized.")

# If there's a need to load pre-trained models or configurations, it can be done here.
# Example: Preload a model if required across the app (uncomment if necessary)
# router_model_instance = RouterModel()
