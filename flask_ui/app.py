from flask import Flask, request, render_template
import requests
 
app = Flask(__name__)
 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        prompt = request.form["prompt"]
       
        files = {
            'file': (file.filename, file.read(), file.content_type)
        }

        print(f"[DEBUG] Type of file file.read(): {type(file.read())}")

        data = {"prompt": prompt}

        print(f"DEBUG uploading file {file.filename} with prompt: {prompt}")
        try: 
            response = requests.post("http://localhost:8000/api/query", 
                        files=files,
                        data=data
            )
            print(f"This is the response :::: {response}")
            print(f"DEBUG FastAPI raw text: {response.text}")
            answer = response.json().get("result", "No result found")

        except Exception as e:
            print(f"[ERROR] {e}")
            answer = f"Error: {str(e)}"

        return render_template("index.html", answer=answer)


    return render_template("index.html")

 
if __name__ == "__main__":
    app.run(debug=True, port=5000)