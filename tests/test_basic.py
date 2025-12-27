import os
import pytest
import torch

from ai_detector_model import load_model

def test_model_file_exists():
    assert os.path.exists("best_combined_resnet_model.pth"), "Model file is missing!"

def test_model_loads():
    # This test will pass if the model loads without error
    try:
        model, device = load_model("best_combined_resnet_model.pth")
    except Exception as e:
        pytest.fail(f"Model failed to load: {e}")

def test_model_is_torch_nn_module():
    model, device = load_model("best_combined_resnet_model.pth")
    assert isinstance(model, torch.nn.Module), "Loaded model is not a torch.nn.Module"