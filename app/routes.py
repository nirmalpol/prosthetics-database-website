from app import app
from flask import render_template, url_for, flash, redirect, request
from flask import jsonify
from flask import send_file, send_from_directory
import os
import time
from io import BytesIO
import zipfile
import shutil

allFiles = []

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
    allFiles = []
    data = request.get_json()
    for i in range(len(data)):
        filename = data[i]
        filename = filename.replace('../', '')
        filename = filename.replace('/', '\\')
        
        allFiles.append(filename[0:-9])
    print(allFiles)
    return jsonify(status="success", data=data)


def database(parameters):
    '''
        Set parameters as a list object.
        Determine logic for deciding how to return user desired prosthetic file.

        
        Storage file directory
            - Recreational Activity 1
                - Left Hand
                    - File 1 L_B
                    - File 1 L_M
                    - File 1 L_S
                - Right Hand
                    - File 1 L_B
                    - File 1 L_M
                    - File 1 L_S

            - Recreational Activity 2
            - Recreational Activity 3

        EXAMPLE:
        Based on the parameters received, you will have identified the recreational activity,
        the handedness, and the size. Simply based on these three parameters, we could just
        have the function search the path and return:

        "/Recreational Activity 1/Left Hand/ File 1 L_B"
        
        We might not need to even have a SQL database. This could simplify the problem
        even further and maybe reconsider this approach later on.
        
    '''
@app.route('/return-files/')
def return_files():
    try:
        global allFiles
        file_path = os.getcwd() + '\\app\\' + allFiles[0]
    
        return send_file(shutil.make_archive('myFiles', 'zip', file_path),
                        attachment_filename='myFiles.zip',
                        as_attachment=True)
    except Exception as e:
        print(os.getcwd())
        return str(e)

@app.route('/About')
def toAboutPage():
    return render_template('About.html')

@app.route('/Contact')
def toContactPage():
    return render_template('Contact.html')

@app.route('/Disclaimer')
def toDisclaimerPage():
    return render_template('Disclaimer.html')
