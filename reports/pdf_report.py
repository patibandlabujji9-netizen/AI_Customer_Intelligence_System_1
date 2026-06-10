# reports/pdf_report.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(df):
    """
    Generate PDF report from dataframe.
    Returns PDF file path.
    """

    # Create output folder
    output_folder = "generated_reports"
    os.makedirs(output_folder, exist_ok=True)

    pdf_path = os.path.join(
        output_folder,
        "sales_report.pdf"
    )

    # Create PDF
    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(
        Paragraph(
            "AI Sales Forecasting Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Summary
    content.append(
        Paragraph(
            f"Total Records: {len(df)}",
            styles["Normal"]
        )
    )

    if "Sales" in df.columns:
        content.append(
            Paragraph(
                f"Total Sales: {df['Sales'].sum():,.2f}",
                styles["Normal"]
            )
        )

    if "Profit" in df.columns:
        content.append(
            Paragraph(
                f"Total Profit: {df['Profit'].sum():,.2f}",
                styles["Normal"]
            )
        )

    if "Quantity" in df.columns:
        content.append(
            Paragraph(
                f"Total Quantity: {df['Quantity'].sum()}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 20))

    # Dataset Preview
    content.append(
        Paragraph(
            "Dataset Preview",
            styles["Heading2"]
        )
    )

    preview_text = df.head().to_string()

    content.append(
        Paragraph(
            preview_text.replace("\n", "<br/>"),
            styles["Code"]
        )
    )

    # Build PDF
    doc.build(content)

    return pdf_path