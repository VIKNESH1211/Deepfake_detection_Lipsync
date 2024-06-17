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
## OUR APPROACH

![image](https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/8223a242-65d1-4706-a94a-c6ec10b5215f)

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

## Raw Dataset
Person speaking OTP (any 6 random digits). We have collected about 105 such videos of different people accounting a total of 105 different combination of numbers.Length of the video varies between 6-10 seconds.

[https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/8bc191e6-1173-4b7f-b954-f5f37380ffe5](https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/18337584-6ec9-423f-8c79-b88783c08db4)

https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/1e2a620a-2428-4ade-85ef-5776d2fb6875
## Example

<figure>
  <img src="https://huggingface.co/vumichien/AV-HuBERT/resolve/main/lipreading.gif" alt="Audio-Visual Speech Recognition">
  <figcaption> Speech Recognition from visual lip movement
  </figcaption>
</figure>

## Datasets
The authors trained the model on LRS3 with 433 hours of transcribed English videos and English portion of VoxCeleb2, which amounts to 1,326 hours

## Technique 1: FaceSwap using Roop
**Description:**
FaceSwap using Roop employs a face-swapping algorithm to seamlessly replace the face of a person in a video with another person's face.

**Features:**

**High-quality face swapping
Realistic blending
Consistent facial expressions**

Video Example:

https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/fac289da-9f40-447c-893a-239145a6230e

https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/05f069b8-ffee-49eb-86b1-abff60eeb358




**Technique 2: FaceDancer**
**Description:**
FaceDancer is a powerful tool for generating deepfakes with smooth transitions and realistic facial movements.

**Features:**

**Smooth transitions
Accurate facial expressions
Robust to different lighting conditions**

**Video Example:**

https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/aa5742ad-64e8-4cce-90f2-4412bb83d48c


https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/cfe4407e-7b87-4ef7-ac52-bc39cee3792b


**Technique 3: Wave2Lip+GAN**
**Description:**
Wave2Lip+GAN combines Wave2Lip’s lipsync capabilities with Generative Adversarial Networks to enhance the realism of the generated video.

**Features:**

**High-quality lipsync
Enhanced realism with GANs
Natural-looking speech movements**

**Video Example:**


https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/4e436a90-a41c-46ad-9caa-5e54a8dc57b2


https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/53f8a299-fb0a-4399-9f53-ca07508bf3a4



**Technique 4: Wave2Lip+ERSGAN**
**Description:**
Wave2Lip+ERSGAN utilizes the Enhanced Super-Resolution GAN to produce high-resolution deepfakes with precise lipsync and fine details.

**Features:**

**Superior visual quality
High-resolution outputs
Detailed and realistic lipsync**

**Video Example:**

https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/e6fa6bde-5439-43bf-93eb-cf39c27fe015


https://github.com/ansh-tandon/Deepfake_detection_Lipsync/assets/90792560/4418cfc2-c386-43f5-863e-bf00337aae3a


