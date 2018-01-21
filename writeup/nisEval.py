import matplotlib.pylab as plt

radar_file = open("nis_radar_log.txt")
laser_file = open("nis_laser_log.txt")

nis_radar = []
nis_laser = []

for line in radar_file.readlines():
  nis_radar.append(float(line))

for line in laser_file.readlines():
  nis_laser.append(float(line))

# exclude RADAR's first measurements
nis_radar = nis_radar[2:]

radar_thresh = 7.815
laser_thresh = 5.991

radar_outliers = sum(1 for i in nis_radar if i > radar_thresh)
radar_ratio = radar_outliers/len(nis_radar)
print("Radar Ratio",radar_ratio)

laser_outliers = sum(1 for i in nis_laser if i > laser_thresh)
laser_ratio = laser_outliers/len(nis_laser)
print("Radar Ratio",laser_ratio)
radar_string = "Over NIS (" + str(radar_thresh) + ") criterion: " + str(int(radar_ratio*100)) + "%"
laser_string = "Over NIS (" + str(laser_thresh) + ") criterion: " + str(int(laser_ratio*100)) + "%"

plt.figure("NIS RADAR")
plt.plot(nis_radar)
plt.axhline(y=radar_thresh)
plt.text(80, 10, radar_string, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
plt.xlabel('MEASUREMENT')
plt.ylabel('NIS RADAR')

plt.figure("NIS LASER")
plt.plot(nis_laser)
plt.axhline(y=laser_thresh)
plt.text(80, 10, laser_string, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
plt.xlabel('MEASUREMENT')
plt.ylabel('NIS RADAR')
plt.xlabel('MEASUREMENT')
plt.ylabel('NIS LASER')
plt.show()