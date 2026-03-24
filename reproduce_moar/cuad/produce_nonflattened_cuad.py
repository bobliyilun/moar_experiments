import json
import pandas as pd
from pathlib import Path

input_path = Path("/Users/yilunli/Desktop/moar_experiments/moar_experiments/data/test/test.json")
output_path = Path("/Users/yilunli/Desktop/moar_experiments/moar_experiments/data/test/test_data_list.json")

# 1) load raw json
raw = input_path.read_text(encoding="utf-8").strip()
if not raw:
    print("Empty input file; writing []")
    output_path.write_text("[]", encoding="utf-8")
    raise SystemExit(0)

root = json.loads(raw)

# 2) get data payload
if "data" not in root:
    raise KeyError(f"'data' key not found in {input_path}")

data_list = root["data"]

# optional check: if data is not list, convert/wrap
if not isinstance(data_list, list):
    data_list = [data_list]

# 3) optional: normalize as dataframe (if nested objects)
df = pd.json_normalize(data_list)

# 4) export list under data as JSON list (raw items)
output_path.write_text(json.dumps(data_list, indent=2, ensure_ascii=False), encoding="utf-8")
print("Saved data list to:", output_path)
print("rows:", len(data_list))