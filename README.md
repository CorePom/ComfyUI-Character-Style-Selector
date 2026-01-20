# ComfyUI-Character-Style-Selector
ComfyUI Prompt Multiple Styles Selector の魔改造品です。

Character_Style_Selectorのフォルダごとcustom_nodesフォルダに入れると使えます。

画像にワークフローのサンプルが入っています。

ウエイトは「無し」をスルーして上から順番にかかります。
一つのセレクタプロンプト内に複数のトークンがある場合は、まとめてウエイトがかかりますが、「,（スペース）」で区切って最大5個まで個別にウエイトがかけれます。
そのため、CSV内のトークンには通常スペースを入れません。

# ComfyUI-Character-Style-Selector

CSVベースでスタイルを選択する ComfyUI カスタムノード集です。

## インストール

1. このリポジトリを ZIP でダウンロード
2. `Character_Style_Selector` フォルダを `ComfyUI/custom_nodes/` に置く
3. ComfyUI を再起動

## 使い方

1. 各 Style Selector で項目を選択
2. Prompt Slot Processor でコスプレ衣装
3. Weight Selector で重み付け

## 注意

- CSV 内のカンマ後のスペースは禁止（`, ` は重みのプロンプト区切り用）
