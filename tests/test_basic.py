import os

def test_model_file_exists():
    assert os.path.exists("best_combined_resnet_model.pth"), "Model file is missing!"