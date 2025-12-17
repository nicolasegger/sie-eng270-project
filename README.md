# CMT
## Project Description
The prupose of the project is to highlight potentials heat islands based on a simple satelite picture using Stefan's law as a model.
## Input files
The first file used by the programm is the satelite picture.
Furthermore, the file pixel.py creates 2 csv files (albedo_matrix.csv & emmissivity_matrix.csv) and a pixelised version of the satelite image.

## Output files
The first file that is compiled by read_file.c is the file temperature_matrixe.csv that represent the temperature value of each pixel of the 100x100 pixelised image
The programm superposition.py uses this csv file to represent graphically the temperature map and the "hot zones" following the parametre hot_threshold
## Report
You can find the detailed report in the docs file.
# Running the program
## Dependencies
The programm uses Python 2.7.18 and C. It runs on Linux using the installed VDI. We used princippaly numpy libraries and matplotlib.
## Build
The C programm is compiled with a ``gcc`` command the the file ``read_file`` (executable) is create in the folder bin
Describe how the C program should be compiled (using gcc or mex). The executable or shared object file can be placed in the "bin/" directory.
## Execute
The programm can be executed directly from the terminal using the shellscript (app.sh file)
To compute the programm, the user has to move on the desktop to the place where the project is downloaded with the command : "cd $(find . -name "CMT" -type d)".
Once in the right place, the execution can be completed with: "./app.sh".
Resume (once on the terminal):
1. cd $(find . -name "CMT" -type d)
2. ./app.sh
## Contributors
Nicolas Egger & Diego Dellamula
# Acknowledgments
## Data sources
We actually created our data ourself so we don't have data sources.
## Code
The code is mainly inspired by our ideas, our previous courses (ICC : pixelizing an image), from the website sieprog.ch for dealing with C, and the teachers webpage : https://stakahama.gitlab.io/sie-eng270/intro_Python_shellscripting.html for automation. We have to mention also that artificial intelligence helped us to debug and gave us suggestions.  

    
