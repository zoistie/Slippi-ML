from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    pdf = canvas.Canvas(output_file, pagesize=letter)
    pdf.setFont("Courier", 10)  # Fixed-width font
    width, height = letter
    y = height - 40

    for line in lines:
        pdf.drawString(40, y, line.strip())
        y -= 12
        if y < 40:  # Start a new page if needed
            pdf.showPage()
            pdf.setFont("Courier", 10)
            y = height - 40

    pdf.save()

# Example usage
create_pdf("src\game_to_csv.py", "output.pdf")
