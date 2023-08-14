# Image Upscaling with OpenVINO


### Overview / Usage
The project addresses the challenge of enhancing image quality through an interactive web application. Often, images captured or available online might be of low resolution. This impacts the visual experience and usability, especially in scenarios like image analysis, printing, and presentations. The project aims to solve this problem by providing a user-friendly interface that takes input images and uses a pre-trained OpenVINO model to upscale them, generating high-resolution versions.

The project merges the capabilities of Gradio, OpenVINO, and OpenCV to create an interactive web application. Users can upload images to the web interface, and the application leverages the power of OpenVINO for image upscaling. The uploaded images are processed using an EDSR (Enhanced Deep Super-Resolution) model, which is designed specifically for enhancing image quality through super-resolution techniques. The user can see the upscaled results on the interface (~within 15 seconds), providing a visual transformation of their images.

### Methodology / Approach
Methodology: The project involves developing an interactive web application aimed at elevating image quality. This is accomplished by employing the EDSR (Enhanced Deep Super-Resolution) model, which specializes in image super-resolution. The process unfolds as follows:

### User Interaction: Users interact with the web application's interface, uploading images for enhancement.
### Preprocessing: Uploaded images undergo preparatory steps, encompassing resizing and normalization, to ensure optimal compatibility with the subsequent model inference.
### Model Inference: The pre-trained EDSR model, optimized via the OpenVINO toolkit, undertakes inference on the preprocessed images. By leveraging deep learning, the model generates high-resolution predictions.
### Post-processing: Model outputs undergo final adjustments, including color correction, pixel value normalization, and other refinements, ensuring optimal visual coherence.
### Output Display: The enhanced high-resolution images are rendered in real-time on the web interface, allowing users to promptly observe the impact of the image enhancement.

##Technological Solution:

### Gradio: 
A user-friendly Gradio interface is instrumental in enabling effortless user interaction, streamlining the process of uploading images and receiving immediate feedback.
### OpenVINO: 
The OpenVINO toolkit serves as a pivotal optimization layer, enhancing the speed and efficiency of deep learning inference, thus facilitating real-time execution of the EDSR model.
### EDSR Model: 
The crux of the project resides in the EDSR model, which is trained on high-resolution and low-resolution image pairs. This model proficiency allows it to predict high-quality versions of     input images.
###  Image Processing Libraries: 
OpenCV and PIL come into play for image manipulation tasks. OpenCV facilitates preprocessing and post-processing operations, while PIL assists in image format adjustments.

### Technologies Used
Gradio
OpenVino
OpenCV
EDSR Model
