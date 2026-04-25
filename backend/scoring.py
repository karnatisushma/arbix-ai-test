def calculate_score(data):
    score = 0
    reasons = []

    # Repayment score (50%)
    score += data.repayment_history_score * 0.5
    if data.repayment_history_score > 75:
        reasons.append("good_repayment")
    else:
        reasons.append("poor_repayment")

    # Land area
    if data.land_area_acres > 5:
        score += 20
        reasons.append("large_landholding")
    else:
        score += 10
        reasons.append("small_landholding")

    # Income band
    if data.annual_income_band == ">10L":
        score += 20
        reasons.append("high_income")
    elif data.annual_income_band == "5-10L":
        score += 15
        reasons.append("mid_income")
    elif data.annual_income_band == "2-5L":
        score += 10
        reasons.append("lower_mid_income")
    else:
        score += 5
        reasons.append("low_income")

    score = min(100, round(score, 2))

    return score, reasons[:3]