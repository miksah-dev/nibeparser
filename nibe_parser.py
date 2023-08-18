import csv
from logging.config import valid_ident
import matplotlib.pyplot as plt

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

value = plt.get_backend()
print(value)

# filename = "22031501.LOG"
filename = "21122001.LOG"

# list all log files in the directory
log_files = os.listdir(log_dir)

# create a figure for the plot
fig, ax = plt.subplots()

# iterate over the log files
for log_file in log_files:

    # open the log file
    with open(log_file, 'r') as f:
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
 


plt.subplot(1, 1, 1)

plt.ylim(-30, 75)

plt.axhline(y=-20, color='g', linestyle=':')
plt.axhline(y=0, color='g', linestyle=':')
plt.axhline(y=20, color='g', linestyle=':')
plt.axhline(y=40, color='g', linestyle=':')
plt.axhline(y=60, color='g', linestyle=':')

plt.rcParams["figure.autolayout"] = True
line1, = plt.plot(plot_temp_out, label = "Outside temp")
line2, = plt.plot(plot_temp_in, ls = ':', label = "Temp in")
line3, = plt.plot(plot_temp_room, ls = ':', label = "Temp room")
line4, = plt.plot(plot_temp_waste, label="Temp waste")
line5, = plt.plot(plot_water_in, ls = ':', label = "Cycle Water in")
line6, = plt.plot(plot_water_out, label="Cycle Water out")
line7, = plt.plot(plot_water_up, ls = ':', label = "Water up ")
line8, = plt.plot(plot_water_down, label = "Water down")
line9, = plt.plot(plot_power, label = "Power")
line10, = plt.plot(plot_prio, label = "Mode")

plt.legend(bbox_to_anchor=(1,0.5), loc="center left", borderaxespad=0)
# leg = plt.legend(loc='upper right')

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
    
# giving a title to my graph
plt.title(filename)

# WX backend full screen
manager = plt.get_current_fig_manager()
manager.frame.Maximize(True)

# function to show the plot
plt.show()
plt.savefig(filename + ".png")