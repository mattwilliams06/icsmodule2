

import streamlit as st
import numpy as np
import time

# This Python file uses the streamlit framework to create a web application for ICS Module 2.
# Hosting this code in a web application allows students to access a user interface without 
# having access to to code itself. 
# Author: Matt Williams, matthew.j.williams@protonmail.com, 518-221-3267

st.title('ICS Module 2 Testing Simulator')
st.markdown('Please choose your vehicle configuration below, and click the button to commence testing.')
st.markdown('Each test takes 1.67 seconds to complete. 1000 tests will take 10 minutes.')


# setting the initial parameters
angle = 0.0
weight = 0
speed = 20
pk = 0.7
surv = 0.0
test_time = 1000/600 # seconds per test. 1000 tests takes 10 minutes

# Use streamlit to create drop-down menus to select the vehicle configuration
chassis = st.selectbox(
	'Select a chassis variant',
	('Tracked', 'Wheeled', 'Hover'))
st.write('You selected ', chassis.lower())

engine = st.selectbox(
	'Select an engine',
	('Mark1', 'Mark2', 'Mark3'))
st.write('You selected ', engine.lower())

weapon = st.selectbox(
	'Select a weapon configuration',
	('Rocket', 'Minigun', 'Both'))
st.write('You selected ', weapon.lower())

radar = st.selectbox(
	'Select a radar variant',
	('Standard', 'Upgraded', 'Enhanced'))
st.write('You selected ', radar.lower())

n_runs = int(st.text_input('Enter the number of tests to perform: ', value='1', key='runs'))

start = st.button('Begin Testing')

# Add a button to allow the user to commence the testing, which displays the progress bar and 
# will display the results after


if start:
    if chassis == 'wheeled':
	    weight += 1275
	    surv += 0.2
	    speed -= 3
	    angle += 22
	    surv += 0.85
	    pk += 0.01
    elif chassis == 'tracked':
	    weight += 1350
	    surv += 0.3
	    speed -= 5
	    angle += 25
	    surv += 0.9
	    pk += 0.02
    else: #hover
	    weight += 1200
	    surv += 0.
	    speed += 0
	    angle += 19
	    surv += 0.8

    if engine == 'Mark1': # baseline engine
	    speed += 0
	    weight += 0
	    angle += 0
	    surv += 0
    elif engine == 'Mark2':
	    speed += 10
	    weight += 100
	    angle += 1
	    surv += 0.02
	    pk += 0.01
    else: # Mark 3
	    speed += 20
	    weight += 150
	    angle += 1
	    surv = 0.03
	    pk += 0.02

    if weapon == 'rocket':
	    speed -= 3
	    weight += 75
	    pk += 0.05
	    angle -= 2
    elif weapon == 'minigun':
	    speed -= 2
	    weight += 50
	    pk += 0.03 
	    angle -= 1
    else: # both
	    speed -= 5
	    weight += 125
	    pk += 0.08
	    angle -= 3

    if radar == 'standard':
	    speed -= 1
	    weight += 50
	    pk += .01
	    angle -= 0

    elif radar == 'upgraded':
	    speed -= 2
	    weight += 60
	    pk += .02
	    angle -= 1
	    surv += 0.02
    else: # enhanced
	    speed -= 3
	    weight += 75
	    pk += .04
	    angle -= 2
	    surv += 0.03
	# Obtain the results from using normal distributions
    weight_std = np.random.uniform(0.1, 0.3)*weight
    weight_distro = np.random.normal(weight, weight_std, n_runs)
    weight_final = weight_distro.mean()
    speed_std = np.random.uniform(0.1, 0.3)*speed
    speed_distro = np.random.normal(speed, speed_std, n_runs)
    speed_final = speed_distro.mean()
    pk_std = np.random.uniform(0.1, 0.3)*pk
    pk_distro = np.random.normal(pk, pk_std, n_runs)
    pk_final = pk_distro.mean()
    angle_std = np.random.uniform(0.1, 0.3)*angle
    angle_distro = np.random.normal(angle, angle_std, n_runs)
    angle_final = angle_distro.mean()
    surv_std = np.random.uniform(0.1, 0.3)*angle
    surv_distro = np.random.normal(angle, angle_std, n_runs)
    surv_final = angle_distro.mean()
    latest_iteration = st.empty()
    my_bar = st.progress(0)
    for i in range(n_runs+1):
	    percent_cpl = int(i / n_runs * 100)
	    latest_iteration.text('Test {}/{}'.format(i, n_runs))
	    my_bar.progress(percent_cpl)
	    time.sleep(test_time)
    st.markdown('Testing results: ')
    st.markdown(f'Weight: {weight_final:.2f} kgs  \nSpeed: {speed_final:.2f} km/hr  \nPk: {pk_final:.2f}\
    	  \nAngle: {angle_final:.2f} deg')