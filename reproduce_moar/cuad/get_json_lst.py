import json
from pathlib import Path

input_path = Path("/Users/yilunli/Desktop/moar_experiments/moar_experiments/data/test/test.json")
output_path = Path("/Users/yilunli/Desktop/moar_experiments/moar_experiments/data/test/cuad_test.json")

root = json.loads(input_path.read_text(encoding="utf-8"))
data_items = root.get("data", [])
if not isinstance(data_items, list):
    raise ValueError("Expected root['data'] to be a list")

result = []
for item in data_items:
    title = item.get("title", None)
    paragraphs = item.get("paragraphs", [])
    if not isinstance(paragraphs, list):
        continue
    for p in paragraphs:
        if isinstance(p, dict) and "context" in p:
            entry = {"context": p["context"]}
            result.append(entry)

output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print("Wrote", len(result), "paragraph contexts to", output_path)