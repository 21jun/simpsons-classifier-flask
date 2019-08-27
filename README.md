## run

python server.py

## inference

```http://127.0.0.1:8000/predict?url="The Simpons family image url you want to inference"```

ex)


```
http://127.0.0.1:8000/predict?url=https://images.clipartlogo.com/files/images/48/481391/maggie-simpson-1_f.jpg
```
```
http://127.0.0.1:8000/predict?url=https://visla.kr/wp/wp-content/uploads/2015/03/The-Simpsons-Illustrated-in-Streetwear-05.jpg
```
## response
```
{"predict": "lisa_simpson", "date": "2019-08-28 03:49:36.078090", "execute time": 0.5399980545043945}
```
```
{"predict": "bart_simpson", "date": "2019-08-28 03:51:53.867311", "execute time": 0.5450229644775391}
```


## Train model via Google Colab

https://colab.research.google.com/drive/1b13UgcqrVyXCYyIvGqSWccdJ48_Zq-Rb


## train image source 

https://www.kaggle.com/alexattia/the-simpsons-characters-dataset

(used only simpsons family characters)
