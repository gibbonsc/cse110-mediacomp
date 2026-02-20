# 12 Activity: Media Computation lab

## Files

### Craft a New Sound File With a Python Synthesizer

An audio file does not contain text or "commma-separated values."
Instead, it's a "binary file" that contains raw digital audio "bytes."

The following program synthesizes tones: one for the left speaker,
another for the right speaker. Musically, the pitches form a "minor
third" interval. The synthesized waveform shapes are
[*square waves*](https://en.wikipedia.org/wiki/Square_wave_%40waveform%41)
which are easy to code as lists of audio samples. Each cycle of a square
wave simply alternates air pressure between "instantly high" (suddenly
compressed) and "instantly low" (suddenly rarefied). A "slope" is used
to very the amplitude of each tone. The left speaker starts loud but
grows quieter, and at the same time the right speaker starts quiet but
grows louder.

```python
import wave

# Create this CD-quality audio data WAV file (16-bit stereo PCM format):
sound_file = "duet.wav"

duration = 176_400  # Create this many stereo frames at 44,100 per second
frequency_a = 440  # Concert A (a.k.a. A4)
frequency_fs = 370  # F-sharp below concert A (a.k.a. F#4)

period_a = 44_100 // frequency_a
half_period_a = period_a // 2
period_fs = 44_100 // frequency_fs
half_period_fs = period_fs // 2

# slope, used to make tones grow louder or quieter as the sound is played.
slope = 32_767 / duration

# build the list of stereo samples
interleaved_samples = []
for i in range(duration):
    # Caution! this wave form is *normalized*.
    #   That means it's the loudest possible sound fit for its waveform!
    #   For hearing health hygiene, turn down your volume before testing!

    # The left channel square wave starts loud, then slopes down quieter.
    if i % period_a < half_period_a:
        left_sample = 32_767 - int(i * slope)
    else:
        left_sample = -32_768 + int(i * slope)

    # Right channel square save starts silent, then slopes up louder.
    if i % period_fs < half_period_fs:
        right_sample = int(i * slope)
    else:
        right_sample = - int(i * slope)

    interleaved_samples.append(left_sample)  # left channel
    interleaved_samples.append(right_sample)  # right channel

# compact interleaved samples into bytes (required for WAV file format)
sample_bytes = bytearray()
for s in interleaved_samples:
    sample_bytes.extend(s.to_bytes(2, byteorder='little', signed=True))
# Write the compacted sound data samples to the file
with wave.open(sound_file, "wb") as audio_file:
    audio_file.setnchannels(2)
    audio_file.setsampwidth(2)
    audio_file.setframerate(44_100)
    audio_file.setnframes(duration)
    audio_file.writeframes(sample_bytes)

```

<audio controls src="duet.wav" type="audio/wav" title="duet.wav"></audio>

(Download audio file: [duet.wav](duet.wav))
