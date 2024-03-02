"""ex_5_2.py
This module contains an entry point that

- loads data from a file ex_5_2-data.csv into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called ex_5_2-processed.csv
"""
import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"
    data = np.loadtxt(INFILE, delimiter=',')
    data_mean_zero = data - np.mean(data)
    processed = data_mean_zero / np.std(data_mean_zero)
    np.savetxt(OUTFILE, processed, delimiter=',')