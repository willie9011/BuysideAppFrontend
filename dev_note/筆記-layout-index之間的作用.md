### 假設的場景

你有一個網站，主要分為三個部分：

1. **導航欄**（放在頁面的最上方，固定顯示）。
2. **主內容**（根據不同的頁面顯示不同的內容，比如首頁內容或關於頁面的內容）。
3. **頁腳**（放在頁面的最下方，固定顯示）。

---

### 對應的檔案

* `_layout.jsx`：負責定義「導航欄 + 主內容（插入子頁面） + 頁腳」的外層結構。
* `index.jsx`：負責定義首頁的內容。
* `about.jsx`（假設有這個檔案）：負責定義關於頁面的內容。

---

### `_layout.jsx` 的內容

```javascript
import { View, Text, StyleSheet } from 'react-native';
import { Slot } from 'expo-router';

const Layout = () => {
  return (
    <View style={styles.container}>
      {/* 固定的導航欄 */}
      <View style={styles.navbar}>
        <Text>導航欄</Text>
      </View>

      {/* 主內容（插入子頁面） */}
      <Slot />

      {/* 固定的頁腳 */}
      <View style={styles.footer}>
        <Text>頁腳</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  navbar: {
    height: 50,
    backgroundColor: 'lightblue',
    justifyContent: 'center',
    alignItems: 'center',
  },
  footer: {
    height: 50,
    backgroundColor: 'lightgray',
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default Layout;

```

---

### `index.jsx` 的內容

```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function Hom() {
  return (
    <View style={styles.container}>
      <Text>歡迎來到首頁！</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

---

### `about.jsx` 的內容

```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function About() {
  return (
    <View style={styles.container}>
      <Text>這是關於我們的頁面。</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

```

---

### 運作原理

1. 當用戶訪問首頁（`/`）：
   * `_layout.jsx` 先被渲染，顯示「導航欄」和「頁腳」。
   * `Slot` 會插入 `index.jsx`，顯示「歡迎來到首頁！」。
2. 當用戶訪問關於頁面（`/about`）：
   * `_layout.jsx` 先被渲染，顯示「導航欄」和「頁腳」。
   * `Slot` 會插入 `about.jsx`，顯示「這是關於我們的頁面」。

---

### 顯示結果

#### 訪問 `/`（首頁）

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">markdown</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="複製"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>複製程式碼</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-markdown">導航欄
-------------------
歡迎來到首頁！
-------------------
頁腳
</code></div></div></pre>

#### 訪問 `/about`（關於頁面）

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">markdown</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="複製"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>複製程式碼</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-markdown">導航欄
-------------------
這是關於我們的頁面。
-------------------
頁腳
</code></div></div></pre>

---

### 為什麼要這樣設計？

1. **減少重複代碼**：
   * 「導航欄」和「頁腳」是固定的，不需要每個頁面都寫一遍。
   * 只需要寫一次 `_layout.jsx`，然後用 `Slot` 把子頁面的內容插入即可。
2. **模組化結構**：
   * 每個頁面（如 `index.jsx`、`about.jsx`）只需要關注自己的內容，讓程式碼更清晰、易維護。
1.

* 父組件（如 `_layout.jsx`）負責提供通用的框架結構。
* 子組件（如 `index.jsx`、`about.jsx`）只需專注自己的內容，通過插槽（`Slot`）自動插入到父組件中。


### 簡單對比：`_layout.jsx` vs `index.jsx`


| **檔案名稱**  | **用途**                   | **內容**                         | **範例**                                        |
| ------------- | -------------------------- | -------------------------------- | ----------------------------------------------- |
| `_layout.jsx` | 定義頁面外層結構與通用樣式 | 導航欄、頁腳、背景樣式、整體框架 | 將`<Slot />`作為子頁面內容的佔位符              |
| `index.jsx`   | 定義頁面具體內容           | 文字、按鈕、圖片等用於展示的內容 | 子頁面內容會自動插入到`_layout.jsx`的`<Slot />` |
