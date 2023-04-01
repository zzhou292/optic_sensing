from Phidget22.Phidget import *
from Phidget22.Devices.Accelerometer import *
import time
import csv

# The CSV file path
csv_file_path = 'my_file.csv'

def onAccelerationChange(self, acceleration, timestamp):

	
	print("Acceleration: \t"+ str(acceleration[0])+ "  |  "+ str(acceleration[1])+ "  |  "+ str(acceleration[2]))
	print("Timestamp: " + str(timestamp))
	print("----------")

	# Open the CSV file for writing
	with open(csv_file_path, mode='a', newline='') as csv_file:
		# Create a CSV writer object
		csv_writer = csv.writer(csv_file, delimiter=',')

		row_data =[]
		row_data.append(timestamp)
		row_data.append(acceleration[0])
		row_data.append(acceleration[1])
		row_data.append(acceleration[2])

		# Write the float array to the CSV file
		csv_writer.writerow(row_data)

def main():
	accelerometer0 = Accelerometer()

	accelerometer0.setOnAccelerationChangeHandler(onAccelerationChange)

	accelerometer0.openWaitForAttachment(200)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass
	accelerometer0.close()

main()