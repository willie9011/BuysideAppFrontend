
| **屬性**            | **用法**                                                                 | **值範例**                                                                                               | **說明**                                                                                   |
|---------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **flex**            | 控制子項目如何分配空間                                                | `1`, `2`                                                                                               | 設定子項目占用父容器的空間比例。                                                         |
| **justifyContent**  | 設定主軸上項目的排列方式                                              | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly`                    | 子項目在主軸上的對齊方式。                                                               |
| **alignItems**      | 控制子項目在交叉軸上的對齊方式                                        | `flex-start`, `center`, `flex-end`, `stretch`, `baseline`                                              | 子項目在交叉軸上的對齊方式。                                                             |
| **flexDirection**   | 設定主軸方向                                                        | `row`, `row-reverse`, `column`, `column-reverse`                                                       | 子項目排列方向，水平方向或垂直方向。                                                     |
| **margin**          | 設定外邊距                                                          | `10`, `marginTop: 10`, `marginHorizontal: 20`                                                         | 與其他元素的距離。                                                                       |
| **padding**         | 設定內邊距                                                          | `10`, `paddingTop: 20`, `paddingHorizontal: 15`                                                       | 元素內容與邊框的距離。                                                                   |
| **width**           | 設定寬度                                                            | `100`, `'50%'`, `'auto'`                                                                               | 元素的寬度，支持像素或百分比。                                                           |
| **height**          | 設定高度                                                            | `200`, `'30%'`                                                                                        | 元素的高度，支持像素或百分比。                                                           |
| **backgroundColor** | 設定背景顏色                                                        | `'blue'`, `#ff0000`, `rgba(255,0,0,0.5)`                                                              | 元素的背景顏色。                                                                         |
| **borderWidth**     | 設定邊框寬度                                                        | `1`, `2`                                                                                               | 元素邊框的寬度。                                                                         |
| **borderColor**     | 設定邊框顏色                                                        | `'black'`, `#333333`                                                                                  | 元素邊框的顏色。                                                                         |
| **borderRadius**    | 設定圓角半徑                                                        | `10`, `50%`                                                                                           | 元素邊框的圓角大小。                                                                     |
| **position**        | 設定定位方式                                                        | `relative`, `absolute`                                                                                 | 元素相對於父容器或最近定位容器的位置。                                                   |
| **top, left, right, bottom** | 設定位置偏移量                                              | `10`, `20`                                                                                            | 搭配 `position` 使用，控制元素在容器中的偏移距離。                                       |
| **textAlign**       | 設定文字水平對齊方式                                                | `left`, `right`, `center`, `justify`                                                                  | 控制文字內容在水平方向的對齊方式。                                                       |

```javascript
const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#f8f8f8',
        padding: 20,
    },
    text: {
        fontSize: 18,
        textAlign: 'center',
        color: 'black',
    },
    box: {
        width: 100,
        height: 100,
        backgroundColor: 'blue',
        margin: 10,
        borderRadius: 10,
    },
});

```
