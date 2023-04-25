from torchvision.datasets import CIFAR10


def init_dataset():
    dataset = CIFAR10(
        root="./data/", train=True, transform=train_transform, download=True
    )

    return dataset
