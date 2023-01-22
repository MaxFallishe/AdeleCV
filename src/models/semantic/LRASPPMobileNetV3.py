import torch
from torchvision import models
from torchvision.models.segmentation import LRASPP_MobileNet_V3_Large_Weights
from torchvision.models.segmentation.lraspp import LRASPPHead

from models.semantic.SemanticModel import SemanticModel


class LRASPPMobileNetV3(SemanticModel):
    def __init__(
            self,
            optimizer,
            loss_fn,
            lr,
            num_classes,
            mode=''
    ):
        super().__init__(
            optimizer=optimizer,
            loss_fn=loss_fn,
            lr=lr,
            weights=LRASPP_MobileNet_V3_Large_Weights,
            model=models.segmentation.lraspp_mobilenet_v3_large
        )

        self.model.classifier = LRASPPHead(
            low_channels=40,
            high_channels=960,
            inter_channels=128,
            num_classes=num_classes
        )

    def train_step(self, x_batch, y_batch):
        self.optimizer.zero_grad()
        pred = self.model(x_batch)['out']
        loss = self.loss_fn(pred, y_batch)
        loss.backward()
        self.optimizer.step()

        return loss.detach()

    def val_step(self, x_batch, y_batch):
        with torch.no_grad():
            pred = self.model(x_batch)['out']
            loss = self.loss_fn(pred, y_batch).detach()

        return loss

    def predict(self, x_batch):
        raise NotImplemented
