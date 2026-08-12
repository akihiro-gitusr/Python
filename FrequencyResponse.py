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

# ---------------- bode plot

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


# ---------------- nyquist diagram

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
