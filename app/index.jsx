// app/
import {StatusBar} from 'expo-status-bar';
import {ScrollView, Text, View} from 'react-native';
import{Redirect,router} from 'expo-router';
import{SafeAreaView} from "react-native-safe-area-context";
import{images} from "../constants"
import {Image} from "expo-image";
import CustomButton from "../components/CustomButton";


export default function App(){
    return (

     <SafeAreaView className = "bg-orange-700 h-full">

        <ScrollView contentContainerStyle={{height:"80%"}}>
            <View className = "w-full justify-center items-center h-full px-4 ">


                <Image
                    source={images.BuysideLogo}

                    style={{ width: 260, height: 200, resizeMode: 'contain' }}
                />

                <Text className="text-sm font-pregular text-gray-100 mt-7 text-center">
                    finding the right price with Buyside
                </Text>

                <CustomButton
                    title = "Continue with Email"
                    handlePress={() =>router.push('/sign-in')}   //router.push 可以將使用者導向特定頁面
                    containerStyles="w-full mt-7"
                />



            </View>
        </ScrollView>

         {/*讀條*/}
         <StatusBar backgroundColor ='#161622' style="light" />
     </SafeAreaView>

    );
}
