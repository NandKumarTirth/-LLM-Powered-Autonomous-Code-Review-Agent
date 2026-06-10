import ast

def analyze_code(file_content):
    results = {
        "total_lines": 0,
        "functions": 0,
        "classes": 0,
        "issues": [],
        "recommendations": [],
        "score": 100
    }

    lines = file_content.splitlines()
    results["total_lines"] = len(lines)

    try:
        tree = ast.parse(file_content)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                results["functions"] += 1

                if len(node.body) > 20:
                    results["issues"].append(
                        f"Function '{node.name}' is too long."
                    )

                if ast.get_docstring(node) is None:
                    results["issues"].append(
                        f"Function '{node.name}' is missing a docstring."
                    )

            elif isinstance(node, ast.ClassDef):
                results["classes"] += 1

        if results["functions"] == 0:
            results["issues"].append(
                "No functions found in code."
            )

        if results["total_lines"] > 200:
            results["issues"].append(
                "Large file detected. Consider splitting into multiple modules."
            )

        if results["functions"] > 10:
            results["issues"].append(
                "Too many functions in one file."
            )

    except Exception as e:
        results["issues"].append(
            f"Syntax Error: {str(e)}"
        )

    # AI Recommendations
    if any("docstring" in issue.lower() for issue in results["issues"]):
        results["recommendations"].append(
            "Add docstrings to improve code readability and maintainability."
        )

    if results["total_lines"] > 200:
        results["recommendations"].append(
            "Consider splitting the file into smaller modules."
        )

    if results["functions"] > 10:
        results["recommendations"].append(
            "Consider organizing related functions into classes."
        )

    # Quality Score
    score = 100
    score -= len(results["issues"]) * 10

    if score < 0:
        score = 0

    results["score"] = score
    if score >= 90:
        results["grade"] = "A"
        results["status"] = "Excellent"
    elif score >= 70:
        results["grade"] = "B"
        results["status"] = "Good"
    elif score >= 50:
        results["grade"] = "C"
        results["status"] = "Fair"
    else:
        results["grade"] = "D"
        results["status"] = "Needs Improvement"

    return results