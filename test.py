import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# カットオフ角周波数
wc = 1

# 伝達関数の定義
# LPF: H(s) = 1/(s/wc + 1)
lpf = signal.TransferFunction([1], [1/wc, 1])
# HPF: H(s) = (s/wc)/(s/wc + 1)
hpf = signal.TransferFunction([1/wc, 0], [1/wc, 1])

# 周波数範囲
w = np.logspace(-2, 2, 500)

# ナイキスト線図の計算
w_lpf, H_lpf = signal.freqresp(lpf, w)
w_hpf, H_hpf = signal.freqresp(hpf, w)

# プロット
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# LPF
ax1.plot(H_lpf.real, H_lpf.imag, 'b-', linewidth=2, label='LPF')
ax1.plot(H_lpf.real[0], H_lpf.imag[0], 'ro', markersize=8)  # ω=0の点
ax1.plot(H_lpf.real[-1], H_lpf.imag[-1], 'go', markersize=8)  # ω=∞の点
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlabel('Real')
ax1.set_ylabel('Imaginary')
ax1.set_title('LPF Nyquist Plot')
ax1.grid(True)
ax1.legend()
ax1.axis('equal')

# HPF
ax2.plot(H_hpf.real, H_hpf.imag, 'r-', linewidth=2, label='HPF')
ax2.plot(H_hpf.real[0], H_hpf.imag[0], 'ro', markersize=8)  # ω=0の点
ax2.plot(H_hpf.real[-1], H_hpf.imag[-1], 'go', markersize=8)  # ω=∞の点
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.set_title('HPF Nyquist Plot')
ax2.grid(True)
ax2.legend()
ax2.axis('equal')

plt.tight_layout()
plt.show()
