# ComfyUI-Character-Style-Selector
ComfyUI Prompt Multiple Styles Selector の魔改造品です。

Character_Style_Selectorのフォルダごとcustom_nodesフォルダに入れると使えます。

画像にワークフローのサンプルが入っています。

ウエイトは「無し」をスルーして上から順番にかかります。
一つのセレクタプロンプト内に複数のトークンがある場合は、まとめてウエイトがかかりますが、「,（スペース）」で区切って最大5個まで個別にウエイトがかけれます。
そのため、CSV内のトークンには通常スペースを入れません。
