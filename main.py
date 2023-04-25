from models import init_model
from torchvision.datasets import CIFAR10
from torchvision import transforms


def main():
    model = init_model("ResNet20")
    train_transform = transforms.Compose(
        [
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, padding=4),
        ]
    )
    train_dataset = CIFAR10(
        root="./data/", train=True, transform=train_transform, download=True
    )

    print(model)


if __name__ == "__main__":
    main()
