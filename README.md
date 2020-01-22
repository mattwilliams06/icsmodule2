# ICS Module 2 and 3 Simulator
This is a repository of files needed to deploy the ICS Module 2 and 3 web app on Heroku. The requirements file contains all versions of packages used to build the application at the time of creation.

## Parameter calculation
The simulator computes parameters based upon the user input. Those computed parameters are then used as the basis for sampling a normal distribution. For example, after the user selects a configuration, the computed weight is used as the mean for a normal distribution whose standard deviation is randomly selected as somewhere between 0.1 and 0.3 times the weight. Finally, the number of samples from the constructed normal distribution is 100 times the number of tests selected by the user. 

So, if the user selects 6 tests, the algorithm will sample each parameter's normal distribution 600 times. If the computed weight based on configuration was 1000 kg, the normal distribution to be sampled will have a mean of 1000 kgs and a standard deviation of something between 100 and 300 kgs. 

## Run time
Each test is simulated as taking 10 minutes to complete. This is imposed by running a for loop where the variable of iteration loops over the total number of seconds (600 seconds * number of tests), and a 1 second sleep time is imposed within each loop iteration. The progress bar is designed to update every second, so that the user is able to track progress with more fidelity. There is a test count display, showing which test out of the number of total tests is complete. This is computed by integer division of the variable of iteration and 600 (the number of seconds per tests). In integer division, 599 // 600 = 0 (since everything less than 600 goes into 600 0 times), and 600 // 600 = 1. Then, the test counter won't increase again unil 1200.

## Web application deployment
The code for the simulator uses the Streamlit framework to assist in deploying Python code to a browser-based application that the user can interact with and diplay progress bars. Using Streamlit eliminates the need to additionally write HTML and CSS files. All documentation and tutorials regarding Streamlit can be found on streamlit.io. Streamlit is integrated with the Python code, and allows Python commands to create all the text boxes, drop-down menus, progress bars, etc.
