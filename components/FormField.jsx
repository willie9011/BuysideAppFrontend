import React, { useState, useCallback } from 'react';
import { View, Text, TextInput, TouchableOpacity, Image } from 'react-native';
import { icons } from '../constants';

const FormField = ({
                       title,
                       value,
                       placeholder,
                       handleChangeText,
                       otherStyles,
                       ...props
                   }) => {
    const [hidePassword, setHidePassword] = useState(true);
    const isPassword = title.toLowerCase() === "password";

    // 新增：用來處理文字變更的回調函數
    const onChangeText = useCallback((text) => {
        if (handleChangeText) {
            handleChangeText(text);
        }
    }, [handleChangeText]);

    return (
        <View className={`space-y-2 ${otherStyles}`}>
            <Text className="text-base text-gray-100 font-pmedium">
                {title}
            </Text>

            <View className="border-2 border-amber-50 w-full h-16 px-4 bg-black-100 rounded-2xl focus:border-secondary flex-row">
                <TextInput
                    style={{
                        flex: 1,
                        width: '100%',
                        color: 'white',
                        paddingRight: 40
                    }}
                    className="flex-1 text-white font-psemibold text-base"
                    value={value}  // 確保這裡使用父元件傳入的value
                    placeholder={placeholder}
                    placeholderTextColor="rgba(255, 255, 255, 0.5)"
                    onChangeText={onChangeText}  // 使用新的回調函數
                    secureTextEntry={isPassword && hidePassword}
                    {...props}
                />
                {isPassword && (
                    <TouchableOpacity
                        onPress={() => setHidePassword(prev => !prev)}
                        style={{
                            position: 'absolute',
                            right: 16,
                            height: '100%',
                            justifyContent: 'center'
                        }}
                    >
                        <Image
                            source={hidePassword ? icons.eyeHide : icons.eye}
                            className="w-6 h-6"
                            resizeMode="contain"
                        />
                    </TouchableOpacity>
                )}
            </View>
        </View>
    );
};

export default FormField;