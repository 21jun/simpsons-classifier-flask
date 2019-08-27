from settings import get_model_path
from fastai.vision import * 

print("loading model...")
defaults.device = torch.device('cpu')
learn = load_learner(get_model_path(), 'export.pkl')
print("done!")