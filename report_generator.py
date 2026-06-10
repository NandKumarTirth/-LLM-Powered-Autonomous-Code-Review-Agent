from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(results, filename="code_review_report.pdf"):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    score = results["score"]

    if score >= 90:
        status = "Excellent"
        grade = "A"
    elif score >= 70:
        status = "Good"
        grade = "B"
    elif score >= 50:
        status = "Fair"
        grade = "C"
    else:
        status = "Needs Improvement"
        grade = "D"

    content = []

    title = Paragraph(
        "AUTONOMOUS CODE REVIEW REPORT",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 20))

    summary_data = [
        ["Metric", "Value"],
        ["Total Lines", str(results["total_lines"])],
        ["Functions", str(results["functions"])],
        ["Classes", str(results["classes"])],
        ["Quality Score", f"{score}%"],
        ["Grade", grade],
        ["Status", status]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[220, 220]
    )

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ])
    )

    content.append(Paragraph("Review Summary", styles["Heading1"]))
    content.append(summary_table)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Issues Detected",
            styles["Heading1"]
        )
    )

    if results["issues"]:
        for i, issue in enumerate(results["issues"], start=1):
            content.append(
                Paragraph(
                    f"{i}. {issue}",
                    styles["Normal"]
                )
            )
    else:
        content.append(
            Paragraph(
                "No issues detected.",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "AI Recommendations",
            styles["Heading1"]
        )
    )

    if results["recommendations"]:
        for rec in results["recommendations"]:
            content.append(
                Paragraph(
                    f"• {rec}",
                    styles["Normal"]
                )
            )
    else:
        content.append(
            Paragraph(
                "No recommendations. Code quality looks good.",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "Final Verdict",
            styles["Heading1"]
        )
    )

    if grade == "A":
        verdict = "Excellent code quality with only minor improvements suggested."
    elif grade == "B":
        verdict = "Good code quality with a few improvements recommended."
    elif grade == "C":
        verdict = "Moderate code quality. Refactoring is recommended."
    else:
        verdict = "Code requires significant improvements."

    verdict_table = Table(
        [[verdict]],
        colWidths=[440]
    )

    verdict_table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
            ("PADDING", (0, 0), (-1, -1), 10),
        ])
    )

    content.append(verdict_table)

    doc.build(content)

    return filename