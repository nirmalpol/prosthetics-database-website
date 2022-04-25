# A Prosthetics Selection tool for Recreational Activities

This is a project completed in the course BME489: Biomedical Systems Engineering Design.

## Project Motivation

There are millions of people living with upper extremity amputations. Access to terminal end prosthetic devices is limited due to their high cost and it is not covered by provincial insurance (OHIP). Furthermore, there is a sharp learning curve required for users who want a customized/customizable prosthetic devices. The customization aspect (e.g. size, shape, load-bearing attributes, applications) is important as it can allow users to participate in various different activities (prosthetic for holding tennis racket vs prosthetic for basketball). 

As a result, an open source database full of customizable prosthetic CAD files is a desirable cost-effective solution for individuals who would like to 3D print their own simple terminal end prosthetic devices.

## Need Statement

A website to provide **open-source** 3D-printable **recreational terminal devices** to individuals with **upper limb amputations** and that reduces the costs of obtaining a prosthetic while allowing size scaling for children and adults

## Project Description

The prototype can be found at the following link: https://terminaldevicedatabaseapp.herokuapp.com/

<p align="center">
  <img 
    width="300"
    height="300"
    src="/assets/choose_an_activity.png"
  >
</p>

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


