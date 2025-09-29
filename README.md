# <p align="center">Climpact</p>

##  What is Climpact?
  
Climpact is an R package that calculates [indices of daily climate extremes](https://climpact-sci.org/indices/). It can read 
data for a single site (e.g. a weather station) in the form of a text file, or for gridded data (e.g. from a climate model) in the form of netCDF files. This software directly builds off the R packages climdex.pcic and climdex.pcic.ncdf, developed by the Pacific Climate Impacts Consortium ([PCIC](https://www.pacificclimate.org/)). 

*If you want to calculate these indices from text files then you **DO NOT** need to install this software, instead go to the [Climpact website](https://climpact-sci.org/get-started/) to calculate these indices online.*
  
  
##  Where can I get Climpact?
  
When calculating the indices for station data Climpact can be accessed [online](https://climpact-sci.org/get-started/). Climpact is also available for download at [this github site](https://github.com/ARCCSS-extremes/climpact) for users who wish to calculate the indices on gridded data or who wish to process station text files locally. The software runs on Windows, Linux and MacOS, though only on Linux and MacOS for gridded calculations.


## Documentation

See the [Climpact user guide](https://github.com/ARCCSS-extremes/climpact/blob/master/www/user_guide/Climpact_user_guide.md) for detailed instructions on using Climpact.


## How do I install Climpact?

If you do not wish to use the [online version](https://climpact-sci.org/get-started/) of Climpact then you can install it locally noting the following software requirements:  
* R version 3.3 or later. You will need administrator privileges on your computer or the ability to install R packages.
* Linux users wanting to calculate indices on gridded data require the *PROJ4* development files (libproj-dev package on Ubuntu) and the [*udunits*](https://www.unidata.ucar.edu/software/udunits/) development files (libudunits2-dev package on Ubuntu).

<br/>

1. Download and extract [this file](https://github.com/ARCCSS-extremes/climpact/archive/master.zip) to your computer.
   This will create a directory named "climpact-master".

2. Install the required R-packages. This step can take several minutes and only needs to be done once.

   In Windows: open R and select "File->Change dir..." and select the
   climpact-master directory created in step 1. Then type:  

```
   source('server/climpact.master.installer.r')
```

   In Linux/MacOS: in a terminal window navigate to the climpact-master directory created in
   step 1, then open R (by typing ```R``` at the command line) and type:  

```
   source('server/climpact.master.installer.r')
```

   You may be asked whether you would like to make a personal library, in 
   most cases the answer should be 'yes'. Once complete, quit R by typing
   ```q()```. 
   
<br/>

##  How do I start Climpact once I've installed it on my computer?

**In Windows**, open R and select "File->Change dir..." and select the 
climpact-master directory created when installing Climpact. **In Linux/MacOS**, open a terminal and navigate to the climpact-master directory created when installing Climpact, then open R (by typing ```R``` at the command line). 

Once inside R, run the following commands:

```
library(shiny) 
runApp()
```

Follow the on-screen instructions to calculate the Climpact indices.

##  ADVANCED: Calculate indices from netCDF data (Linux/MacOS only)

**Warning:** Calculating and using the gridded indices requires familiarity with the command line and netCDF files.

**Warning:** Due to an error in the SPEI and SPI package these indices will not be
correct for gridded data IF your data contain missing values (e.g. they are based on remote sensing observations).
    
1) Navigate to the climpact-master directory created when installing Climpact. Then modify the *climpact.ncdf.wrapper.r* file to suit your needs (see user guide
   for optional parameters to specify). 
   
2) Execute the above script by entering the following command at the command line:

```
   Rscript climpact.ncdf.wrapper.r
```

   Depending on the size of your data and the number of cores selected, this process
   can take anywhere from one hour to weeks to complete (if you don't have appropriate resources). As a
   yard stick, for a 20 year global ~1x1 degree dataset and a computer with 2 cores you should assign ~30 hours to begin with. Then adjust your expectations from there.

### Notes on netCDF file format:
* Files must be CF compliant.
* Look at the [sample netCDF file](https://github.com/ARCCSS-extremes/climpact/raw/master/www/sample_data/climpact.sampledata.gridded.1991-2010.nc) for an example of how to correctly structure your file. Most climate model output will be compatible with Climpact.
* There must be no 'bounds' attributes in your latitude or 
  longitude variables.
* Your precipitation variable must have units of "kg m-2 d-1",
  not "mm/day". These are numerically equivalent.
* Your minimum and maximum temperature variables must be 
  uniquely named.
* The *ncrename*, *ncatted* and *ncks* commands from the NCO package can help 
  you modify your netCDF files.
  http://nco.sourceforge.net/


##  ADVANCED: Calculate thresholds from netCDF data (Linux/MacOS only)

1) Navigate to the climpact-master directory created when installing Climpact. Then modify the *climpact.ncdf.thresholds.wrapper.r* file to suit your needs (see user guide for guidance on the parameters to specify). 
   
2) Then execute this file by running ```Rscript climpact.ncdf.thresholds.wrapper.r``` from the command line. Depending
   on the size of your data and the number of cores selected, this process
   can take anywhere from one to many hours.


## ADVANCED: Batch process multiple station files from the command line

1) Navigate to the climpact-master directory created when installing Climpact. 
       
2) From the terminal run the following command, replacing the flags
   with: the folder where your station text files are kept, a metadata file
   containing the file name of each station text file along with relevant 
   station information (see the [sample](https://github.com/ARCCSS-extremes/climpact/raw/master/www/sample_data/climpact.sample.batch.metadata.txt) provided), the beginning and end years of the base period, and
   the number of cores to use in processing, respectively. See the user guide
   for more information.

```
   Rscript climpact.batch.stations.r ./www/sample_data/ ./www/sample_data/climpact.sample.batch.metadata.txt 1971 2000 2
```


##  Common problems

* If you experience trouble installing R packages in Windows, try to disable
  your antivirus software temporarily.
* If you are trying to use the wrapper scripts in Windows anyway, ensure your PATH
  environment variable is changed to include the installation directory of R.


## Having trouble?

Make sure you read the relevant part of the [user guide](https://github.com/ARCCSS-extremes/climpact/blob/master/www/user_guide/Climpact_user_guide.md). Otherwise, search and/or submit an [issue](https://github.com/ARCCSS-extremes/climpact/issues).


##  Contact
  
climdex.climpact@gmail.com
