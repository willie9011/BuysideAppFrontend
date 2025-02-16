// /app/(tabs)
import { View, Text } from 'react-native';
import { Tabs } from "expo-router";
import { Image } from "expo-image";
import { icons } from '../../constants';


// ----------------------------------- 設定導航欄 "圖片配置" 的地方-----------------------------------
const TabIconConfig = ({ icon, color, name, focused }) => {
    return (
        <View className="items-center justify-center gap-2">
            <Image
                source={icon}
                style={{ width: 24, height: 24, resizeMode: 'contain' }} //<----resizemode 歸類在style了
                tintColor={color}
                className="w-6 h-6"
            />
        </View>
    );
};

// ----------------------------------------------導航欄-------------------------------------------------------
const TabsLayout = () => {
    return (
        //--------------------------------------導航欄配置------------------------------
        <Tabs
            screenOptions={{
                // 是否顯示標籤頁文字，設置為 false 會隱藏文字，只顯示圖標
                tabBarShowLabel: false,
                // 當前活動標籤頁（選中）圖示的顏色
                tabBarActiveTintColor: '#FFA001', // 橙色
                // 非活動標籤頁（未選中）圖示的顏色
                tabBarInactiveTintColor: '#CDCDE0', // 灰藍色
                // 設置整體導航欄的樣式
                tabBarStyle: {
                    // 導航欄的背景顏色設置為深灰色
                    backgroundColor: '#161622',
                    // 設置導航欄的上邊框寬度為 1 像素
                    borderTopWidth: 1,
                    // 設置上邊框的顏色為稍淺的灰色
                    borderTopColor: '#232533',
                    // 設置導航欄的高度為 84 像素
                    height: 84,
                },
            }}
        >
            {/*------------------------------ Home 鍵 ----------------------------------------*/}
            <Tabs.Screen
                name="home"
                options={{
                    title: 'Home',
                    headerShown: false, // 完全隱藏標頭
                    headerStyle: false,
                    tabBarIcon: ({ color, focused }) => (
                        <TabIconConfig
                            icon={icons.home}
                            color={color}
                            name="Home"
                            focused={focused}
                        />
                    ),
                }}
            />

            {/*------------------------------ Bookmark 鍵----------------------------------------*/}

            <Tabs.Screen
                name="bookmark"
                options={{
                    title: 'Bookmark',
                    headerShown: false, // 完全隱藏標頭
                    headerStyle: false,
                    tabBarIcon: ({ color, focused }) => (
                        <TabIconConfig
                            icon={icons.bookmark}
                            color={color}
                            name="Bookmark"
                            focused={focused}
                        />
                    ),
                }}
            />

            {/*-------------------------------- Create 鍵----------------------------------------*/}
            <Tabs.Screen
                name="create"
                options={{
                    title: 'Create',
                    headerShown: false, // 完全隱藏標頭
                    headerStyle: false,
                    tabBarIcon: ({ color, focused }) => (
                        <TabIconConfig
                            icon={icons.plus}
                            color={color}
                            name="Create"
                            focused={focused}
                        />
                    ),
                }}
            />

            {/*-------------------------------- Profile 鍵----------------------------------------*/}
            <Tabs.Screen
                name="profile"
                options={{
                    title: 'Profile',
                    headerShown: false, // 完全隱藏標頭
                    headerStyle: false,
                    tabBarIcon: ({ color, focused }) => (
                        <TabIconConfig
                            icon={icons.profile}
                            color={color}
                            name="Profile"
                            focused={focused}
                        />
                    ),
                }}
            />
        </Tabs>
    );
};

export default TabsLayout;
