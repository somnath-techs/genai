from django.shortcuts import render
from core.utils import extract_text_from_pdf
from core.gemini import gemini_text_summerization
# Create your views here.


def home(request):
    response = "Upload PDF file to get summerization report"
    if request.method == "POST" and request.FILES['file']:
        pdf_file = request.FILES['file']
        text = extract_text_from_pdf(pdf_file)
        # if pdf_file:
        #     print("PDF file accepted")
        # print(text)
        response = gemini_text_summerization(text)
        print(response)
        context = {
            "response":response
        }
    else:
        context = {
            "response":response
        }
    return render(request, "index.html", context)