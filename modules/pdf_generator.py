from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(content):

    pdf_file = "grant_proposal.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = [Paragraph(content.replace("\n", "<br/>"), styles["BodyText"])]

    doc.build(story)

    return pdf_file