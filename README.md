# AWS 認證考試練習 | AWS Certification Quiz

線上雙語題庫練習網站，支援 AIF-C01（AI 從業者）與 CLF-C02（雲端從業者）兩張認證考試。

🌐 **網站連結**：[https://kevinzerocode.github.io/AWS_Certificate_Pratice/](https://kevinzerocode.github.io/AWS_Certificate_Pratice/)

---

## 功能說明 | Features

### 考試選擇
進入網站後，選擇要練習的考試科目：
- **AIF-C01** — AWS Certified AI Practitioner（AI 從業者）
- **CLF-C02** — AWS Certified Cloud Practitioner（雲端從業者）

### 三種練習模式

| 模式 | 說明 |
|------|------|
| 📋 完整考試 Full Exam | 將該科目所有題目隨機排序，完整作答 |
| 🎯 隨機練習 Practice | 自選題數（拖曳滑桿），從題庫隨機抽題練習 |
| 🔁 複習錯題 Review Wrong | 只出現過去答錯的題目，加強複習 |

### 答題功能
- **單選題**：點選選項即自動判斷
- **多選題**：勾選所有正確答案後點「確認 Submit」
- **解析面板**：每題作答後顯示每個選項的詳細說明
- **中英切換**：點右上角「中文 / EN」按鈕切換語言顯示

### 錯題記錄
- 答錯的題目會自動儲存在瀏覽器（localStorage）
- 下次進入網站，錯題記錄依然保留
- 可在選單頁點「清除記錄 Clear」重置
- **注意**：記錄儲存在各自裝置的瀏覽器中，不同裝置/瀏覽器的記錄不共用

### 成績頁面
- 顯示本次正確率與得分
- 列出本次答錯的題目與正確答案
- 可選擇重新練習、回選單或返回首頁

---

## 題庫來源

| 科目 | 題數 |
|------|------|
| AIF-C01 AI Practitioner | 271 題 |
| CLF-C02 Cloud Practitioner | 177 題 |
| **合計** | **448 題** |

---

## 本地端開發 | Local Development

若要在本地端重新產生題庫 HTML：

```bash
cd C:/Users/USER/Documents/AWS_Certificate_Pratice
python build_quiz.py
# 產生 aws_quiz.html
cp aws_quiz.html docs/index.html
```

需要安裝：
```bash
pip install pdfplumber wordninja
```

---

## 部署 | Deployment

本專案使用 **GitHub Pages** 從 `docs/` 資料夾提供靜態網頁服務。
推送至 `main` 分支後，網站自動更新。
