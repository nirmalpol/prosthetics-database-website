from app import app
from flask import render_template, url_for, flash, redirect, request
from flask import jsonify
from flask import send_file, send_from_directory
import os
import time
from io import BytesIO
import zipfile
import shutil

allFiles = None

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

''' Acquire file paths from javascript code for the user's selected files.
    Store the names of the paths of these files. The /return_files function
    will return the actual file paths once the user clicks the download button.'''
@app.route('/handle_data', methods=['POST'])
def handle_data():
    global allFiles
    data = request.get_json()
    for i in range(len(data)):
        filename = data[i]
        filename = filename.replace('../', '')
        filename = filename.replace('/', '\\')
        
        allFiles = filename[0:-9]
    print(allFiles)
    return jsonify(status="success", data=data)


@app.route('/return_files/', methods=['POST'])
def return_files():

    global allFiles
    file_path = os.getcwd() + '\\app\\' + allFiles
    print(os.getcwd())
    print(file_path)
    return send_file(shutil.make_archive('myFiles', 'zip', file_path),
                    attachment_filename='myFiles.zip',
                    as_attachment=True)



@app.route('/About')
def toAboutPage():
    return render_template('About.html')

@app.route('/Contact')
def toContactPage():
    return render_template('Contact.html')

@app.route('/Disclaimer')
def toDisclaimerPage():
    return render_template('Disclaimer.html')
