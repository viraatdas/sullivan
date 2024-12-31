from sullivan.optimization.OptimizationInterface import OptimizationInterface
from Cython.Build import cythonize
from setuptools import setup, Extension
import os
import subprocess
import sys

class CythonOptimization(OptimizationInterface):
    def __init__(self, file_path):
        self.file_path = file_path

    def optimize(self):
        """
        Applies Cython optimization to the specified Python file.
        """
        print(f"Applying Cython optimization to {self.file_path}")
        
        # Check if the file exists
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} not found.")
            return
        
        # Generate the Cython module
        self._cythonize_file(self.file_path)

    def _cythonize_file(self, py_file):
        """
        Convert a Python file to a C extension module using Cython.
        """
        # Prepare the extension module
        ext_modules = cythonize([Extension(name=os.path.splitext(py_file)[0], sources=[py_file])])

        # Create a setup script dynamically
        setup_script = """
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("{0}", compiler_directives={{'language_level': "3"}}),
)
""".format(py_file)

        setup_file = "setup_cython.py"
        with open(setup_file, "w") as f:
            f.write(setup_script)

        # Run the setup script
        try:
            subprocess.check_call([sys.executable, setup_file, "build_ext", "--inplace"])
            print(f"Successfully compiled {py_file} with Cython.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to compile {py_file}: {e}")
        finally:
            # Clean up the setup script
            os.remove(setup_file)

    def get_name(self):
        return "Cython Optimization"
