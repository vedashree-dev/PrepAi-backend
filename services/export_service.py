def generate_html(paper, include_answer_key=False, is_premium=False):
    html = """
    <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; padding: 30px; }
                h1 { text-align: center; }
                h2 { margin-top: 30px; }
                p { margin: 10px 0; }
                strong { font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Question Paper</h1>
    """

    for idx, section in enumerate(paper):
        html += f"<h2>Section {chr(65 + idx)}: {section.topic}</h2>"
        for i, q in enumerate(section.questions, 1):
            html += f"<p><strong>{i}. ({q.marks} marks) [{q.type}]</strong> {q.question}</p>"
            if include_answer_key and is_premium and q.answer:
                html += f"<p><em>Answer:</em> {q.answer}</p>"

    html += "</body></html>"
    return html

def html2docx(html: str, filename: str) -> str:
    from bs4 import BeautifulSoup
    from docx import Document
    import os

    soup = BeautifulSoup(html, "html.parser")
    doc = Document()

    for p in soup.find_all("p"):
        doc.add_paragraph(p.get_text())

    output_path = os.path.join("generated", filename)
    os.makedirs("generated", exist_ok=True)
    doc.save(output_path)

    return output_path
