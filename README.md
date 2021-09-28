## 2021년 홍익대학교 빅데이터 양성과정 프로젝트 1 수행결과물

프로젝트 주제는 '추천시스템을 도입한 전통시장 플랫폼'입니다. 프로젝트 선정의 목적부터 결과까지 pdf 파일로 정리하였으니 관심있으신 분은 읽어보시면 좋을 것 같습니다.
프로젝트를 진행하면서 참고한 자료입니다.
#### 참고자료 및 데이터
* https://www.kaggle.com/laowingkin/fifa-18-predict-player-s-positions 

데이터는 Google Form을 통해 500명의 설문을 직접 받았습니다. 개인정보가 포함되어있기 때문에 업로드는 못했습니다.

#### 추천시스템

먼저 추천시스템에 대해 간략히 설명하겠습니다. 

추천 시스템을 크게 2가지로 분류합니다.
#### CB(content-based)

![cb](https://user-images.githubusercontent.com/83809636/135036337-facd1224-eb22-42a8-a011-24eced1dbee9.png)


### Step 1

각 사용자에 대한 성별,나이,직업,가구원 수와 거기에 mbti를 사용자 속성으로 추가해 이를 기반으로 CF(Collaborative-filtering) 중 user-based 
```python
import numpy as np
import pandas as pd
import plotly.graph_objects as go
    for i in range(5):
        print(i)
       
