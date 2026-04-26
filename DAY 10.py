import copy
import math
import random
import numpy as np
import pandas as pd
ROLL_NUMBER = 569
STEP_SIZE = ROLL_NUMBER % 3 or 3
def build_students(count):
    students = []
    for student_id in range(1, count + 1):
        students.append(
            {
                "student_id": student_id,
                "marks": random.randint(40, 95),
                "attendance": random.randint(60, 100),
                "quiz_scores": [random.randint(10, 25), random.randint(10, 25)],
            }
        )
    return students
def to_dataframe(records):
    return pd.DataFrame(records)
def apply_mutation(records, step):
    for idx, record in enumerate(records):
        if idx % step == 0:
            current_marks = record["marks"]
            record["marks"] = round(current_marks + math.sqrt(current_marks), 2)
            record["attendance"] = min(record["attendance"] + 5, 100)
            record["quiz_scores"][0] += 2
            record["quiz_scores"][1] += 3
    return records
def summarize(records_before, records_after):
    before_marks = np.array([student["marks"] for student in records_before], dtype=float)
    after_marks = np.array([student["marks"] for student in records_after], dtype=float)

    mean_after = np.mean(after_marks)
    median_after = np.median(after_marks)
    std_after = np.std(after_marks)
    drift_amount = abs(np.mean(before_marks) - mean_after)

    manual_mean_after = sum(after_marks) / len(after_marks)
    normalized_after = (after_marks - np.min(after_marks)) / (
        np.max(after_marks) - np.min(after_marks)
    )
    return {
        "mean": mean_after,
        "median": median_after,
        "std_dev": std_after,
        "drift": drift_amount,
        "manual_mean": manual_mean_after,
        "normalized": normalized_after,
    }
def determine_status(drift, std_dev, shared_reference_detected):
    if shared_reference_detected:
        return "Copy Reference Issue"
    if drift > 7:
        return "Critical Distribution Drift"
    if drift > 3:
        return "Minor Distribution Drift"
    return "Data Stable"
if __name__ == "__main__":
    student_count = random.randint(10, 15)
    students = build_students(student_count)
    original_snapshot = copy.deepcopy(students)

    shallow = copy.copy(students)
    deep = copy.deepcopy(students)

    apply_mutation(shallow, STEP_SIZE)
    apply_mutation(deep, STEP_SIZE)

    shallow_df = to_dataframe(shallow)
    deep_df = to_dataframe(deep)
    original_df = to_dataframe(students)

    shared_reference_issue = any(
        students[i] != original_snapshot[i] for i in range(len(students))
    )
    analysis = summarize(original_snapshot, deep)
    status_message = determine_status(analysis["drift"], analysis["std_dev"], shared_reference_issue)

    print("=== Original Dataset ===")
    print(original_df)
    print("\n=== Shallow Copy Dataset ===")
    print(shallow_df)
    print("\n=== Deep Copy Dataset ===")
    print(deep_df)

    print(f"\nMean (deep copy)       : {analysis['mean']:.2f}")
    print(f"Median (deep copy)     : {analysis['median']:.2f}")
    print(f"Std Dev (deep copy)    : {analysis['std_dev']:.2f}")
    print(f"Manual Mean            : {analysis['manual_mean']:.2f}")
    print(f"Normalization vector   : {analysis['normalized']}")
    print(f"Drift between sets      : {analysis['drift']:.2f}")

    print("\nUnique student IDs:")
    print({student["student_id"] for student in students})
    print(f"\nResult summary tuple   : ({analysis['mean']:.2f}, {analysis['drift']:.2f}, {analysis['std_dev']:.2f})")
    print(f"System classification  : {status_message}")
