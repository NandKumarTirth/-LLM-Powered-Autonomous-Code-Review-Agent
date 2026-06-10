import streamlit as st
from analyzer import analyze_code
from report_generator import generate_report

st.set_page_config(
    page_title="Autonomous Code Review Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Code Review Agent")
st.write("Upload a Python file and get an automated code review.")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    results = analyze_code(code)

    # Metrics
    st.subheader("📊 Analysis Results")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Lines", results["total_lines"])

    with col2:
        st.metric("Functions", results["functions"])

    with col3:
        st.metric("Classes", results["classes"])

    with col4:
        st.metric("Quality Score", f"{results['score']}%")

    with col5:
        st.metric("Grade", results.get("grade", "N/A"))

    # Quality Score
    st.progress(results["score"] / 100)

    # Review Status
    status = results.get("status", "Unknown")

    if status == "Excellent":
        st.success("✅ Status: Excellent")
    elif status == "Good":
        st.info("ℹ️ Status: Good")
    elif status == "Fair":
        st.warning("⚠️ Status: Fair")
    else:
        st.error("❌ Status: Needs Improvement")

    # Source Code
    st.subheader("📄 Uploaded Code")
    st.code(code, language="python")

    # Detected Issues
    st.subheader("⚠ Issues Found")

    if results["issues"]:
        for issue in results["issues"]:
            st.warning(issue)
    else:
        st.success("No major issues found! Great job. 🎉")

    # AI Suggestions
    st.subheader("🧠 AI Recommendations")

    if results["recommendations"]:
        for rec in results["recommendations"]:
            st.info(rec)
    else:
        st.success("No recommendations. Code quality looks good!")

    # PDF Export
    pdf_file = generate_report(results)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="code_review_report.pdf",
            mime="application/pdf"
        )