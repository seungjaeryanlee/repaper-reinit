from .resnet import init_ResNet20


def init_model(model_name):
    model = None

    if model_name == "ResNet20":
        model = init_ResNet20()

    return model
