## 1.Stack 、Slot 、Link 的使用

```javascript
//_layout
import { Slot ,Stack} from "expo-router"; //Sloat 為靜態加載index 的佔位符只能一層 ////Stack 則是動態加載可以好幾層 
import{useFonts} from "expo-font";
import "../global.css";

export default function Layout() {
    return (
        <Stack direction="row" spacing={2}>
            <Slot/>
        </Stack>
    );
}
```

```javascript
//index.jsx
import {StatusBar} from 'expo-status-bar';
import {Text,View} from 'react-native';
import{Link} from 'expo-router'; //用來置入 其他檔案的

export default function App(){
    return (
        <View className='flex-1 items-center justify-center bg-amber-600'>   //windtail 的css屬性條
            <Text className = "font-black items-center justify-center ">well come to buyside!</Text> 
            <StatusBar status="auto" /> //裝置上面的屬性條
            <Link href="profile.jsx" style={{color:'white'}}>  
                click here to navigate to Profile
            </Link>
        </View>
    );
}

```

---

## 2. import useFonts from "expo-font" 來一次讀取多個字形

```javascript
import { Slot ,Stack} from "expo-router";
import "../global.css"; // 確保這個路徑是正確的
import{useFonts} from "expo-font";

export default function Layout() {
  
    const [fontsLoaded,error] = useFonts(        //<-----------------   
        {"Poppins-Black":require("../assets/fonts/Poppins-Black.ttf")}, //<-----
        {"Poppins-Medium":require("../assets/fonts/Poppins-Medium.ttf")}, //<-------
    );
  
    return (
        <Stack direction="row" spacing={2}>
            <Slot/>
        </Stack>
    );
}

```

## 3. useEffect

基本用法:

```javascript
useEffect(() => {
  // 副作用邏輯，例如 API 請求或 DOM 操作
  return () => {
    // 清理邏輯，可選，通常用於移除事件監聽或清理資源
  };
}, [dependencies]); // 依賴陣列

```

```javascript
    useEffect( () => {
        if (error) throw error;
        if(fontsLoaded) throw SplashScreen.hideAsync();
    }, [fontsLoaded,error]);

    if (!fontsLoaded && !error) return null;
```

### **`useFonts`的功能**

* **加載自定義字體**：你可以通過 `useFonts` 同時加載多個自定義字體。
* **返回字體加載狀態**：它返回一個布林值 `fontsLoaded`，表示字體是否成功加載。
* **避免閃爍問題**：在字體加載完成前，你可以延遲渲染，避免顯示默認系統字體或發生閃爍。



### **`throw error` 的作用**

* **拋出錯誤**：`throw` 是一個語句，用來中止程式碼的執行並拋出錯誤，通常會觸發 `try...catch` 的錯誤處理邏輯，或者（如果沒有捕捉）讓應用程式停止並記錄錯誤。
* **表示程式邏輯中出現了非預期的情況**：用 `throw` 明確告訴程式某個操作無法成功，這通常用於異常情境。



### `SplashScreen` 的功能

1. **展示啟動畫面**
   * 啟動畫面通常是一個簡單的圖像或品牌標誌，讓使用者知道應用正在載入，並提供一個專業且一致的第一印象。
2. **隱藏啟動畫面**
   * 當應用程式載入完成（例如資源加載、API 請求完成或其他初始化邏輯結束後），可以使用 **SplashScreen.hideAsync()** 來隱藏啟動畫面，顯示應用的主畫面。
3. **阻止啟動畫面過早隱藏(SplashScreen.preventAutoHideAsync())**
   * 預設情況下，啟動畫面可能會在應用還未準備好時隱藏，這可能導致主畫面閃爍或白屏。 **SplashScreen** 提供了一個手動隱藏的機制，確保在應用載入完成前，啟動畫面不會消失。

```javascript
import {Slot, SplashScreen, Stack} from "expo-router";
import "../global.css"; // 確保這個路徑是正確的
import{useFonts} from "expo-font";
import {useEffect} from "react";

SplashScreen.preventAutoHideAsync();   //<-----放在開頭阻止程式還沒跑好之前就消失
```
