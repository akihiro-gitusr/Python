import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

wc = 1  # カットオフ角周波数

# LPF: H(s) = 1/(s/wc + 1)
lpf = signal.TransferFunction([1], [1/wc, 1])
# HPF: H(s) = (s/wc)/(s/wc + 1)
hpf = signal.TransferFunction([1/wc, 0], [1/wc, 1])

w = np.logspace(-2, 2, 500)
w_lpf, mag_lpf, phase_lpf = signal.bode(lpf, w)
w_hpf, mag_hpf, phase_hpf = signal.bode(hpf, w)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,6))
ax1.semilogx(w_lpf, mag_lpf, label="LPF")
ax1.semilogx(w_hpf, mag_hpf, label="HPF")
ax1.set_ylabel("Gain [dB]")
ax1.legend(); ax1.grid(True, which="both")

ax2.semilogx(w_lpf, phase_lpf, label="LPF")
ax2.semilogx(w_hpf, phase_hpf, label="HPF")
ax2.set_ylabel("Phase [deg]")
ax2.set_xlabel("Frequency [rad/s]")
ax2.legend(); ax2.grid(True, which="both")

plt.tight_layout()
plt.show()
