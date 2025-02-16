// app/(auth)
import React from 'react';
import {View, Text, StyleSheet, ScrollView,Image} from 'react-native';
import {SafeAreaView} from "react-native-safe-area-context";
import {images} from '../../constants';
import FormField from "../../components/FormField";
import CustomButton from "../../components/CustomButton";
import {Link} from "expo-router";

const SignIn = () => {
    const [form,setForm] = React.useState({
        email:"",
        password:""
    });

    const [isSubmitting, setIsSubmitting] = React.useState(false);

    const submit = ()=>{

    }

    return (
     <SafeAreaView className = "bg-orange-700 h-full">
        <ScrollView>
            <View className = "bg-orange-700 h-full justify-content-center  px-4 my-2 mt-10"

            >
                <View style ={{ alignItems: 'center'}}>
                    <Image
                    source={images.BuysideLogo}
                    resizeMode = "contain"
                    style={{ width: 100, height: 100, resizeMode: 'contain', alignItems:"center"}}
                    />
                    <View className="justify-center flex-row gap-2">

                        <Text className="text-2xl text-white text-semibold mt-10">Well come !</Text>

                    </View>
                </View>


                <FormField
                    title = "Email"
                    value ={form.email}
                    handleChangeText = {(e) => setForm({...form, email: e})}
                    otherStyles = "mt-5"
                    keyboardType="email-address"
                />

                <FormField
                    title = "Password"
                    value ={form.password}
                    handleChangeText = {(e) => setForm({...form, password: e})}
                    otherStyles="mt-5 mb-12"
                />

                <CustomButton
                    title="Sign in"
                    handlePress = {submit}
                    containerStyle="mt-6"
                    isLoading ={isSubmitting}
                />
                {/*flex-row	讓子元素水平排列（橫向）	把原本直排的元素變成橫排*/}
                {/*gap-2	讓子元素之間有間距	讓每個元素之間有 2 單位的距離*/}
                <View className="justify-center pt-5 flex-row gap-2">
                    <Text className="  text-white">
                        Dont have account?
                    </Text>
                    <Link href="/sign-up" className="text-blue-800   font-medium">
                        Sign up
                    </Link>

                </View>
            </View>
        </ScrollView>
     </SafeAreaView>
    );
};



export default SignIn;
