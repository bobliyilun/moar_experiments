import json
from typing import Any, Dict
from docetl.utils_evaluation import register_eval

@register_eval
def evaluate_results(dataset_file_path: str, results_file_path: str) -> Dict[str, Any]:
    """
    Evaluate medication extraction results.

    Checks if each extracted medication appears verbatim in the original transcript.
    In this example, the dataset has a 'src' attribute with the original input text.
    """
    # Load pipeline output
    with open(results_file_path, 'r') as f:
        output = json.load(f)

    total_correct_medications = 0
    total_extracted_medications = 0

    # Evaluate each result
    for result in output:
        # In this example, the dataset has a 'src' attribute with the original transcript
        original_transcript = result.get("src", "").lower()
        extracted_medications = result.get("medication", [])

        # Check each extracted medication
        for medication in extracted_medications:
            total_extracted_medications += 1
            medication_lower = str(medication).lower().strip()

            # Check if medication appears in transcript
            if medication_lower in original_transcript:
                total_correct_medications += 1

    # Calculate metrics
    precision = total_correct_medications / total_extracted_medications if total_extracted_medications > 0 else 0.0

    return {
        "medication_extraction_score": total_correct_medications,  # This is used as the accuracy metric
        "total_correct_medications": total_correct_medications,
        "total_extracted_medications": total_extracted_medications,
        "precision": precision,
    }