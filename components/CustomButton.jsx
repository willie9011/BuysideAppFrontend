import React from 'react';
import {TouchableOpacity,Text} from 'react-native';

const CustomButton = ({title,handlePress,containerStyles,textStyles,isLoading}) => {
    return (
        <TouchableOpacity
            //設定讀取條
            className={`bg-amber-500 rounded-xl min-h-[62px] justify-center items-center ${containerStyles} ${isLoading ? 'opacity-50':''}`}
            disabled={isLoading}

            onPress={handlePress}
            activeOpacity={0.7}


        >
            {/*設定字體*/}
            <Text className={`text - gray - 950 font-semibold text-lg ${textStyles}`}>{title}</Text>
        </TouchableOpacity>
    );
};


export default CustomButton;
