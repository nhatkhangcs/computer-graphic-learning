import sys
import os

# Get the path to the 'src' directory (project root)
src_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(src_path)
