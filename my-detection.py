#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils
# import torch
# import torchvision.transforms as transforms
# from PIL import Image

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# def jpeg_2_cuda(jpeg_path):
#     image = Image.open(jpeg_path).convert('RGB')
#     transform = transforms.Compose([transforms.ToTensor()])
#     cuda_tensor = transform(image).unsqueeze(0).to(device)
#     return cuda_tensor

camera = jetson.utils.videoSource("/home/nvidia/jetson-inference/examples/b10.jpeg")
# cuda_image = jpeg_2_cuda('/home/nvidia/jetson-inference/examples/a10.jpeg')

display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming(): # main loop will go here
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)

    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))











