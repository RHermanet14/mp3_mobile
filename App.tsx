import { useState } from 'react';
import { Alert, Button, StyleSheet, TextInput} from 'react-native';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';

function downloadURL(url: string) {
  Alert.alert("downloading " + url);
}

export default function App() {
  const [url, onChangeURL] = useState('');
  return (
    <SafeAreaProvider style={styles.provider}>
      <SafeAreaView>
        <TextInput
          style={styles.input}
          onChangeText={onChangeURL}
          placeholder='Enter any valid YouTube URL.'
          value={url}
        />
        <Button
          title="Download"
          onPress={() => downloadURL(url)}
        />
      </SafeAreaView>
    </SafeAreaProvider>
    
  );
};

const styles = StyleSheet.create({
  provider: {
    justifyContent:'center',
    alignItems:'center'
  },
  input: {
    height:40,
    width:200,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
  submit: {

  }
})