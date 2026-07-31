from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER

heading_style = styles["Heading2"]
body_style = styles["BodyText"]

doc = SimpleDocTemplate("output/vendor-risk-memo.pdf")

story = []

story.append(Paragraph("Vendor Risk Assessment Memo", title_style))

story.append(Paragraph("<b>Vendor:</b> PeopleFlow Inc.", body_style))
story.append(Paragraph("<b>Assessment:</b> UBI – The Root Access Network – GRC Analyst Stage 6", body_style))
story.append(Paragraph("<b>Intern Code:</b> UBI-2026-0017", body_style))
story.append(Paragraph("<b>Variant:</b> D4", body_style))
story.append(Paragraph("<b>Evidence Marker:</b> UBI-A6-BC7742481B33", body_style))

story.append(Paragraph("Executive Summary", heading_style))
story.append(Paragraph(
    "A technical and governance assessment was performed using the supplied "
    "vendor questionnaire, assurance documentation, contractual commitments, "
    "and machine-readable telemetry exports. Several inconsistencies were "
    "identified between vendor claims and observed technical evidence.",
    body_style,
))

story.append(Paragraph("Key Findings", heading_style))
findings = [
    "TLSv1.0 observed on a public endpoint.",
    "Privileged administrative activity without MFA.",
    "Duplicate privileged access event identifiers.",
    "Broken privileged access audit hash chain.",
    "Regional processing inconsistent with vendor claims.",
    "Incomplete deletion evidence.",
]
for item in findings:
    story.append(Paragraph(f"• {item}", body_style))

story.append(Paragraph("Risk Summary", heading_style))
story.append(Paragraph(
    "Overall vendor risk is assessed as Medium-High. The most significant "
    "issues relate to transport encryption, privileged access controls, "
    "audit log integrity, and regional processing assurances.",
    body_style,
))

story.append(Paragraph("Recommendations", heading_style))
recommendations = [
    "Require TLS 1.2 or higher.",
    "Enforce phishing-resistant MFA for privileged accounts.",
    "Implement immutable audit logging with integrity validation.",
    "Clarify approved processing regions.",
    "Require evidence of backup deletion.",
    "Adopt the proposed monitoring plan before production onboarding.",
]
for rec in recommendations:
    story.append(Paragraph(f"• {rec}", body_style))

story.append(Paragraph("Decision", heading_style))
story.append(Paragraph(
    "<b>Conditional Approval.</b> Vendor onboarding should proceed only after "
    "the identified findings are remediated and the recommended contractual "
    "controls are implemented.",
    body_style,
))

doc.build(story)

print("✅ Created output/vendor-risk-memo.pdf")
