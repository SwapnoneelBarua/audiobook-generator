from TTS.utils.manage import ModelManager

manager = ModelManager()
model_list = manager.list_models()

for model in model_list:
    print(model)