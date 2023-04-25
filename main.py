from datasets import init_dataset
from models import init_model
from transforms import init_transform


def main():
    model = init_model("ResNet20")
    train_transform = init_transform()
    train_dataset = init_dataset()

    print(model)


if __name__ == "__main__":
    main()
