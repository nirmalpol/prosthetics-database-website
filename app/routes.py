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
    
    filename = data[0]
    filename = filename.replace('../', '')
    filename = filename[0:-10]

    allFiles = filename.split('/')
    allFiles.insert(0, "app")

    return jsonify(status="success", data=data)

@app.route('/return_files/', methods=['POST'])
def return_files():

    global allFiles
    
    file_path = os.getcwd()
    
    for i in range(len(allFiles)):
        file_path = os.path.join(file_path, allFiles[i])
    
    try:
        # For MAC OS and Linux
        return send_file(shutil.make_archive('DesignFiles', 'zip', file_path+"/"),
                    attachment_filename='DesignFiles.zip',
                    as_attachment=True)
    except:
        # For Windows
        return send_file(shutil.make_archive('DesignFiles', 'zip', file_path+"\\"),
                    attachment_filename='DesignFiles.zip',
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
