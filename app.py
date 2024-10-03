from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# HTML code with embedded file listing and delete functionality
html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Sharing App</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Share Files Between Devices</h1>
        
        <form action="/upload" method="post" enctype="multipart/form-data" class="text-center">
            <input type="file" name="file" class="form-control mb-3" style="display:inline-block; width:auto;">
            <input type="submit" value="Upload" class="btn btn-primary">
        </form>
        
        <h2 class="mt-5">Uploaded Files:</h2>
        <ul class="list-group">
        {% for file in files %}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <a href="/uploads/{{ file }}">{{ file }}</a>
                <form action="/delete/{{ file }}" method="post" style="display:inline;">
                    <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                </form>
            </li>
        {% else %}
            <li class="list-group-item">No files uploaded yet.</li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    # Get the list of files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(html_code, files=files)

# Route for uploading files
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('home'))

# Route to view uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route for deleting files
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('home'))
    except Exception as e:
        return f'Error deleting file: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
