# Image Upscaling with OpenVINO

## Overview / Usage

Enhancing image quality has never been easier with the interactive web application. Low-resolution images, whether captured or found online, often lack the visual impact required for image analysis, printing, and presentations. The project aims to address this challenge by offering a user-friendly interface that takes input images and utilizes a pre-trained OpenVINO model to upscale them, resulting in stunning high-resolution versions.

By using the capabilities of Gradio, OpenVINO, and OpenCV, made an intuitive web application. Users can effortlessly upload their images to the web interface, where the application uses model to perform image upscaling. The uploaded images undergo processing using the Enhanced Deep Super-Resolution (EDSR) model, a cutting-edge approach specifically designed to enhance image quality .(takes ~ 15 seconds).

## Methodology / Approach

**Methodology:** The project revolves around the development of an interactive web application focused on improving image quality. This is achieved through the application of the Enhanced Deep Super-Resolution (EDSR) model, a specialist in image super-resolution. The step-by-step process is as follows:

1. **User Interaction:** Users can engage with the web application's interface,uploads image for enhancement.
2. **Preprocessing:** Uploaded images undergo preprocessing, involving resizing and normalization, ensuring compatibility with the model.
3. **Model Inference:** The pre-trained EDSR model, fine-tuned with the OpenVINO toolkit, performs inference on the preprocessed images. Harnessing the power of deep learning, the model generates high-resolution predictions.
4. **Post-processing:** Model outputs undergo final adjustments, encompassing color correction, pixel value normalization, and other refinements, culminating in visually coherent and compelling results.
5. **Output Display:** The enhanced high-resolution images are showcased in real-time on the web interface, enabling users to promptly witness the transformative impact of image enhancement.

## Technological Solution

**Gradio:** The user-friendly interface, powered by Gradio, ensures a seamless user experience. Uploading images and receiving instant feedback has never been easier.

**OpenVINO:** The OpenVINO toolkit serves as a critical optimization layer, significantly boosting the speed and efficiency of deep learning inference. This enables real-time execution of the EDSR model and delivers results promptly.

**EDSR Model:** At the heart of the project lies the EDSR model. Trained on high-resolution and low-resolution image pairs, this model's proficiency enables it to predict remarkable high-quality versions of input images.

**Image Processing Libraries:** OpenCV and PIL play crucial roles in image manipulation. OpenCV handles preprocessing and post-processing tasks, while PIL assists in fine-tuning image formats.

## Technologies Used

- Gradio
- OpenVino
- OpenCV
- EDSR Model
## Demo

Check out the demo video to see the Image Upscaling with OpenVINO in action!

https://github.com/AghoraGuru/1API/assets/88477799/4d29aaca-ba3a-4dfc-8131-a12249fb2267


## Try it out:

Check out the HuggingFace [Space](https://huggingface.co/spaces/aghoraguru/EDSR-OpenVINO) to try it ! 

## ScreenShots:
![Gradio](https://github.com/AghoraGuru/1API/assets/88477799/45eed204-a1e4-41bf-ad9f-35d200b922a8)
![scaled_robo](https://github.com/AghoraGuru/1API/assets/88477799/6ceccba3-be2b-4a66-8969-b1e79ca94e73)
