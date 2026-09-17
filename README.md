# English LADDER

高校英語の授業・家庭学習をつなぐ学習アプリです。`avenirplus/english-ladder` を正本とします。

## 現在の運用
- 教科: 英語
- 2026年度の既定科目: 論理・表現Ⅰ (`LE1`)
- アプリ本体は年度・科目・クラスから独立させる
- 教材は `materials/` 以下の JSON と `materials/manifest.json` で管理する
- 生徒の学習履歴はプロフィール単位、年度・科目は `learningContext`、クラス・番号は `studentInfo` で識別する

## 暗唱ラダー
1. きく
2. ならべる（句）
3. ならべる（語）
4. かく

Stage 1〜3 は `noRead: true` とし、解答前に英文音声を聞けないようにします。解答後は正解英文の読み上げと3回音読チェックを利用できます。

## 構成
- `index.html`: v3 bootstrap。設定・教材JSONを読み込み、既存コアを互換モードで起動
- `app-core-v2.5.0.html`: 2026-07-16時点の実績あるコアを凍結保存
- `config/app-config.json`: アプリ名・保存キー・現在の既定年度/科目
- `materials/manifest.json`: 配布教材一覧
- `materials/<年度>/<科目>/<lesson>/`: 教材JSON
- `docs/`: 設計・運用の正本

新教材は巨大な `index.html` に直接焼き込まず、原則JSONを追加してください。
