import pandas as pd
import streamlit as st
import numpy as np
import time

# This Python file uses the streamlit framework to create a web application for ICS Modules 2 and 3.
# Hosting this code in a web application allows students to access a user interface without 
# having access to to code itself. The web application is currently hosted on Heroku. 
# Author: Matt Williams, matthew.j.williams@protonmail.com, 518-221-3267

# Welcome heading, and create an input box for students to select module 2 or 3
st.title('ICS Module Testing Simulator')
st.header('Select a module to simulate:')
module = st.text_input('Type 2 or 3 into the box and press enter.')

### Module 2
if module == '2':
  st.title('ICS Module 2 Testing Simulator')
  st.markdown('Please choose your vehicle configuration below, and click the button to commence testing.')
  st.markdown('Each test takes 10 minutes to complete.')
  st.markdown('Your displayed results will be the averages of all of the prototype tests.')

  # setting the initial parameters
  angle = 0.0
  weight = 0
  speed = 20
  pk = 0.7
  surv = 0.0
  test_time = 600 # 10 minutes in seconds. 600 seconds per test

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
  
  # Change everything to lowercase for simplicity
  chassis = chassis.lower()
  engine = engine.lower()
  weapon = weapon.lower()
  radar = radar.lower()
  
  # Commence this section of code if the start button has been pressed
  # This adds and subtracts from parameters based on the selected configuration
  if start:
    if chassis == 'wheeled':
      weight += 1275
      surv += 0.2
      speed -= 3
      angle += 22
      surv += 0.85
      pk += 0.01
      net_ready = 4.9
      MTBF = 173.7
      MTTR = 4.7
      CPI = .92
      SPI = .92
      pd = 0.73
      vehicle_range = 18
    elif chassis == 'tracked':
      weight += 1350
      surv += 0.3
      speed -= 5
      angle += 25
      surv += 0.9
      pk += 0.02
      net_ready = 4.8
      MTBF = 185.2
      MTTR = 5.1
      CPI = 1.12
      SPI = 1.0
      pd = 0.75
      vehicle_range = 12
    else: #hover
      weight += 1200
      surv += 0.
      speed += 0
      angle += 19
      surv += 0.8
      net_ready = 4.4
      MTBF = 265.5
      MTTR = 6.7
      CPI = .88
      SPI = 0.86
      pd = 0.74
      vehicle_range = 12

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
      vehicle_range += 2
    else: # Mark 3
      speed += 20
      weight += 150
      angle += 1
      surv = 0.03
      pk += 0.02
      vehicle_range += 3

    if weapon == 'rocket':
      speed -= 3
      weight += 75
      pk += 0.05
      angle -= 2
      vehicle_range -= 1
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
      vehicle_range -= 2

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
    # Obtain the results using normal distributions
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
    surv_std = np.random.uniform(0.1, 0.3)*surv
    surv_distro = np.random.normal(surv, surv_std, n_runs)
    surv_final = surv_distro.mean()
    range_std = np.random.uniform(0.1, 0.3)*vehicle_range
    range_distro = np.random.normal(vehicle_range, range_std, n_runs)
    range_final = range_distro.mean()
    pd_std = np.random.uniform(0.1, 0.3)*pd
    pd_distro = np.random.normal(pd, pd_std, n_runs)
    pd_final = pd_distro.mean()
    net_ready_std = np.random.uniform(0.1, 0.3)*net_ready
    net_ready_distro = np.random.normal(net_ready, net_ready_std, n_runs)
    net_ready_final = net_ready_distro.mean()
    MTTR_std = np.random.uniform(0.1, 0.3)*MTTR
    MTTR_distro = np.random.normal(MTTR, MTTR_std, n_runs)
    MTTR_final = MTTR_distro.mean()
    MTBF_std = np.random.uniform(0.1, 0.3)*MTBF
    MTBF_distro = np.random.normal(MTBF, MTBF_std, n_runs)
    MTBF_final = MTBF_distro.mean()
    CPI_std = np.random.uniform(0.1, 0.3)*CPI
    CPI_distro = np.random.normal(CPI, CPI_std, n_runs)
    CPI_final = CPI_distro.mean()
    SPI_std = np.random.uniform(0.1, 0.3)*surv
    SPI_distro = np.random.normal(surv, surv_std, n_runs)
    SPI_final = surv_distro.mean()
    
    # Show a progress bar and the current test number
    # Delay the results based on the number of tests selected
    latest_iteration = st.empty()
    my_bar = st.progress(0)
    total_time = test_time * n_runs # total time in seconds
    for i in range(total_time + 1):
      percent_cpl = int(i / total_time * 100)
      latest_iteration.text('Test {}/{}'.format(i // 600, n_runs))
      my_bar.progress(percent_cpl)
      time.sleep(1)
    st.markdown('Testing results: ')
    st.markdown(f'Weight: {weight_final:.2f} kgs  \nSpeed: {speed_final:.2f} km/hr  \nPk: {pk_final:.2f}\
        \nAngle: {angle_final:.2f} deg  \nNet Ready: {net_ready_final:.1f} sec  \nPd: {pd_final:.3f} \
        \nSurvivability index: {surv_final:.3f}  \nMTTR: {MTTR_final:.1f} hours  \nMTBF: {MTBF_final:.1f} hours\
        \nCPI: {CPI:.3f}, \SPI: {SPI:.3f}')
### Module 3
elif module == '3':
  correct_pword = 'cellardoor'
  pword = st.text_input('Enter the password for Module 3: ')
  if pword == correct_pword:
    st.title('ICS Module 3 Testing Simulator')
    st.markdown('Please choose your vehicle configuration below, and click the button to commence testing.')
    st.markdown('Each test takes 10 minutes to complete.')

    # The following sections of code create the dataframes to store information
    # Creating the multi-level row indices per the Dragonfly Component Tradeoff Matrix
    # Active power data not currently included
    engine_index = pd.MultiIndex.from_tuples([('engine_size', 'weight'), ('engine_size', 'speed'), ('engine_size', 'cost')])
    frame_index = pd.MultiIndex.from_tuples([('frame', 'weight'), ('frame', 'survivability'), ('frame', 'cost')])
    armor_index = pd.MultiIndex.from_tuples([('armor', 'weight'), ('armor', 'survivability'), ('armor', 'cost')])

    # Creating the multi-level column indices per the Dragonfly Component Tradeoff Matrix
    # These commands are shortucts to creating the repetitive column labels. For example, each frame size has the 
    # option for a small, medium, and large engine.
    wheeled_engine_columns = pd.MultiIndex.from_product([['wheeled_small_frame', 'wheeled_medium_frame', 'wheeled_large_frame'],
                            ['small', 'medium', 'large']])
    wheeled_frame_columns = pd.MultiIndex.from_product([['wheeled_small_frame', 'wheeled_medium_frame', 'wheeled_large_frame'],
                            ['aluminum', 'composite', 'titanium']])
    wheeled_armor_columns = pd.MultiIndex.from_product([['wheeled_small_frame', 'wheeled_medium_frame', 'wheeled_large_frame'],
                            ['none', 'steel', 'tungsten']])

    tracked_engine_columns = pd.MultiIndex.from_product([['tracked_small_frame', 'tracked_medium_frame', 'tracked_large_frame'],
                            ['small', 'medium', 'large']])
    tracked_frame_columns = pd.MultiIndex.from_product([['tracked_small_frame', 'tracked_medium_frame', 'tracked_large_frame'],
                            ['aluminum', 'composite', 'titanium']])
    tracked_armor_columns = pd.MultiIndex.from_product([['tracked_small_frame', 'tracked_medium_frame', 'tracked_large_frame'],
                            ['none', 'steel', 'tungsten']])

    hover_engine_columns = pd.MultiIndex.from_product([['hover_small_frame', 'hover_medium_frame', 'hover_large_frame'],
                            ['small', 'medium', 'large']])
    hover_frame_columns = pd.MultiIndex.from_product([['hover_small_frame', 'hover_medium_frame', 'hover_large_frame'],
                            ['aluminum', 'composite', 'titanium']])
    hover_armor_columns = pd.MultiIndex.from_product([['hover_small_frame', 'hover_medium_frame', 'hover_large_frame'],
                            ['none', 'steel', 'tungsten']])

    # Data from the Dragonfly matrix, except for active power for the engines
    # First row is weight, third row is cost. Second row is component-dependent (see Dragonfly matrix).
    wheeled_engine_data = [[695, 756, 895, 705, 756, 895, 715, 756, 895],
                          [30, 35, 40, 25, 30, 35, 20, 25, 30],
                          [278, 347.5, 417, 347.5, 417, 486.5, 417, 486.5, 556]]
    wheeled_frame_data = [[224, 317, 405, 220, 320, 420, 240, 340, 440],
                         [80, 110, 140, 100, 110, 120, 110, 120, 130],
                         [417, 486.5, 556, 486.5, 556, 625.5, 556, 625.5, 695]]
    wheeled_armor_data = [[0, 135, 380, 0, 140, 380, 0, 145, 380],
                        [0, 85, 250, 0, 90, 250, 0, 95, 250],
                        [0, 417, 486.5, 0, 486.5, 556, 0, 556, 625.5]]

    tracked_engine_data = [[705, 775, 910, 715, 785, 920, 725, 795, 930],
                         [14, 16, 18, 12, 14, 16, 10, 12, 14],
                         [417, 486.5, 556, 486.5, 556, 625.5, 556, 625.5, 695]]
    tracked_frame_data = [[200, 300, 400, 210, 310, 410, 220, 320, 420],
                         [70, 100, 130, 75, 105, 135, 80, 110, 140],
                         [556, 625.5, 695, 625.5, 695, 764.5, 556, 625.5, 695]]
    tracked_armor_data = [[0, 130, 370, 0, 135, 380, 0, 140, 390],
                        [0, 80, 240, 0, 85, 250, 0, 90, 260],
                        [0, 556, 625.5, 0, 625.5, 695, 0, 695, 764.5]]

    hover_engine_data = [[670, 735, 885, 675, 750, 895, 680, 765, 905],
                        [25, 30, 35, 20, 25, 30, 15, 20, 25],
                        [347.5, 417, 486.5, 417, 486.5, 556, 486.5, 556, 625.5]]
    hover_frame_data = [[220, 310, 400, 225, 315, 405, 230, 320, 410],
                       [75, 105, 135, 80, 110, 140, 85, 115, 145],
                       [486.5, 556, 625.5, 556, 625.5, 695, 625.5, 695, 764.5]]
    hover_armor_data = [[0, 125, 175, 0, 130, 180, 0, 135, 185],
                       [0, 75, 200, 0, 80, 225, 0, 85, 250],
                       [0, 486.5, 556, 0, 556, 625.5, 0, 625.5, 695]]

    rocket_data = [[0, 42, 43, 44, 45, 46],
                  [0, 80, 90, 100, 110, 120],
                  [0, 156, 173.5, 191, 208.5, 226]]

    minigun_data = [[0, 40, 41, 42, 43, 44],
                   [0, 10, 20, 30, 40, 50],
                   [0, 138.5, 156, 173.5, 191, 208.5]]

    laser_missile_data = [[0, 44, 45, 46, 47, 48],
                         [0, 80, 90, 100, 110, 120],
                         [0, 173.5, 191, 208.5, 226, 243.5]]

    grenade_data = [[0, 37, 38, 39, 40, 41],
                   [0, 50, 55, 60, 65, 70],
                   [0, 103.5, 121, 138.5, 156, 173.5]]

    targeting_comp_data = [[0, 41, 43, 45, 47, 49],
                        [0, 1.1, 1.12, 1.15, 1.175, 1.2],
                        [0, 173.5, 191, 208.5, 226, 243.5]]

    # creating the dataframes, three per variant (engine, frame, and armor)
    wheeled_engine_df = pd.DataFrame(data=wheeled_engine_data,
              index=engine_index,
              columns=wheeled_engine_columns)

    wheeled_frame_df = pd.DataFrame(data=wheeled_frame_data,
              index=frame_index,
              columns=wheeled_frame_columns)

    wheeled_armor_df = pd.DataFrame(data=wheeled_armor_data,
              index=armor_index,
              columns=wheeled_armor_columns)

    tracked_engine_df = pd.DataFrame(data=tracked_engine_data,
              index=engine_index,
              columns=tracked_engine_columns)

    tracked_frame_df = pd.DataFrame(data=tracked_frame_data,
              index=frame_index,
              columns=tracked_frame_columns)

    tracked_armor_df = pd.DataFrame(data=tracked_armor_data,
              index=armor_index,
              columns=tracked_armor_columns)

    hover_engine_df = pd.DataFrame(data=hover_engine_data,
              index=engine_index,
              columns=hover_engine_columns)

    hover_frame_df = pd.DataFrame(data=hover_frame_data,
              index=frame_index,
              columns=hover_frame_columns)

    hover_armor_df = pd.DataFrame(data=hover_armor_data,
              index=armor_index,
              columns=hover_armor_columns)

    # Create the drop-down menus for user input
    chassis = st.selectbox(
      'Select a chassis variant',
      ('Tracked', 'Wheeled', 'Hover'))
    st.write('You selected ', chassis.lower())

    frame_size = st.selectbox(
      'Select a vehicle frame size',
      ('Small', 'Medium', 'Large'))
    st.write('You selected ', frame_size.lower())

    engine_size = st.selectbox(
      'Select an engine size',
      ('Small', 'Medium', 'Large'))
    st.write('You selected ', engine_size.lower())

    frame = st.selectbox(
      'Select a frame material',
      ('Aluminum', 'Composite', 'Titanium'))
    st.write('You selected ', frame.lower())

    armor = st.selectbox(
      'Select armor',
      ('None', 'Steel', 'Tungsten'))
    st.write('You selected ', armor.lower())

    chassis = chassis.lower()
    frame_size = frame_size.lower()
    engine_size = engine_size.lower()
    frame = frame.lower()
    armor = armor.lower()

    st.markdown('Please select the weapon configuration below.')
    st.markdown('MK1 variants provide the lowest performance, while MK5 provides the highest.')
    st.markdown('The laser-guided missile requires a targeting computer to be installed in order to obtain higher lethanlity than a free rocket.')

    rocket = st.selectbox(
      'Rocket variant',
      ('None', 'MK1', 'MK2', 'MK3', 'MK4', 'MK5'))
    st.write('You selected ', rocket)

    minigun = st.selectbox(
      'Minigun variant',
      ('None', 'MK1', 'MK2', 'MK3', 'MK4', 'MK5'))
    st.write('You selected ', minigun)

    laser_guided_missile = st.selectbox(
      'Laser-guided missile variant',
      ('None', 'MK1', 'MK2', 'MK3', 'MK4', 'MK5'))
    st.write('You selected ', laser_guided_missile)

    grenade = st.selectbox(
      'Grenade-launcher variant',
      ('None', 'MK1', 'MK2', 'MK3', 'MK4', 'MK5'))
    st.write('You selected ', grenade)

    targeting_computer = st.selectbox(
      'Targeting computer variant',
      ('None', 'MK1', 'MK2', 'MK3', 'MK4', 'MK5'))
    st.write('You selected ', targeting_computer)

    rocket = rocket.lower()
    minigun = minigun.lower()
    laser_guided_missile = laser_guided_missile.lower()
    grenade = grenade.lower()
    targeting_computer = targeting_computer.lower()

    n_runs = int(st.text_input('Enter the number of tests to perform: ', value=1, key='runs'))

    start = st.button('Begin Testing')

    # Function for selecting the data based on chassis-related input
    def get_chassis_data(chassis, frame_size, engine_size, frame, armor):
      if chassis == 'wheeled':
        engine_df = wheeled_engine_df
        frame_df = wheeled_frame_df
        armor_df = wheeled_armor_df
      elif chassis == 'tracked':
        engine_df = tracked_engine_df
        frame_df = tracked_frame_df
        armor_df = tracked_armor_df
      else: #chassis == 'hover':
        engine_df = hover_engine_df
        frame_df = hover_frame_df
        armor_df = hover_armor_df
      # getting data from the dataframes 
      col1 = chassis + '_' + frame_size + '_' + 'frame'
      col2 = [col for col in (engine_size, frame, armor)]
      engine_weight, speed, engine_cost = engine_df[col1][col2[0]].values
      frame_weight, frame_surv, frame_cost = frame_df[col1][col2[1]].values
      armor_weight, armor_surv, armor_cost = armor_df[col1][col2[2]].values

      surv = (frame_surv + armor_surv) / (260 + 140) # fraction of max possible value  
      weight = engine_weight + frame_weight + armor_weight
      cost = engine_cost + frame_cost + armor_cost

      return weight, speed, surv, cost

    # Function for selecting data related to the weapon configuration
    def accessory_data(rocket, minigun, laser_missile, grenade, targeting_comp):
      column_dict = {'none': 0, 'mk1': 1, 'mk2': 2, 'mk3': 3, 'mk4': 4, 'mk5': 5}
      rocket_weight, rocket_damage, rocket_cost = [rocket_data[col][column_dict[rocket]] for col in range(len(rocket_data))]
      minigun_weight, minigun_damage, minigun_cost = [minigun_data[col][column_dict[minigun]] for col in range(len(minigun_data))]
      laser_missile_weight, laser_missile_damage, laser_missile_cost = [laser_missile_data[col][column_dict[laser_missile]] for col in range(len(laser_missile_data))]
      grenade_weight, grenade_damage, grenade_cost = [grenade_data[col][column_dict[grenade]] for col in range(len(grenade_data))]
      targeting_comp_weight, targeting_comp_damage, targeting_comp_cost = [targeting_comp_data[col][column_dict[targeting_comp]] for col in range(len(targeting_comp_data))]

      if targeting_comp != 'none':
        laser_missile_damage *= targeting_comp_damage

      weight = rocket_weight + minigun_weight + laser_missile_weight + grenade_weight + targeting_comp_weight
      cost = rocket_cost + minigun_cost + laser_missile_cost + grenade_cost + targeting_comp_cost
      baseline_damage = 120 + 120*1.2 # this is the maximum damage possible with two weapons
      damage = (rocket_damage + minigun_damage + laser_missile_damage + grenade_damage) / baseline_damage

      return weight, damage, cost

    # Call the functions and sum the results when the start button is pushed. 
    # Delay the results and display the status bar.
    if start:
      chassis_weight, speed, surv, chassis_cost = get_chassis_data(chassis, frame_size, engine_size, frame, armor)
      acc_weight, damage, acc_cost = accessory_data(rocket, minigun, laser_guided_missile, grenade, targeting_computer)

      weight = chassis_weight + acc_weight
      cost = chassis_cost + acc_cost

      # Show a progress bar and the current test number
      # Delay the results based on the number of tests selected
      latest_iteration = st.empty()
      my_bar = st.progress(0)
      test_time = 600
      total_time = test_time * n_runs # total time in seconds
      for i in range(total_time + 1):
        percent_cpl = int(i / total_time * 100)
        latest_iteration.text('Test {}/{}'.format(i // 600, n_runs))
        my_bar.progress(percent_cpl)
        time.sleep(1)
      st.markdown('Testing results: ')
      st.markdown(f'Weight: {weight:.2f} kgs  \nSpeed: {speed:.2f} km/hr  \nSurvivability index: {surv:.3f}\
          \nDamage index: {damage:.2f}  \nCost: {cost:.2f} ($M)')
  else:
    st.write('Incorrect password')
        
else:
  st.write('No module selected')
