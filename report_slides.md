---
marp: true
theme: gaia
_class: lead
backgroundColor: #f0f0f0
color: #000
paginate: true
header: "Nemo 매물 데이터 심층 분석 보고서"
footer: "© 2026 Nemo Data Analytics Team"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;700&family=Noto+Sans+KR:wght@400;900&display=swap');

  section {
    font-family: 'Archivo', 'Noto Sans KR', sans-serif;
    background-color: #f0f0f0;
    padding: 50px;
    border: 8px solid #000;
  }
  h1 {
    font-family: 'Archivo Black', 'Noto Sans KR', sans-serif;
    font-weight: 900;
    color: #000;
    font-size: 70px;
    text-transform: uppercase;
    background-color: #ffde03;
    padding: 20px;
    border: 6px solid #000;
    box-shadow: 12px 12px 0px #000;
    display: inline-block;
    margin-bottom: 40px;
  }
  h2 {
    font-family: 'Archivo Black', 'Noto Sans KR', sans-serif;
    color: #000;
    font-size: 50px;
    background-color: #ff52af;
    padding: 10px 20px;
    border: 5px solid #000;
    box-shadow: 8px 8px 0px #000;
    display: inline-block;
  }
  h3 {
    font-family: 'Archivo Black', 'Noto Sans KR', sans-serif;
    color: #000;
    font-size: 35px;
    background-color: #00ffa3;
    padding: 5px 15px;
    border: 4px solid #000;
    box-shadow: 6px 6px 0px #000;
    display: inline-block;
    margin-top: 20px;
  }
  p, li {
    font-size: 26px;
    font-weight: 700;
    line-height: 1.4;
    color: #000;
  }
  strong {
    background-color: #ffde03;
    padding: 0 5px;
    border: 2px solid #000;
  }
  footer {
    font-weight: 900;
    color: #000;
    background-color: #00ffa3;
    border-top: 5px solid #000;
  }
  img {
    border: 6px solid #000;
    box-shadow: 15px 15px 0px #000;
    border-radius: 0px !important;
  }
  table {
    border: 6px solid #000;
    box-shadow: 10px 10px 0px #000;
    background-color: #fff;
    width: 100%;
  }
  th {
    background-color: #ffde03;
    border-bottom: 5px solid #000 !important;
    color: #000 !important;
    font-weight: 900;
  }
  td {
    border: 3px solid #000 !important;
    font-weight: 700;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 40px;
    align-items: center;
  }
  .small-text {
    font-size: 18px;
    background: #fff;
    border: 2px solid #000;
    padding: 5px;
  }
---

# <!-- fit --> 📊 Nemo DATA
## 전략 보고서 v2.0

**20년 경력 수석 데이터 분석가**
2026-04-28

<!--
[발표자 노트 - 1페이지]
새롭게 단장한 네오브루탈리즘 스타일의 보고서입니다. 강렬한 대비와 굵은 선을 통해 데이터의 메시지를 더욱 확실하게 전달하겠습니다. 1,071건의 매물 데이터를 기반으로 한 비즈니스 전략, 지금 시작합니다.
-->

---

## 1. 시장 인사이트
### MARKET INSIGHTS

![bg right:45% 85%](./docs/images/market_trends.png)

1. **'초양극화'** (Hyper-Gap)
2. **'실용성 중심'** (Utility First)
3. **'데이터 가격'** (Data-Driven)

<!--
[발표자 노트 - 2페이지]
네오브루탈리즘 디자인처럼 시장도 매우 선명하게 갈리고 있습니다. 상위 매물에 모든 가치가 집중되는 초양극화 현상이 가속화되고 있습니다.
-->

---

### 1.1 구조적 특징

<div class="columns">
<div>

- **정교한 임대료**
  - 상관계수 **0.82** (강력함)
- **자산 양극화**
  - 권리금 평균 **4.2억**
  - **중앙값은 0원!**
  - (상위 매물 독점)

</div>
<div>

![w:500](./docs/images/polarization.png)

</div>
</div>

<!--
[발표자 노트 - 3페이지]
보증금과 월세의 상관계수 0.82는 시장의 논리가 매우 견고함을 뜻합니다. 하지만 권리금 중앙값 0원은 시장의 허상을 보여주는 결정적 증거입니다.
-->

---

### 1.2 지역 집중도

![bg left:48% 95%](./docs/images/heatmap.png)

- **'골든 트라이앵글'**
  - **역삼동(108.4)** 압도적
  - 서초동(58.1)
  - 강남역(55.4)
- **핵심 상권**
  - 테헤란로/강남대로 집중

<!--
[발표자 노트 - 4페이지]
히트맵을 보시면 강남의 심장부가 어디인지 한눈에 알 수 있습니다. 역삼동의 집중도는 타 지역을 압도합니다.
-->

---

## 2. 세부 지표 분석

| 지표 | 평균 (Mean) | 중앙값 (Med) | 최댓값 (Max) |
| :--- | :---: | :---: | :---: |
| **보증금** | 6.13억 | **4.00억** | 200억 |
| **권리금** | 4.26억 | **0** | 900억 |
| **면적** | 124.03㎡ | **99.17㎡** | 1,225㎡ |
| **월세** | 5,500만 | **3,800만** | 12.5억 |

<p class="small-text" style="text-align:center; margin-top:20px;">
*평균의 함정에 빠지지 마십시오. 중앙값이 실체입니다.*
</p>

<!--
[발표자 노트 - 5페이지]
평균 5,500만 원의 월세는 허상일 수 있습니다. 우리가 주목해야 할 실제 거래 기준점은 3,800만 원입니다.
-->

---

## 3. 핵심 인사이트

- **업종 분포**: 
  - 범용 공간 비중 **50% 상회**
- **가격 유형**: 
  - 임대 매물 **98.9%** (압도적)
- **필터링 조건**: 
  - **'인테리어', '역세권', '1층'**

<!--
[발표자 노트 - 6페이지]
임차인들은 이제 특정 용도가 아닌 '다용도'로 쓸 수 있는 유연한 공간을 원합니다. 인테리어 완비 여부가 계약의 핵심입니다.
-->

---

## 4. 전략 제언

<div class="columns">
<div>

### 임차인 전략
- **권리금 0원** 시장 공략
- 인테리어 승계로 비용 절감
- 데이터 기반 협상

</div>
<div>

### 임대인 전략
- **유연한 공간** 구성
- 인테리어 유지보수 강화
- 공실 리스크 선제 대응

</div>
</div>

<!--
[발표자 노트 - 7페이지]
임차인은 스마트하게 권리금 없는 옥석을 가려야 하고, 임대인은 공간의 유연성을 확보해야 살아남을 수 있습니다.
-->

---

# <!-- fit --> 💡 DONE!
**Nemo Data Team**

*1,071건의 데이터가 증명하는 전략*

<!--
[발표자 노트 - 8페이지]
데이터는 거짓말을 하지 않습니다. 이 강렬한 데이터의 신호를 비즈니스의 기회로 만드시길 바랍니다. 감사합니다.
-->
