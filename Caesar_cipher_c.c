#include <stdio.h>
#include <string.h>

void MakeCryption(char* plain_text, char* cryption_txt);
void PrintCryption(const char* cryption_txt);
void MakeDecryption(char* cryption_txt, char* decryption_txt);
void PrintDecryption(const char* decryption_txt);

int main(void) {
    char plain_text[100], cryption_txt[100], decryption_txt[100];

    printf("Write your message: ");
    scanf("%s", plain_text);  

    MakeCryption(plain_text, cryption_txt);  
    PrintCryption(cryption_txt);

    MakeDecryption(cryption_txt, decryption_txt);  
    PrintDecryption(decryption_txt);

    return 0;
}

void MakeCryption(char* plain_text, char* cryption_txt) {
    int i;
    for (i = 0; i < strlen(plain_text); i++) {
        cryption_txt[i] = plain_text[i] + 3;  
    }
    cryption_txt[i] = '\0';  
}

void PrintCryption(const char* cryption_txt) {
    printf("Cryption: %s\n", cryption_txt);
}

void MakeDecryption(char* cryption_txt, char* decryption_txt) {
    int i;
    for (i = 0; i < strlen(cryption_txt); i++) {
        decryption_txt[i] = cryption_txt[i] - 3;  
    }
    decryption_txt[i] = '\0'; 
}

void PrintDecryption(const char* decryption_txt) {
    printf("Decryption: %s\n", decryption_txt);
}
