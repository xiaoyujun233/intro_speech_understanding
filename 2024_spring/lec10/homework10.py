import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    num_frames = int((len(waveform) - frame_length) / step) + 1
    frames = np.zeros((frame_length, num_frames))
    
    for t in range(num_frames):
        frames[:, t] = waveform[t * step : t * step + frame_length]
    
    return frames

def frames_to_stft(frames):
    frame_length, num_frames = frames.shape
    stft = np.zeros((frame_length, num_frames), dtype=complex)
    
    for t in range(num_frames):
        stft[:, t] = np.fft.fft(frames[:, t])
    
    return stft

def stft_to_spectrogram(stft):
    abs_stft = np.abs(stft)
    spectrogram = 20 * np.log10(np.maximum(0.001, abs_stft/np.amax(abs_stft)))

    return spectrogram


