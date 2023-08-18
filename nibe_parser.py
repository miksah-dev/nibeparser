import csv
import os
from logging.config import valid_ident
import matplotlib.pyplot as plt



value = plt.get_backend()
print(value)

# filename = "22031501.LOG"
#filename = "21122001.LOG"

# directory where the log files are stored
log_dir = 'Logs/'

# set the output directory as "monthly"
output_dir = "monthly/"

# list all log files in the directory
log_files = os.listdir(log_dir)

print (log_files)

# create a figure for the plot
fig, ax = plt.subplots()

# iterate over the log files
for log_file in log_files:

    plot_temp_out = []
    plot_water_in = []
    plot_water_out = []
    plot_water_down = []
    plot_water_up = []
    plot_temp_waste = []
    plot_temp_in = []
    plot_temp_room = []
    plot_power = []
    plot_prio = []

    # open the log file
    with open(os.path.join(log_dir, log_file), 'r') as f:
        # create a csv reader object
        reader = csv.reader(f, delimiter='\t')

        # skip the first two lines (value dividers and headers)
        next(reader)
        next(reader)

        # iterate over the data lines and extract the temperature and other values
        for row in reader:
            date, time, version, r_version, bt1, bt2, bt3, bt6, bt7, bt16, bt18, bt19, bt20, bt21, bt22, bt50, int_add, alarm_num, calc_supply, bt1_avg, relays, prio = row

            # convert the values to floating-point numbers using the value dividers
            version = float(version) / 10
            r_version = float(r_version) / 10
            bt1 = float(bt1) / 10
            bt2 = float(bt2) / 10
            bt3 = float(bt3) / 10
            bt6 = float(bt6) / 10
            bt7 = float(bt7) / 10
            bt16 = float(bt16) / 10
            bt18 = float(bt18) / 10
            bt19 = float(bt19) / 10
            bt20 = float(bt20) / 10
            bt21 = float(bt21) / 10
            bt22 = float(bt22) / 10
            bt50 = float(bt50) / 10
            int_add = float(int_add) / 100
            calc_supply = float(calc_supply) / 10
            bt1_avg = float(bt1_avg) / 10

            plot_temp_out.append(bt1)
            plot_water_in.append(bt2)
            plot_water_out.append(bt3)
            plot_water_down.append(bt6)
            plot_water_up.append(bt7)
            plot_temp_waste.append(bt21)
            plot_temp_in.append(bt22)
            plot_temp_room.append(bt50)
            plot_power.append(int_add)
            plot_prio.append(int (prio))

            # print the extracted values
            # print(date, time, version, r_version, bt1, bt2, bt3, bt6, bt7, bt16, bt18, bt19, bt20, bt21, bt22, bt50, int_add, alarm_num, calc_supply, bt1_avg, relays, prio)
 


    ax.set_ylim(-35, 75)
    
    ax.axhline(y=-20, color='g', linestyle=':')
    ax.axhline(y=0, color='g', linestyle=':')
    ax.axhline(y=20, color='g', linestyle=':')
    ax.axhline(y=40, color='g', linestyle=':')
    ax.axhline(y=60, color='g', linestyle=':')

    plt.rcParams["figure.autolayout"] = True
    ax.set_sketch_params()

    line1, = ax.plot(plot_temp_out, label = "Outside temp")
    line2, = ax.plot(plot_temp_in, ls = ':', label = "Temp in")
    line3, = ax.plot(plot_temp_room, ls = ':', label = "Temp room")
    line4, = ax.plot(plot_temp_waste, label="Temp waste")
    line5, = ax.plot(plot_water_in, ls = ':', label = "Cycle Water in")
    line6, = ax.plot(plot_water_out, label="Cycle Water out")
    line7, = ax.plot(plot_water_up, ls = ':', label = "Water up ")
    line8, = ax.plot(plot_water_down, label = "Water down")
    line9, = ax.plot(plot_power, label = "Power")
    line10, = ax.plot(plot_prio, label = "Mode")

    ax.legend(bbox_to_anchor=(1,0.5), loc="center left", borderaxespad=0)
    # leg = ax.legend(loc='upper right')

    # naming the x axis
    ax.set_xlabel('x - axis')
    # naming the y axis
    ax.set_ylabel('y - axis')
        
    # giving a title to my graph
    ax.set_title (log_file)
    
    # WX backend full screen
    manager = plt.get_current_fig_manager()


    # function to show the plot
    # plt.show()
        
    # save the plot to a file in the monthly subdirectory
    #plt.savefig("monthly/{log_file[:-4]}.png")
    plot_filename = os.path.join(output_dir, f"{log_file[:-4]}.png")
    plt.savefig(plot_filename)
    

    
