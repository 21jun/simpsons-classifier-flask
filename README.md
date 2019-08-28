## Setup

Windows 10 / Python 3.6 & 3.7

create venv
```sh
python -m venv flaskenv
flaskenv\Script\activate
```
pytorch-cpu (https://pytorch.org/get-started/locally/)
```sh
pip install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
flask and [fastai](https://docs.fast.ai/install.html)
```sh
pip install -r requirements.txt
```

## Run

```sh
python server.py
```
## Inference

```
http://127.0.0.1:8000/predict?url="The Simpons family image url you want to inference"
```

ex)

```
http://127.0.0.1:8000/predict?url=https://images.clipartlogo.com/files/images/48/481391/maggie-simpson-1_f.jpg
```
```
http://127.0.0.1:8000/predict?url=https://visla.kr/wp/wp-content/uploads/2015/03/The-Simpsons-Illustrated-in-Streetwear-05.jpg
```
## Response
```
{"predict": "lisa_simpson", "proba": 0.9948817491531372, "date": "2019-08-28 04:23:54.205912", "execute time": 0.5455162525177002}
```
```
{"predict": "bart_simpson", "proba": 0.9999544620513916, "date": "2019-08-28 04:23:36.695044", "execute time": 0.5500726699829102}
```


## Train model via Google Colab

https://colab.research.google.com/drive/1b13UgcqrVyXCYyIvGqSWccdJ48_Zq-Rb


## Train image source 

https://www.kaggle.com/alexattia/the-simpsons-characters-dataset

(used only simpsons family characters)
