# 🔬 Horikx Diagram Calculator

<div align="center">

![Horikx Diagram Logo](path-to-logo) <!-- TODO: Add a project logo, perhaps a simplified Horikx diagram -->

[![GitHub stars](https://img.shields.io/github/stars/fmsalamanca/horikx-diagram?style=for-the-badge)](https://github.com/fmsalamanca/horikx-diagram/stargazers)

[![GitHub issues](https://img.shields.io/github/issues/fmsalamanca/horikx-diagram?style=for-the-badge)](https://github.com/fmsalamanca/horikx-diagram/issues)

[![GitHub license](https://img.shields.io/badge/license-Unspecified-lightgrey?style=for-the-badge)](LICENSE) <!-- TODO: Add LICENSE file if available -->

**Compute and visualize random and selective Horikx diagrams based on initial parameters.**

</div>

## 📖 Overview

This repository provides a Python-based computational tool for generating and visualizing Horikx diagrams. The Horikx diagram is a fundamental concept in polymer science, critical for understanding the degradation kinetics and structural changes in cross-linked polymer networks under various scission mechanisms. This tool is designed to empower researchers and students to accurately compute both **random** and **selective** scission curves, offering profound insights into how specific network parameters influence polymer degradation behavior.

Originating from an existing MATLAB implementation, this project has been meticulously converted to Python to enhance accessibility, facilitate integration into contemporary scientific workflows, and leverage the robust ecosystem of Python's scientific libraries. The repository includes a core Python script (`horikx.py`), a convenient pre-compiled Windows executable (`horikx.exe`), and a comprehensive Jupyter Notebook (`MatlabToPythonConversion.ipynb`) that meticulously details the underlying methodology, the MATLAB-to-Python conversion process, and serves as an interactive guide for parameter exploration.

## ✨ Features

-   **Random Scission Computation:** Accurately calculates Horikx curves under the assumption of random scission events across the polymer network.
-   **Selective Scission Computation:** Generates Horikx curves specifically for scenarios involving selective scission, where certain bonds are preferentially broken.
-   **Parameter-Driven Analysis:** Users can define and modify key initial polymer network parameters (e.g., initial crosslink density, initial molecular weight, scission probabilities) to dynamically observe their impact on the degradation curves.
-   **Interactive Methodological Walkthrough:** The included Jupyter Notebook (`MatlabToPythonConversion.ipynb`) provides a step-by-step, interactive explanation of the mathematical models and computational procedures, allowing for direct experimentation and visualization.
-   **Standalone Executable:** A pre-compiled `horikx.exe` (specifically for Windows operating systems) offers a self-contained, convenient method to run calculations without requiring a local Python environment setup.
-   **Comprehensive Documentation:** Detailed user instructions and contextual information are provided in `instructions.pdf` and `instructions.docx` to guide users through the tool's application and theoretical background.

## 🛠️ Tech Stack

**Core Technologies:**
-   **Language:** Python
-   **Interactive Environment:** Jupyter Notebook

**Inferred Libraries (based on scientific computing nature):**
-   **Numerical Computation:** NumPy
-   **Scientific Computing:** SciPy
-   **Data Visualization:** Matplotlib

**Packaging:**
-   **Executable Generation:** PyInstaller (utilized for creating `horikx.exe`)

## 🚀 Quick Start

This section provides instructions for setting up your environment, exploring the scientific principles via the Jupyter Notebook, and executing the Horikx diagram computations.

### Prerequisites

-   Python 3.7 or newer (highly recommended)
-   Basic familiarity with command-line interfaces for executing scripts or programs.

### Installation (Python Environment)

To set up the Python environment and install necessary libraries:

1.  **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/fmsalamanca/horikx-diagram.git
    cd horikx-diagram
    ```

2.  **Create and activate a virtual environment** (recommended to manage dependencies):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install the required Python packages**:
    ```bash
    pip install numpy scipy matplotlib
    # Install Jupyter if you wish to run the notebook:
    pip install jupyter
    ```
    *Note: A `requirements.txt` file is not explicitly provided in the repository. The listed dependencies (`numpy`, `scipy`, `matplotlib`) are inferred as standard for projects involving scientific computation and visualization in Python.*

### Usage

The Horikx Diagram Calculator can be utilized in three primary ways:

#### 1. Running the Python Script (`horikx.py`)

The `horikx.py` script represents the core computational logic. It accepts parameters directly via the command line.

```bash

# Example: Execute the Python script with illustrative parameters

# The exact parameters depend on the implementation within horikx.py.

# Please inspect 'horikx.py' or 'MatlabToPythonConversion.ipynb'

# for precise parameter definitions, their order, and expected value types.
python horikx.py <parameter1_value> <parameter2_value> ...
```
*   **Parameter Guidance:** It is essential to refer to the source code of `horikx.py` or, more interactively, the `MatlabToPythonConversion.ipynb` Jupyter Notebook for a detailed explanation of the required input parameters, their physical meaning, and example usage.

#### 2. Interacting with the Jupyter Notebook (`MatlabToPythonConversion.ipynb`)

For an in-depth, interactive exploration of the methodology, parameter effects, and the MATLAB-to-Python conversion details:

1.  **Start Jupyter Lab or Jupyter Notebook** from the project's root directory:
    ```bash
    jupyter notebook
    # or
    jupyter lab
    ```
2.  In your browser, **open `MatlabToPythonConversion.ipynb`** from the Jupyter interface.
3.  **Execute the cells sequentially** to follow the computational flow, visualize intermediate and final results, and gain a comprehensive understanding of the Horikx diagram calculations. This notebook serves as the primary instructional and demonstrative resource.

#### 3. Using the Standalone Executable (`horikx.exe`)

For users on Windows who prefer to run the tool without a Python installation, a pre-compiled executable is provided:

```bash

# Navigate to the project directory in your command prompt or PowerShell
cd path/to/horikx-diagram

# Execute the application with the necessary parameters.

# The executable expects the same command-line arguments as the horikx.py script.

# Consult the Python script or Jupyter Notebook for parameter specifics.
.\horikx.exe <parameter1_value> <parameter2_value> ...
```

## 📁 Project Structure

```
horikx-diagram/
├── .ipynb_checkpoints/        # Internal directory used by Jupyter Notebooks
├── MatlabToPythonConversion.ipynb # Main Jupyter Notebook: detailed methodology, conversion, and interactive examples
├── horikx.exe                 # Pre-compiled Windows executable of the Horikx diagram calculator
├── horikx.py                  # Core Python script containing the Horikx diagram calculation logic
├── instructions.docx          # Official documentation and user guide (Microsoft Word format)
└── instructions.pdf           # Official documentation and user guide (Portable Document Format)
```

## ⚙️ Configuration & Parameters

The behavior and output of the Horikx diagram calculations are fundamentally driven by a set of input parameters. These parameters govern the initial characteristics of the polymer network and the specifics of the degradation process (e.g., initial chain length, crosslink density, scission probabilities).

These parameters are typically passed as command-line arguments when running `horikx.py` or `horikx.exe`. For a comprehensive understanding of the available parameters, their scientific significance, acceptable value ranges, and practical usage examples, it is **highly recommended** to:
1.  **Review the `MatlabToPythonConversion.ipynb` Jupyter Notebook** for an interactive and explanatory guide.
2.  **Examine the source code of `horikx.py`** to identify the exact parameter definitions and parsing logic.

## 📚 Documentation

Detailed user instructions, theoretical background, and guidance on parameter interpretation are available in the following external documents provided within this repository:

-   [`instructions.pdf`](instructions.pdf)
-   [`instructions.docx`](instructions.docx)

These documents are invaluable resources for gaining a deeper understanding of the Horikx diagram concept and effectively utilizing this computational tool.

## 🤝 Contributing

While this project primarily serves as a computational utility, contributions are welcome. If you encounter bugs, have suggestions for new features, or wish to propose improvements to the Python code or Jupyter Notebook, please feel free to:

-   **Report Issues:** Use the [GitHub Issues](https://github.com/fmsalamanca/horikx-diagram/issues) tracker.

### Development Setup for Contributors

To set up your environment for modifying the code:
1.  Follow the [Installation (Python Environment)](#installation-python-environment) steps outlined above.
2.  Make your desired changes to `horikx.py` or `MatlabToPythonConversion.ipynb`.
3.  Thoroughly test your modifications, ideally by comparing outputs against known theoretical results or the original MATLAB implementation's behavior.

## 📄 License

This project currently does not have an explicit open-source license defined. For licensing inquiries or permission to use, distribute, or modify the code, please contact the author directly.

<!-- TODO: Add a LICENSE file with an appropriate open-source license (e.g., MIT, Apache 2.0). -->

## 🙏 Acknowledgments

-   **Original Developers:** Credit to the creators of the original MATLAB implementation from which this Python version was converted.
-   **Open-Source Scientific Community:** Special thanks to the developers and communities behind NumPy, SciPy, and Matplotlib for providing the foundational libraries that make this scientific computation possible.
-   **Jupyter Project:** Appreciation for the Jupyter project, which enables interactive and reproducible scientific workflows.

## 📞 Support & Contact

-   🐛 **Report Issues:** Please use the [GitHub Issues](https://github.com/fmsalamanca/horikx-diagram/issues) page for bug reports and feature requests.
-   📧 **Author:** [fmsalamanca](https://github.com/fmsalamanca) <!-- TODO: Add specific contact email if direct contact is preferred -->

---

<div align="center">

**⭐ Star this repository if you find this tool valuable for your research or studies!**

Made with ❤️ by [fmsalamanca](https://github.com/fmsalamanca)

</div>
