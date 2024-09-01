import os

#os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["SUNO_USE_SMALL_MODELS"] = "1"

#from IPython.display import Audio
#import numpy as np

from bark import generate_audio, preload_models, SAMPLE_RATE

import time

preload_models()

t0 = time.time()
#text = "In the light of the moon, a little egg lay on a leaf"
#text="Ok, agora queremos testar uma cenário em português para avaliar o desempenho do modelo."

text = '''
♪ Do music: Serguei Lavrov denunciou que os países da Aliança “estão a encher a Ucrânia com armas mais modernas todos os dias e estão agora a debater como utilizá-las”.
'''

audio_array = generate_audio(text, history_prompt="v2/pt_speaker_0")

from scipy.io.wavfile import write as write_wav

write_wav("bark_generation5.wav", SAMPLE_RATE, audio_array)

generation_duration_s = time.time() - t0
audio_duration_s = audio_array.shape[0] / SAMPLE_RATE

print(f"took {generation_duration_s:.0f}s to generate {audio_duration_s:.0f}s of audio")

os.cpu_count()
