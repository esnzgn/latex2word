from pathlib import Path
import re

# Load the LaTeX file
latex_path = Path("/mnt/data/main.tex")
latex_text = latex_path.read_text()

# Basic LaTeX to plain text conversion
def latex_to_text(latex):
    # Remove comments
    latex = re.sub(r"(?<!\\)%.*", "", latex)
    # Remove preamble and begin/end document
    latex = re.sub(r"\\documentclass.*?\\begin{document}", "", latex, flags=re.DOTALL)
    latex = re.sub(r"\\end{document}", "", latex)
    # Replace sections
    latex = re.sub(r"\\section\*?{(.+?)}", r"\n\n# \1\n", latex)
    latex = re.sub(r"\\subsection\*?{(.+?)}", r"\n\n## \1\n", latex)
    latex = re.sub(r"\\subsubsection\*?{(.+?)}", r"\n\n### \1\n", latex)
    # Remove LaTeX commands
    latex = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:{[^}]*})?", "", latex)
    # Replace common special characters
    latex = latex.replace("~", " ")
    latex = latex.replace("``", '"').replace("''", '"')
    # Remove multiple newlines
    latex = re.sub(r"\n\s*\n", "\n\n", latex)
    return latex.strip()

plain_text = latex_to_text(latex_text)
plain_text[:2000]  # Show a preview of the converted content
