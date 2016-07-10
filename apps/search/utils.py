import os

# Use this module to define all the global variables that could be used in multiple modules
APP_NAME = os.path.basename(os.path.dirname(__file__))

# Attributes used in this model
BASE_SCORE_ATTR = 1.0

# The global variables given below are used in request.query_params. We will keep the names of parameters
# similar to model attributes, wherever possible.
Q_PARAM = 'q'
