"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root
root_dir = get_repository_root()
data_dir = root_dir / "data"
output_dir = root_dir / "outputs"
input_file = data_dir / "ex_5_4-data.csv"
output_file = output_dir / "ex_5_4-processed.csv"
data = np.loadtxt(input_file, delimiter=',')
data[data < 0] = 0
np.savetxt(output_file, data, delimiter=',')