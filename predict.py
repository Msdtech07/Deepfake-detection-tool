import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import sys

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Load model
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load("model.pth", map_location=device))
model = model.to(device)
model.eval()

# Class names
classes = ["Fake", "Real"]

# Load image
image_path = sys.argv[1]
image = Image.open(image_path).convert("RGB")
image = transform(image).unsqueeze(0).to(device)

# Prediction
with torch.no_grad():
    output = model(image)
    _, predicted = torch.max(output, 1)

print("Prediction:", classes[predicted.item()])