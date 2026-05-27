import os
import pytest
from lab2.main import solve_variant_1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DIR = os.path.join(BASE_DIR, "tests")

if os.path.exists(TEST_DIR):
    input_files = sorted([f for f in os.listdir(TEST_DIR) if f.startswith("input_") and f.endswith(".txt")])
else:
    input_files = []

@pytest.mark.parametrize("input_file", input_files)
def test_variant_1_outputs(input_file):
    input_path = os.path.join(TEST_DIR, input_file)
    output_file = input_file.replace("input_", "output_")
    output_path = os.path.join(TEST_DIR, output_file)
    
    result = solve_variant_1(input_path)
    res_id, res_gc = result.strip().split("\n")
    
    with open(output_path, "r", encoding="utf-8") as f:
        expected_lines = [line.strip() for line in f.read().splitlines() if line.strip()]
    
    expected_id = expected_lines[0]
    expected_gc = expected_lines[1]
    
    assert res_id == expected_id
    assert float(res_gc) == pytest.approx(float(expected_gc), abs=1e-6)
