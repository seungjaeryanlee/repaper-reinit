from models import init_model


def main():
    model = init_model("ResNet20")
    print(model)


if __name__ == "__main__":
    main()
