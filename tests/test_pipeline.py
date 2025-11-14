#Testes simples para o pipeline ETL
#Simple tests for the ETL pipeline

import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.extract import extract_data
import logging