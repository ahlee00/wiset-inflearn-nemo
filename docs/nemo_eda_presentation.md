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
    border: 8px solid #000;
    padding: 40px;
    font-size: 28px;
  }
  h1 {
    color: #000;
    font-size: 60px;
    text-shadow: 6px 6px 0px #FF2D55;
    border-bottom: 6px solid #000;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  h2 {
    background: #000;
    color: #F5F500;
    display: inline-block;
    padding: 5px 20px;
    transform: rotate(-2deg);
    margin-bottom: 30px;
  }
  li {
    list-style: none;
    margin-bottom: 15px;
  }
  li::before {
    content: "■ ";
    color: #FF2D55;
  }
  blockquote {
    background: #CCFF00;
    border: 4px solid #000;
    box-shadow: 10px 10px 0px #000;
    padding: 20px;
    font-weight: bold;
  }
  footer {
    font-weight: bold;
    color: #000;
  }
  header {
    font-weight: bold;
    color: #000;
    text-transform: uppercase;
  }
header: '📊 NEMO REAL ESTATE REPORT'
footer: '© 2026 NEMO DATA STRATEGY'
---

# 📊 NEMO 매물 분석
## 비즈니스 전략 보고서

**2026-04-28**
20년 경력 수석 데이터 분석가

---

## 01. 시장 인사이트

- **초양극화**: 권리금 평균 4.2억 vs 중앙값 0원
- **실용성 중심**: '다용도점포', '유연한 공간' 지향
- **데이터 기반**: 입지/면적에 따른 정교한 가격 형성

---

## 02. 자산 양극화 현상

- 보증금-월세 상관계수 **0.82** (Extremely High)
- 권리금(`premium`)의 극심한 양극화
  - 중앙값 **0원** (시설 권리금 없는 매물 다수)
- **GOLDEN TRIANGLE**: 테헤란로-강남대로 집중

---

## 03. 업종별 분포

![bg right:45% 95%](../data/plots/businessMiddleCodeName_freq.png)

- **기타창업모음** & **다용도점포** > 50%
- 특정 업종에 고착되지 않은 
- **'범용 공간'** 수요 압도적

---

## 04. 핵심 기술 통계

| 지표 | 보증금 | 권리금 | 월세 |
|:---:|:---:|:---:|:---:|
| **평균** | 6.13억 | 4.26억 | 5,500만 |
| **중앙값** | 4.00억 | **0원** | 3,800만 |

> 시장의 실질적 진입 장벽은 보증금과 월세에 집중됨

---

## 05. 가격 및 면적 분석

![bg left:45% 95%](../data/plots/price_type_dist.png)

- **임대 매물(98.9%)** 절대적 비중
- 면적-보증금의 **강한 선형 관계**
- 특정 구간(100~200㎡) 
- 고권리금 타겟팅 발생

---

## 06. 키워드 중요도

![bg right:45% 95%](../data/plots/title_tfidf.png)

- **TOP FILTERING**:
  - '인테리어'
  - '역세권'
  - '1층'
- 실질적 선호도가 제목에 즉각 반영

---

## 07. 비즈니스 전략

1. **무권리 매물 선점**: 중앙값 0원 시장 활용
2. **시설 승계**: 기존 인테리어 활용 극대화
3. **유연한 공간**: 업종 변경 용이성 확보

---

## 08. 최종 결론

### "실용적 가치가 지배하는 안정적 임대차 시장"

- 정교한 데이터 기반 가격 체계
- **FLEXIBILITY**가 성공 창업의 핵심

---

# Q&A
**THANK YOU**
