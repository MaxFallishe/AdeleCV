from models.base.BaseModel import BaseModel


class BaseSemanticModel(BaseModel):
    def __init__(
            self,
            weights,
            model,
            optimizer,
            lr,
            loss_fn,
            scheduler=None
    ):
        self.weights = weights.DEFAULT
        self.model = model(
            weights=self.weights
        )
        self.transforms = self.weights.transforms()
        self.optimizer = optimizer(self.model.parameters(), lr=lr)
        self.loss_fn = loss_fn
