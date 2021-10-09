# 이미지분류 경진대회

- 얼굴을 정면으로 찍은 사진이 입력으로 주어집니다. (총 18,000장)
- `마스크 정상 착용 여부(3)` * `나이대(3)` * `성별(2)` = 18 classes
- 총 18개의 클래스로 이미지를 분류하는 경진대회입니다.
- 평가지표는 `f1-score`를 사용합니다.

## 데이터 설명

- 대상: 아시아인 남녀, 20대~70대
- 전체 사람 수 : 4,500
- 한 사람당 사진의 개수: 7
  - 마스크 정상 착용: 5장
  - 마스크 불량 착용: 1장
  - 마스크 미착용: 1장
- 이미지 크기: (384, 512)

<details>
<summary>데이터 상세 Description 보기</summary>
<div markdown="1">


  ### 학습데이터, 테스트 데이터

  - 데이터 분할
    - 학습데이터 60%
    - public 테스트셋 20%
    - private 테스트셋 20%

  ### 입출력

  - 입력: 마스크 착용 사진, 미착용 사진, 혹은 이상하게 착용한 사진(코스크, 턱스크)
  - 출력: 총 18개의 class를 예측해야합니다. 결과값으로 0~17에 해당되는 숫자가 각 이미지 당 하나씩 나와야합니다.
    <details>
    <summary>예시</summary>
    <div markdown="1">

    - the class of `cfe1268.jpg` : 7  
    - the class of `3a2662c.jpg` : 2

    </div>
    </details>

  ### 클래스 분류 기준

  - 마스크 착용여부, 성별, 나이를 기준으로 총 18개의 클래스가 있습니다.
    <details>
    <summary>상세 분류 기준 보기</summary>
    <div markdown="1">

    <img src="https://user-images.githubusercontent.com/35002768/136669475-74d45d46-6236-4b70-85f0-cbc6a42bbed5.png" width="60%">

    </div>
    </details>


</div>
</details>

## 평가방식

- Submission 파일을 채점서버에 올리면, F1-Score를 기준으로 결과를 보여주는 방식입니다.
- 평가기준: F1-score
<!-- $$F_1 = 2 * {{precision * recall} \over {precision + recall}}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

<!-- $$precision = {TP \over {TP + FP}}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

<!-- $$recall = {TP \over {TP + FN}}$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>
