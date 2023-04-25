from torchvision.datasets import CIFAR10


def init_dataset(transform, train):
    dataset = CIFAR10(
        root="./data/", train=train, transform=transform, download=True
    )

    return dataset
