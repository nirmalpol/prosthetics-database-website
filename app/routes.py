from app import app
from flask import render_template, url_for, flash, redirect, request

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

    ''' 
    TO DO ------------------------------------------------------------------
    Write logic to retrieve user responses from recreational activity and 
    customization option fields on html.

    The only difficult part is to incorporate the javascript code I created to 
    display the recreational activity images when user is hovering their mouse 
    over the selection.
    '''
    #activity_resp1 = request.form.get('<insert assigned html <name> value>')
    #cust_resp1 = request.form.get('<insert assigned html <name> value>')

    '''             
    TO DO ------------------------------------------------------------------
    User will have pressed submit button before receiving file. Check if any
    responses are missing or incorrectly filled out and present the messages
    '''
    
    '''             
    TO DO ------------------------------------------------------------------
    Display preview of numpy-stl on the canvas of the html code so that the user 
    can see what the file looks like on the website

    Include downloadable link to the preview file
    Include cost, time, image of the file and the user's selections
    '''


    return render_template('main.html')



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

@app.route('/About')
def toAboutPage():
    return render_template('About.html')

@app.route('/Contact')
def toContactPage():
    return render_template('Contact.html')