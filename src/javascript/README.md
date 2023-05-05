# Project-Rotten Viewer

This is a React Native Expo project, part of the Project-Rotten repository. It's a cross-platform mobile application that runs on Android, iOS, and the web.

## Prerequisites

Before setting up the project, make sure you have the following tools installed on your system:

- Node.js (latest LTS version): https://nodejs.org/
- Expo CLI: Install globally using `npm install -g expo-cli`

## Setting Up the Project

Follow these steps to set up and run the project on your local machine:

1. Open an administrator terminal in `Project-Rotten/src/javascript`
2. Install project dependencies: <br> ```npm install```
3. Install Expo Web components (Optional) <br> ```npx expo install react-native-web@~0.18.10 react-dom@18.2.0 @expo/webpack-config@^18.0.1```

## Running the Expo server
Follow these steps to run the Expo development server.
1. Open the `/src/javascript` folder in your IDE's integrated terminal. <br> ```cd Project-Rotten/src/javascript```
2. Start the development server: <br> ```npx expo start``` 
<br> This command will open a new browser window with the Expo Developer Tools.
3. From the Expo Developer Tools, you can run the app on Android, iOS, or a web browser by scanning the QR code or following the on-screen instructions.
4. Save changes in your IDE, they should be quickly reflected in the instance running on the connected mobile device.

## Running Expo Clients
### Android
1. Download [Expo](https://play.google.com/store/apps/details?id=host.exp.exponent) from the Google Play Store.
2. Scan the QR code provided by the server using the app.
### iOS
1. Cry because you spent too much money on a phone.
2. Scan the QR code using the native camera application.
### Web
1. Ensure you have followed step 3 of the set-up procedure.
2. In the Expo Server terminal press `w` to open the web viewer in your default browser.

## Debugging

Expo provides built-in debugging features, such as error reporting, performance monitoring, and logging. You can access these tools from the Expo Developer Tools in the browser, or by shaking your device while the app is running in development mode.
