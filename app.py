import gradio as gr
from openvino.inference_engine import IECore
import cv2
import numpy as np
from PIL import Image

# Load the OpenVINO model
model_xml = '/home/kalyan/gitrepo/NeedToStartARepo/oneapi/kalyan.xml'
model_bin = '/home/kalyan/gitrepo/NeedToStartARepo/oneapi/kalyan.bin'

ie = IECore()
net = ie.read_network(model=model_xml, weights=model_bin)
exec_net = ie.load_network(network=net, device_name="CPU")

# Define the function for image processing
def upscale_image(input_image):
    # Convert Gradio PIL Image to numpy array
    input_image = np.array(input_image)

    # Preprocess the input image
    image = cv2.cvtColor(input_image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0
    image = np.transpose(image, (2, 0, 1))
    image = image.reshape(1, 3, 224, 224)

    # Run inference
    outputs = exec_net.infer(inputs={'input': image})

    # Post-process the output
    output_image = outputs['output'][0]
    output_image = np.transpose(output_image, (1, 2, 0))
    output_image = np.clip(output_image, 0, 1) * 255
    output_image = output_image.astype(np.uint8)
    output_image = cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)
    return output_image

# Create the Gradio interface
inputs = gr.inputs.Image(type="pil", label="Input Image")  # Use 'pil' type for uploaded images
outputs = gr.outputs.Image(type="pil", label="Upscaled Image")

title = "Image Upscaling App"
description = "Upload an image and see the upscaled result."
iface = gr.Interface(fn=upscale_image, inputs=inputs, outputs=outputs, title=title, description=description)

# Launch the Gradio interface
iface.launch()
