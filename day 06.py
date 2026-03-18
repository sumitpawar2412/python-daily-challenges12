def analyser(list):
    dict={"invalid":[],"normal":[],"large":[],"highrisk":[]}
    for amt in list:
        if amt <= 0:
            dict["invalid"].append(amt)
        elif amt <= 500:
            dict["normal"].append(amt)
        elif amt <= 2000:
            dict["large"].append(amt)
        else:
            dict["high_risk"].append(amt)
    valid_transactions = [x for x in transactions if x > 0]
    total_value = sum(valid_transactions)
    total_count = len(transactions)

    frequent_flag = total_count > 5
    large_spending_flag = total_value > 5000
    suspicious_flag = len(categories["high_risk"]) >= 3

    # Step 5: Risk Classification Logic
    risk_score = 0
    if frequent_flag:
        risk_score += 1
    if large_spending_flag:
        risk_score += 1
    if suspicious_flag:
        risk_score += 2

    if risk_score >= 3:
        risk_level = "High Risk"
    elif risk_score == 2:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    # Step 6: Tuple Summary
    summary = (total_count, total_value, risk_level)

    # Output
    print("\n--- Transaction Report ---")
    print("Categorized Transactions:")
    for key, value in categories.items():
        print(f"{key}: {value}")

    print("\nSummary:")
    print(f"Total Transactions: {summary[0]}")
    print(f"Total Value: {summary[1]}")
    print(f"Final Risk Level: {summary[2]}")

    return summary


# Example Run
data = [100, 700, 2500, 50, 3000, -20, 1200]
analyze_transactions(data)
