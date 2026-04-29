---
marp: true
theme: gaia
_class: lead
backgroundColor: #0f172a
color: #f8fafc
paginate: true
header: "Nemo 매물 데이터 심층 분석 보고서"
footer: "© 2026 Nemo Data Analytics Team"
style: |
  section {
    font-family: 'Noto Sans KR', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    color: #38bdf8;
    font-size: 60px;
  }
  h2 {
    color: #818cf8;
    font-size: 45px;
    margin-top: 20px;
  }
  h3 {
    color: #38bdf8;
    font-size: 35px;
  }
  p, li {
    font-size: 25px;
    line-height: 1.6;
  }
  footer {
    color: #64748b;
  }
  img {
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 30px;
  }
  .small-text {
    font-size: 20px;
  }
---

# <!-- fit --> 📊 Nemo 매물 데이터 심층 분석
## 비즈니스 전략 보고서

**20년 경력 수석 데이터 전략 분석가**
2026-04-28

---

## 1. 종합 시장 인사이트
### Comprehensive Market Insights

![bg right:40% 90%](./docs/images/market_trends.png)

서울 주요 권역(강남, 서초)의 상업용 부동산 시장 핵심 키워드:

1. **'초양극화'** (Hyper-Polarization)
2. **'실용성 중심의 재편'** (Shift to Utility)
3. **'데이터 기반의 가격 형성'**
   - 주관적 판단보다 객관적 지표 중심

---

### 1.1 시장의 구조적 특징 및 자산 양극화

<div class="columns">
<div>

- **정교한 임대료 체계**
  - 보증금-월세 상관계수 **0.82**
  - 입지, 면적에 따른 정량적 가격 형성

- **자산 양극화의 심화**
  - 권리금 평균 **4.2억 원** 상회
  - 하지만 **중앙값(Median)은 0원**
  - 상위 매물에 부가 가치 집중

</div>
<div>

![w:500](./docs/images/polarization.png)

</div>
</div>

---

### 1.2 지역적 집중도 및 분석

![bg left:45% 95%](./docs/images/heatmap.png)

- **'골든 트라이앵글'의 위상**
  - 역삼동(108.4) > 서초동(58.1)
  - 강남역(55.4) 순의 집중도

- **핵심 상권 결집**
  - 테헤란로와 강남대로 중심
  - 상업 부동산 거래의 절대적 심장부

---

## 2. 세부 지표 분석 (Statistical Details)

| 지표 | 평균 (Mean) | 중앙값 (Median) | 최댓값 (Max) |
| :--- | :---: | :---: | :---: |
| **보증금** | 6.13억 | 4.00억 | 200억 |
| **권리금** | 4.26억 | 0 | 900억 |
| **면적** | 124.03㎡ | 99.17㎡ | 1,225㎡ |
| **월세** | 5,500만 | 3,800만 | 12.5억 |

<p class="small-text" style="text-align:center; color:#94a3b8; margin-top:20px;">
*극단적 최댓값으로 인한 평균의 왜곡을 방지하기 위해 중앙값(Median) 참고 권장*
</p>

---

## 3. 시각화 분석 및 핵심 인사이트

- **업종별 매물 분포**: 
  - '범용 공간'(기타창업, 다용도) 비중 **50% 상회**
- **가격 유형**: 
  - 임대 매물이 **98.9%**로 압도적 유동성 중심
- **핵심 필터링 조건**: 
  - **'인테리어', '역세권', '1층'** 선호 뚜렷

---

## 4. 최종 결론 및 전략 제언

<div class="columns">
<div>

### 임차인 전략
- 권리금 **중앙값 0원** 시장 역이용
- 고급 인테리어 승계 매물 선점
- 초기 투자비 최소화 및 재무 안정

</div>
<div>

### 임대인 전략
- **범용성(Flexibility)** 확보 필수
- 인테리어 상태 유지가 공실 해소 관건
- 목적 변경 용이한 공간 구성

</div>
</div>

---

# <!-- fit --> 💡 Thank You!
**Nemo 데이터 분석 팀**

*본 보고서는 매물 데이터 1,071건을 정밀 분석한 결과입니다.*
