import csv
import os
import sys
from agfield_client import AgFieldClient


def main():
    # Default to http://127.0.0.1:5000 (local mock server)
    base_url = os.environ.get("AGFIELD_API_URL", "http://127.0.0.1:5000")
    client = AgFieldClient(base_url=base_url)

    # Path to synthetic CSV (relative to this script)
    csv_path = os.path.join(os.path.dirname(__file__), "../../examples/synthetic/practice_logs.csv")

    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found. Run: python tools/generate_synthetic_data.py")
        sys.exit(1)

    print(f"Reading {csv_path}...\n")

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 1):
            text = row.get("text", "")
            farmer_id = row.get("farmer_id", "unknown")
            
            try:
                result = client.parse_practice(text)
                parsed = result.get("structured", {})
                print(f"[{i}] Farmer: {farmer_id}")
                print(f"    Input: {text[:60]}...")
                print(f"    Parsed: {parsed}\n")
            except Exception as e:
                print(f"[{i}] Error parsing: {e}\n")


if __name__ == "__main__":
    main()
