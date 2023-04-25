from torchvision import transforms


def init_transform():
    transform = transforms.Compose(
        [
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, padding=4),
        ]
    )

    return transform
