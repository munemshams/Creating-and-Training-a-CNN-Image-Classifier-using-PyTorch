import torch
import pandas as pd
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from model import FashionCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.ToTensor()

test_data = datasets.FashionMNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

test_loader = DataLoader(test_data, batch_size=1)

model = FashionCNN()
model.load_state_dict(torch.load("fashion_cnn.pth"))
model.to(device)

model.eval()

predictions = []
indices = []

with torch.no_grad():

    for idx, (image, label) in enumerate(test_loader):

        image = image.to(device)

        output = model(image)

        pred = torch.argmax(output, dim=1)

        predictions.append(pred.item())
        indices.append(idx)

df = pd.DataFrame({
    "image_index": indices,
    "predicted_label": predictions
})

df.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")
