# Smart-Voting-system-Using-IrisRecognition
<br>

This is a python project for Windows. This code does not work on MacOS and still needs some development. 
Before getting started with the project, there are few libraries that needs to be installed. 
This project shows a voting system based on Unique Aadhar and Iris Recognition. 
The system iimplementation is shown below:

&emsp; &emsp; &emsp; &emsp;&emsp; &emsp; <img width="442" alt="Screen Shot 2021-04-15 at 3 52 25 AM" src="https://user-images.githubusercontent.com/80937013/114834594-b3b04780-9d9e-11eb-94e3-80bec156950d.png">


The above figure depicts our proposed system model. In this model, the admin can login and add the nominees and voters to the
database. Moreover, the admin can view the nominee and voters' details and election results. The voter will also login with valid voter id and Iris images, and he/she can poll the vote if authenticated successfully, otherwise denied. 

# DESIGN :
<br>

The design of the system is primarily divided into two functionalities: Admin and voters. In the system, the admin, once given access, can operate various functions like adding a nominee, voters, and their iris images. Admin can also view results. When it comes to the voter, the only action that is allowed is casting a vote. Voters can log in with valid credentials such as Smart-ID and iris.

In this project, the iris recognition process is done in the following way:

1-> HOUGH TRANSFORMATION

2-> DOUGMAN'S RUBBER SHEET MODEL

3-> CANNY EDGE

4-> HAMMING DISTANCE(If the bit shifting is 0, i.e., Hamming distance is 0, it is a perfect match. If it is 0.5 or more, then the two strings are different.)

The idea of data flow diagrams is to perform system analysis efficiently. The figure below shows how the system is going to be performed.
# Flow Diagram :
<br>

![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/4ed3b7fa-2800-49b9-a2a6-3092b0625303)


PYQT5:It is a set of Python bindings for Qt libraries which are used to create cross-platform applications with a robust graphical user interface (GUI). PyQt5 allows developers to create applications for Windows, macOS, and Linux with the same codebase. Some of elements are Widgets,Layouts,Events,Dialogs,Graphics View Framework

OpenCV: The Open Source Computer Vision Library, is a powerful toolkit for working with images and videos in Python. Below is a comprehensive guide to getting started with OpenCV in Python, covering installation, basic usage, and some advanced features.

Matplotlib:This is a widely used plotting library in Python that allows you to create static, interactive, and animated visualizations. It provides a wide range of plotting capabilities, including line plots, scatter plots, bar charts, histograms, and more. Matplotlib integrates well with other libraries such as NumPy, pandas, and SciPy.

Scikit-image: This is a powerful library in Python for image processing. It is built on top of NumPy, SciPy, and Matplotlib and provides a wide range of image processing tools, including filtering, morphology, feature detection, and more. Here's a comprehensive guide to getting started with scikit-image.

# OUTPUT :
<br />
Output will look like

![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/a387b998-1999-4cbe-a0fe-df46238cd01f)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/f7696f89-f221-4311-a2d5-37bf1b39b93f)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/bf3174c3-9cd1-477d-8e87-cfe2ae197627)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/814917f2-fd8b-47c5-aea8-772a2058236b)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/9ba849d5-b2c6-4c71-ace4-dc61bef49fae)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/99def5ff-2eeb-4082-b2cf-304b138b4209)


![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/83504d34-5e53-4bd4-b6b9-aa070e087767)

> [!NOTE]  
> # Steps of Iris Recognition

<br>

![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/5c7d0d07-102e-4fd5-afef-40124af31679)

> [!NOTE]  
> # Algo of Image Processing
<br>

![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/e3f3243b-8815-400f-954b-8cf8de87b26a)

> [!NOTE]  
> # Architecture of Image Processing
<br>

![image](https://github.com/MauryaTejash/Smart-Voting-System-Using-IrisRecognition/assets/93006244/eb6b9544-94f5-47e3-835a-e72cb14d15dd)

<br />

# This is the complete project and its working which is well-defined in this file,follow the instruction to run the complete code in efficient way.
# $${\color{lightblue}Thanku \space Team \space memebers}$$
