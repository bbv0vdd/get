import numpy as np
import matplotlib.pyplot as plt

data_array = np.loadtxt("data.txt", dtype = float)
#print(set(data_array))
settings = np.loadtxt("settings.txt", dtype = float)
fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.minorticks_on()
time_step = settings[0]/data_array.size
time = np.arange(data_array.size)
time=time*time_step
ax.plot(time, data_array, color = "green", linewidth = 2.0, marker = "o", markevery = 7, label = "V(t)")
plt.ylabel("Voltage, V")
plt.xlabel("Time, sec")
plt.legend()
plt.title("Voltage on time")
plt.ylim(data_array.min(), data_array.max())
plt.xlim(time.min(), time.max())
ax.grid(color = 'black', which = 'major', linestyle = "-", linewidth = 2.0)
ax.grid(color = 'black', which = 'minor', linestyle = "--", linewidth = 1.0)
plt.text(0.8*time.max(), 0.8*data_array.max(), f"Total time: {time.max():.3f}\n"
                                               f"Charging time: {data_array.argmax()*time_step:.3f}\n"
                                               f"Discharging: {time.max()-data_array.argmax()*time_step:.3f}",
         bbox={"facecolor": "white"})
fig.savefig("grafic.png")
fig.savefig("grafic.svg")
#plt.show()