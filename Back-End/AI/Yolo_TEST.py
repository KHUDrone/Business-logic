import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')

im = "ZIDAM8.webp"

results = model(im)

results.print()
results.show()