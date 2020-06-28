# NK Model Simulator


## 참고 논문
#### Temporarily Divide to Conquer: Centralized, Decentralized, and Reintegrated Organizational Approaches to Exploration and Adaptation (Nicolaj Siggelkow * Daniel A. Levinthal)

## 프로젝트 개요 
#### 2017년 연세대학교 경영학과 STRATEGIC MANAGEMENT(Prof. Kim Ji-hyun)의 수업에서 위 논문의 알고리즘을 분석하고 이를 프로그래밍(PYTHON)하여 시뮬레이션 결과를 구현한 것입니다.


## 실행방법
1. Repository를 clone하고 해당 폴더로 이동합니다.
2. pip3 install -r requirements.txt 
(혹은 pip install -r requirements.txt) 명령어를 입력하여 필요 module을 설치합니다.
3.  python3 .\nk_model_simulator.py  
(혹은 python .\nk_model_simulator.py) 
명령어를 입력하여 스크립트를 실행시킵니다.
4. print되는 설명에 따라 아래의 input들을 차례대로 터미널에 입력합니다.
- Number of N
- Type of interaction matrix
- Number of K
- Number of Division
- Number of simulation

## 실행결과
#### matplotlib 사용하여 시뮬레이션 결과를 2D 그래프로 출력합니다.

![결과1](/images/simul_individual1.png)
![결과2](/images/simul_individual6.png)
![결과3](/images/simul_S=2000,Di=3,K=2.png)


_2017년 처음 PYTHON을 배우면서 시뮬레이션 재현만 되면 된다라는 마음으로.. 하찮은 솜씨로 상당히 투박하게 만든 코드입니다. 기회가되면 좀 더 깔끔하게 리팩토링해보겠습니다._


_팀으로 진행하는 프로젝트였으나 첨부한 코드는 모두 혼자서 구현했고, 따라서 개인 Repository에 구현한 코드를 첨부하는데 문제 될 소지가 없다고 판단하였습니다._

