---
license: apache-2.0
language:
- en
pipeline_tag: automatic-speech-recognition
datasets:
- LRS3

tags:
- Audio Visual to Text
- Automatic Speech Recognition
---

## Model Description

These are model weights originally provided by the authors of the paper [Learning Audio-Visual Speech Representation by Masked Multimodal Cluster Prediction](https://arxiv.org/pdf/2201.02184.pdf).

<figure>
  <img src="https://huggingface.co/vumichien/AV-HuBERT/resolve/main/HuBert.png" alt="Audio-visual HuBERT">
  <figcaption>Audio-visual HuBERT
  </figcaption>
</figure>

Video recordings of speech contain correlated audio and visual information, providing a strong signal for speech representation learning from the speaker’s lip
movements and the produced sound. 

Audio-Visual Hidden Unit BERT (AV-HuBERT), a self-supervised representation learning framework for audio-visual speech, which masks multi-stream video input and predicts automatically discovered and iteratively refined multimodal hidden units. AV-HuBERT
learns powerful audio-visual speech representation benefiting both lip-reading and automatic speech recognition.

The official code of this paper in [here](https://github.com/facebookresearch/av_hubert)
## Deepfake Generated Videos
Person speaking OTP (any 6 random digits). We have collected about 105 such videos of different people accounting a total of 105 different combination of numbers.

[https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/8bc191e6-1173-4b7f-b954-f5f37380ffe5](https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/18337584-6ec9-423f-8c79-b88783c08db4)
## Example

<figure>
  <img src="https://huggingface.co/vumichien/AV-HuBERT/resolve/main/lipreading.gif" alt="Audio-Visual Speech Recognition">
  <figcaption> Speech Recognition from visual lip movement
  </figcaption>
</figure>

## Datasets
The authors trained the model on LRS3 with 433 hours of transcribed English videos and English portion of VoxCeleb2, which amounts to 1,326 hours
