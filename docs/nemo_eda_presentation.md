---
marp: true
theme: default
paginate: true
backgroundColor: #F5F500
style: |
  section {
    background-color: #F5F500;
    color: #000;
    font-family: 'Arial Black', sans-serif;
    border: 10px solid #000;
    padding: 50px;
    font-size: 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    color: #000;
    font-size: 55px;
    text-shadow: 6px 6px 0px #FF2D55;
    border: 5px solid #000;
    background: #fff;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 10px 10px 0px #000;
  }
  h2 {
    background: #000;
    color: #F5F500;
    display: inline-block;
    padding: 5px 25px;
    margin-bottom: 25px;
    font-size: 32px;
  }
  li {
    list-style: none;
    margin-bottom: 12px;
    font-weight: 900;
  }
  li::before {
    content: "➜ ";
    color: #FF2D55;
  }
  blockquote {
    background: #CCFF00;
    border: 5px solid #000;
    box-shadow: 12px 12px 0px #000;
    padding: 25px;
    font-size: 26px;
    margin: 20px 0;
  }
  img {
    border: 5px solid #000;
    box-shadow: 8px 8px 0px #000;
    background: #fff;
  }
  table {
    border: 5px solid #000;
    background: #fff;
    width: 100%;
    border-collapse: collapse;
  }
  th {
    background: #000;
    color: #fff;
    padding: 10px;
  }
  td {
    border: 3px solid #000;
    padding: 10px;
    font-weight: bold;
    text-align: center;
  }
  footer { font-weight: 900; color: #000; font-size: 18px; }
  header { font-weight: 900; color: #000; text-transform: uppercase; font-size: 18px; }

header: '📊 NEMO DATA INSIGHT 2026'
footer: 'CONFIDENTIAL | © NEMO DATA STRATEGY'
---

# 📊 NEMO 매물 분석
## 비즈니스 전략 보고서

**2026-04-28**
수석 데이터 분석가 리포트

---

## 01. 시장 종합 인사이트

- **초양극화 현상** : 권리금 평균 4.2억 vs 중앙값 0원
- **실용성 중심** : '다용도점포', '유연한 공간' 선호
- **데이터 기반** : 입지와 면적에 따른 정교한 가격 체계

---

## 02. 자산 양극화 정밀 분석

- 보증금-월세 상관계수 **0.82** (매우 높음)
- 권리금(`premium`)의 극단적 차이
  - 중앙값 **0원** ➜ 무권리 매물 다수 존재
- **핵심 구역** : 테헤란로 & 강남대로 집중 분포

---

## 03. 업종별 매물 분포

![bg right:45% 95%](../data/plots/businessMiddleCodeName_freq.png)

- **기타창업모음** 및 **다용도점포**
- 전체 매물의 **50% 이상** 차지
- 특정 업종에 얽매이지 않는 
- **'범용적 상업 공간'** 수요 급증

---

## 04. 핵심 통계 지표

| 분석 지표 | 보증금 (평균) | 권리금 (평균) | 월세 (평균) |
|:---:|:---:|:---:|:---:|
| **통계치** | 6.13억 | 4.26억 | 5,500만 |
| **중앙값** | 4.00억 | **0원** | 3,800만 |

> **인사이트** : 권리금 거품이 빠진 '실속형 매물'이 시장의 주류

---

## 05. 가격 및 면적 상관관계

![bg left:45% 95%](../data/plots/price_type_dist.png)

- **임대 매물(98.9%)**이 시장 지배
- 면적 증가에 따른 **보증금 선형 상승**
- 특정 면적대(100~200㎡)에서 
- 전략적 권리금 형성 확인

---

## 06. 키워드 중요도 (TF-IDF)

![bg right:45% 95%](../data/plots/title_tfidf.png)

- **임차인 핵심 필터링** :
  - **'인테리어'** (시설 승계)
  - **'역세권'** (접근성)
  - **'1층'** (노출도)
- 제목에 명시된 키워드가 거래 성사 결정

---

## 07. 성공 비즈니스 전략

1. **무권리 매물 선점** : 초기 재무 리스크 최소화
2. **시설 권리 승계** : 인테리어 비용 절감 극대화
3. **유연한 공간 활용** : 업종 전환이 용이한 구조 선택

---

## 08. 최종 분석 결론

### "실용 가치가 지배하는 정교한 데이터 시장"

- 거품 없는 데이터 기반의 가격 형성 확인
- **유연성(Flexibility)** 확보가 창업 성공의 핵심

---

# Q&A
**THANK YOU**
**NEMO STRATEGY TEAM**
