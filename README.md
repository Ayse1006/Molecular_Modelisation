# Molecular_Modelisation
## Context
This project is an exercise on 3D molecular modeling using Blender.
We modeled the release of neurotransmitters from a vesicle which are goinf to bond with ions in order to form a new molecules called complexe. These complexes are going to attach to closed transmembrane receptors and thus open them.

## Requirement
In order to implement this project the following softwares need to be downloaded :
* Blender version 2.79 : https://download.blender.org/release/Blender2.79/
* Mcell version 3.4 and  Cellblender version 1.1 : https://mcell.org/download_previous.html
* For the second part  Python version 3.7 : https://www.python.org/downloads/

## Usage
### setting Blender
For the first launch of blender, importing cellblender is needed. It allows to have the cellblender menu needed for the project.
Do not forget to change the pathway of the mcell file in tha initialisation.py script (line 46).
**initialisation.py** has all the functions needed in order to build and set up all the parameters for the simulation.

### Launching simulation
To launch the simulation, the script has to be opened in blender. To do that default view has to be changed to scripting view.
Open the **initialisation.py** and run it *(Text > Run script)*.
The figures will be showed in the windows. In the cellblender window all the paramters should be filled up.
Don't forget to save the blender file in order to go on.
To run the simulation go to *(Cellblender > Run simulation )*. But before the seed number should be set to 10. This will launch 10 simulations. Go to *(Run simulation > Output/Control Options)* and change the End Seed to 10.
All that is need to do is *(Export & Run)*

### Creating graphs
When the simulation is runed, blender will create a new folder with the same name as the blender file. In this folder there are multiple 
files and folder but only a few of them will be used to create the graphs.
**statistics.py** should be put put inside the new folder. 
Then with an access to a terminal in the new folder, run the script `$ python statistic.py``
The output should be like the following : 
![Alt text](Result/result_graph.png?raw=true "Title")
There are 1 graph for each molecules. The mean and standard deviation are shown in the figure.

## Results
![](./Result/result_gif.gif)
You can find the result video from blender in the **Result** folder

## Contribution 
You can find our report by clicking on the following link : https://fr.overleaf.com/read/htjbxxbkvmxx

