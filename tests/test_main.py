import csv
import json
import tempfile
import unittest
from pathlib import Path
from main import csv_to_json, json_to_csv


class BridgeTests(unittest.TestCase):
    def test_json_to_csv_flattens_nested_objects(self):
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp)/"in.json", Path(tmp)/"out.csv"
            source.write_text(json.dumps([{"user":{"name":"Ada"},"score":7}]), encoding="utf-8")
            self.assertEqual(json_to_csv(source,target),1)
            with target.open(encoding="utf-8",newline="") as handle:
                row=next(csv.DictReader(handle))
            self.assertEqual(row["user.name"],"Ada")
            self.assertEqual(row["score"],"7")

    def test_csv_to_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            source,target=Path(tmp)/"in.csv",Path(tmp)/"out.json"
            source.write_text("name,city\nAda,London\n",encoding="utf-8")
            self.assertEqual(csv_to_json(source,target),1)
            self.assertEqual(json.loads(target.read_text(encoding="utf-8"))[0]["city"],"London")


if __name__ == "__main__":
    unittest.main()
