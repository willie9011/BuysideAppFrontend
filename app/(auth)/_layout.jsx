// app/(auth)
import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

import {Stack} from "expo-router";
import {StatusBar} from "expo-status-bar";

const AuthLayout = () => {
    return (
      <>
          <Stack>
              <Stack.Screen
                name = "sign-in"
                options = {{
                      headerShown: false,
                }}
              />
              <Stack.Screen
                  name = "sign-up"
                  options = {{
                      headerShown: false,
                  }}
              />
          </Stack>
          <StatusBar backgroundcolor = "#161622" style={"light"}/>
      </>
    );
}




export default AuthLayout;
