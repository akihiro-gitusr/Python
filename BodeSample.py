import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- 回路パラメータ ---
R = 1e3        # 抵抗 [Ω]
C = 1e-6       # コンデンサ [F]
tau = R * C    # 時定数 τ = RC [s]
fc = 1 / (2 * np.pi * tau)   # カットオフ周波数 [Hz]

print(f"時定数 τ = {tau:.3e} s")
print(f"カットオフ周波数 fc = {fc:.2f} Hz")

# --- 伝達関数の定義 ---
# LPF: H(s) = 1 / (RCs + 1)
lpf = signal.TransferFunction([1], [tau, 1])

# HPF: H(s) = RCs / (RCs + 1)
hpf = signal.TransferFunction([tau, 0], [tau, 1])

# --- 周波数応答の計算 ---
w = np.logspace(0, 6, 1000)  # 角周波数 [rad/s]

w_lpf, mag_lpf, phase_lpf = signal.bode(lpf, w)
w_hpf, mag_hpf, phase_hpf = signal.bode(hpf, w)

f = w / (2 * np.pi)  # rad/s -> Hz に変換

# --- プロット ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# ゲイン線図
ax1.semilogx(f, mag_lpf, color='b', label='LPF')
ax1.semilogx(f, mag_hpf, color='r', label='HPF')
ax1.axvline(fc, color='k', linestyle='--', linewidth=0.8, label=f'fc = {fc:.1f} Hz')
ax1.axhline(-3, color='gray', linestyle=':', linewidth=0.8)
ax1.set_ylabel('Gain [dB]')
ax1.set_title('Bode Plot: LPF vs HPF')
ax1.grid(which='both', linestyle=':')
ax1.legend()

# 位相線図
ax2.semilogx(f, phase_lpf, color='b', label='LPF')
ax2.semilogx(f, phase_hpf, color='r', label='HPF')
ax2.axvline(fc, color='k', linestyle='--', linewidth=0.8)
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Phase [deg]')
ax2.grid(which='both', linestyle=':')
ax2.legend()

plt.tight_layout()
plt.show()
