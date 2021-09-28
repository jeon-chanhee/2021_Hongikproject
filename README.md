## 2021년 홍익대학교 빅데이터 양성과정 프로젝트 1 수행결과물

프로젝트 주제는 '추천시스템을 도입한 전통시장 플랫폼'입니다. 프로젝트 선정의 목적부터 결과까지 pdf 파일로 정리하였으니 관심있으신 분은 읽어보시면 좋을 것 같습니다.
프로젝트를 진행하면서 참고한 자료입니다.
#### 참고자료 및 데이터
* https://www.kaggle.com/laowingkin/fifa-18-predict-player-s-positions 

데이터는 Google Form을 통해 500명의 설문을 직접 받았습니다. 개인정보가 포함되어있기 때문에 업로드는 못했습니다.

### 추천시스템

먼저 추천시스템에 대해 간략히 설명하겠습니다. 
추천 시스템은 사용자(user)가 선호하는 상품(item)으 예측하는 시스템이라고 할 수 있는데 크게 2가지로 분류합니다.
#### CB(Content-based)

* 출처 : https://towardsdatascience.com/essentials-of-recommendation-engines-content-based-and-collaborative-filtering-31521c964922

![cb](https://user-images.githubusercontent.com/83809636/135036337-facd1224-eb22-42a8-a011-24eced1dbee9.png)

아이템을 기반으로 추천해주는 시스템이며 사용자가 특정 아이템을 선호하는 경우 그 아이템과 비슷한 콘텐츠를
가진 다른 아이템을 추천합니다.

#### CF(Collaborative-filtering)

![cf](https://user-images.githubusercontent.com/83809636/135038509-3f3b4b56-c095-451e-ba40-2672b3476e13.png)

협업 필터링(collaborative filtering)에는 최근접 이웃 기반(nearest neighbor based collaborative filtering)과 잠재 요인(latent factor based collaborative filtering)이 있습니다.
저는 최근접 이웃 기반 알고리즘을

### Step 1

각 사용자에 대한 성별,나이,직업,가구원 수와 거기에 mbti를 사용자 속성으로 추가해 이를 기반으로 CF(Collaborative-filtering) 중 user-based 
```python
import numpy as np
import pandas as pd
import plotly.graph_objects as go
    for i in range(5):
        print(i)
       
