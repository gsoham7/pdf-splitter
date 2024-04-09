from flask import Flask, render_template, request, send_file
from pdfsplitter import cropper as split_pdf

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("file_upload.html")

@app.route("/success", methods=["POST"])
def success():
    start = int(request.form.get('start', 0))

    end = int(request.form.get('end',0))
    f = request.files.get('file')

    if f is not None:
        filename = f.filename
        cropped_filename = split_pdf(start, end, filename)
        return render_template("download.html", filename=cropped_filename)
    else:
        # Handle the case where the file upload failed or the file field was missing
        # For example, you can return an error message or redirect the user to the upload page
        return "File upload failed or file field is missing."
    return render_template("success.html", start=start, end=end, name=filename)

@app.route("/convert", methods=["POST"])
def cropper():
    start = int(request.form.get('start', 0))

    end = int(request.form.get('end',0))
    f = request.files.get('file')

    if f is not None:
        filename = f.filename
        cropped_filename = split_pdf(start, end, filename)
        return render_template("download.html", filename=cropped_filename)
    else:
        # Handle the case where the file upload failed or the file field was missing
        # For example, you can return an error message or redirect the user to the upload page
        return "File upload failed or file field is missing."

    cropped_filename = split_pdf(start, end, file)
    return render_template("download.html", filename=cropped_filename)

@app.route("/download/<filename>")
def download(filename):
    return send_file(filename, as_attachment=True)


