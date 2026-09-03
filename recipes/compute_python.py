# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
out_prep_by_name = dataiku.Dataset("out_prep_by_name")
out_prep_by_name_df = out_prep_by_name.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_df = out_prep_by_name_df # For this sample code, simply copy input to output


# Write recipe outputs
python = dataiku.Dataset("python")
python.write_with_schema(python_df)
