# OpenStreetMap

I analyzed data from OpenStreetMap to gain insights into the Greater Salt Lake City metropolitan area.

I explain how I addressed the requirements for this project below: 

### 1.	A pdf document containing your answers to the rubric questions. This file should document your data wrangling process. 

I kept the answers to these questions in mind as I performed my data auditing and cleaning:

#### 1.1 Does the code function as expected?
        My code takes the large, raw dataset of the Greater Salt Lake City Metropolitan Area (.32 GB) and creates a smaller sample file (.013 GB) that can be analyzed. The code then audits the data and cleans the data as it is converted from XLM data to CSV data. Then I run SQL queries to better understand the data. All of these work as desired.   

#### 2.1 Does project utilize good coding practices?
        I attempted to follow standard coding conventions as I wrote my scripts. I'm sure a more advanced coder could do what I did using using more efficient code.

#### 3.1 Is the code commented in a way that is useful and not superfluous?
        I think it is. I used a jupyter notebook to organize my code, and I provided comments about what each piece of code is doing. 

#### 4.1 Does the project document the challenges encountered during the wrangling?
        I provided commentary on problematic data I found. I then address these issues programmtically later in my code. 

#### 5.1 Is data cleaned programmatically?
        Yes. Please see answer to previous question. 

#### 6.1 Is the OSM XML large enough?
        yes. The uncompressed OSM XML is 325MB. The requirement was that it must be larger than 50 MB.  

#### 7.1 Are overview statistics of the dataset computed?
        Yes, these are provided in the "Exploring the Database" portion of my jupyter notenook. 

#### 8.1 Are the database queries documented?
        They are. Please see the OpenStreetMap_Project IPYNB file in this repository. 

#### 9.1 Are ideas for additional improvements included?
        I suggest areas for future research in the "Conclusions" section. 

#### 10.1 Are benefits and problems with additional improvements discussed?
         Yes. I discuss how making the additional analysis will require some extra computing power than I currently have. 

#### 11.1 Is the submission long enough to answer the questions?
         I think so. If anything, the submission is too long! :D 

### 2.	Your Python code you used in auditing and cleaning your dataset for the final project. You may also include the original Case Study scripts, but make sure it is clear which code was used for the project, and which applies to the lesson quizzes. We recommend including a Readme file to describe the contents of each file you include in your submission.

         All of my code in contained in the OpenStreetMap_Project IPYNB file in this GitHub repository. 

### 3.	A text file containing a link to the map position you wrangled in your project, a short description of the area and a reason for your choice.

         I extracted my OSM file using MapZen. Unfortunately, as of February, 2018, MapZen stopped their service. The area I chose was the Greater Salt Lake City Metropolitan Area because I live there. 

### 4.	An .osm file containing a sample part of the map region you used (around 1 - 10 MB in size). See the notes below.

         I have included a sample file in this GitHub repository. It is 13 MB 

### 5.	A text file containing a list of Web sites, books, forums, blog posts, github repositories etc that you referred to or used in this submission (Add N/A if you did not use such resources).

         The references I used for the project are the SQL lessons in the Data Wrangling module as well as the Udacity forums and my Udacity mentor. 
 





