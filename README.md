# A Prosthetics Selection tool for Recreational Activities

This is a project completed in the course BME489: Biomedical Systems Engineering Design.

## Project Motivation

There are millions of people living with upper extremity amputations. Access to terminal end prosthetic devices is limited due to their high cost and it is often times not covered by insurance. Furthermore, there is a sharp learning curve required for users who want a customized/customizable prosthetic devices. The customization aspect (e.g. size, shape, load-bearing attributes, applications) is important as it can allow users to participate in various different activities (prosthetic for holding tennis racket vs prosthetic for basketball). 

As a result, an open source database full of customizable prosthetic CAD files is a desirable cost-effective solution for individuals who would like to 3D print their own simple terminal end prosthetic devices.

## Need Statement

A website to provide **open-source** 3D-printable **recreational terminal devices** to individuals with **upper limb amputations** and that reduces the costs of obtaining a prosthetic while allowing size scaling for children and adults

## Project Description

The prototype can be found at the following link (note it may take a few seconds to load): https://terminaldevicedatabaseapp.herokuapp.com/

Website was completed in html, css, and javascript languages using the Flask application.

### Choosing an Recreational Activity

When the user comes to the page, they are greeted with a short "How to use" that is straightforward and simple. The user first begins by selecting what recreational activity they are interested in so that a suitable prosthetic can be provided for that activity.

<p align="center">
  <img 
    width="500"
    height="300"
    src="/assets/choose_an_activity.png"
  >
</p>

The images of the recreational activity dynamically change once the user selects an activity. This helps the user correctly identify their selection so they do not misinterpret their selection.

### Customization Options

After selecting the recreational activity, the user can now select which side of the body and what size they need to customize the prosthetic file. Once the customizations are complete, the user can click submit and receive their 3D STL file for printing.

<p align="center">
  <img 
    width="500"
    height="500"
    src="/assets/customization_options.png"
  >
</p>

The customization table for size is presented to explain the different measurements available and help the user understand the relevance to their age so they understand which size to select. The customization table changes values based on selected recreational activity. The diagram is a cartoon mockup that visually show which dimension the measurements are referring in the table to help guide the user.

### Preview/Downloading

The user receives a link to the 3D file for printing by clicking the download button.

<p align="center">
  <img 
    width="500"
    height="600"
    src="/assets/download_file.png"
  >
</p>

The user is also presented with a canvas preview based on a cross-platform 3D modeling open-source library of Three.js. This allows the users to rotate, zoom in/out, and drag the file around so that the user can verify and see their file prior to downloading.

The cost and time details are mentioned for every material depending on chosen recreational activity and selected customization features.

## Bugs/Defects

**Software Bugs/Defects:**
- Unable to rotate/pan files in Safari but can zoom in and out; updates correctly; download correctly
- On Windows, view slightly shifts based on whether a side scrollbar is present or not
- With the way it is setup, only one user should interact with the prototype at a time as two users making selections can lead to the wrong files being sent to the users

**Other Issues:**
- Users may be confused that canvas does not update unless ‘Submit’ is explicitly pressed again 
- Users may like to directly change certain dimensions of the file for their needs

## Future Considerations

Currently, the prototype design is able to present the user with options for the type of recreational activity, the side of the body, and the size for the prosthetic device. Then the user receives the selected file. The backend does not automatically do any of these customizations on the fly. The team had to manually create all possible design files and customization options and put them in our database so that the backend only needs to select the right file based on the user's selections. 

If the project were to be scaled up with multiple types of prosthetics as well as more customizable features, it will be difficult to manually create and keep all the prosthetic CAD files up to date. A software solution that interacts and manipulates the CAD files would be a better option for future considerations.


