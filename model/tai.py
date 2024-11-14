import google.generativeai as genai
API = 'AIzaSyDEVMep2BaFNpLYMNPVIIGRc0LGYQtVAFY'
genai.configure(api_key=API)
model = genai.GenerativeModel("gemini-1.5-flash")

myfile = genai.upload_file("test.jpg")
# print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile, "\n\n", "what's in the photo"]
)
print(f"{result.text=}")