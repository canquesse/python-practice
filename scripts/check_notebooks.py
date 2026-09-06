"""Execute the small, pure-Python exercise cells in order with isolated namespaces."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
for path in sorted(root.rglob("*.ipynb")):
    if any(part.startswith(".") for part in path.relative_to(root).parts):
        continue
    notebook = json.loads(path.read_text())
    namespace = {"__name__": "__main__"}
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            source = "".join(cell["source"])
            exec(compile(source, f"{path.name}:cell-{index}", "exec"), namespace)
    print(f"PASS {path.relative_to(root)}")
