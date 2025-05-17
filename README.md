# 3HS88PWN4
A core sound engine source code of 3HS88PWN4, a fantasy sound chip that written in C++. Also called S3HS for short, 3SGUC2 for internal Sound Generation Unit.

# 3HS88PWN4 Specifications:
- 8-Channel 8-Operator Harmonic Synthesizer
- 4-Channel PCM/Wavetable/Noise Synthesizer (With IIR Filter)
- 16-bit 48KHz Stereo Linear PCM DAC
- 3-band EQ (Low, Mid, High)
- Envelope Generator (ADSR)
- FM, RM, iPD, and combination synthesis modes
- 8-bit PCM Sample Memory (4096 KBytes)
- Modulation with dynamic wavetable from PCM channel

# 3HS88PWN4 I/O Map Allocations:
- 0x000000 - 0x3FFFFF: PCM Sample Memory (4096 KBytes)
- 0x400000 - 0x4003FF: Register Memory (512 Bytes)
- 0x400400 - 0x403FFF: Unused
