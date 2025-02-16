// app/(tabs)
import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

const Create = () => {
    return (
        <View style={styles.container}>
            <Text>Create</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default Create;
