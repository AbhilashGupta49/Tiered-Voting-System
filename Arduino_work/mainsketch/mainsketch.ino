#include <Keypad.h>
#include <LiquidCrystal.h>
char ch;
int Contrast=100;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {30, 31, 32, 33}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {34, 35, 36}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

const int button1=40;
const int button2=24;
const int button3=38;
const int button4=52;

const int led1=43;
const int led2=25;
const int led3=39;
const int led4=45;

int buttonState1=0;
int buttonState2=0;
int buttonState3=0;
int buttonState4=0;

void setup()
{
  analogWrite(9,10000);
pinMode(led1,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
pinMode(led4,OUTPUT);
pinMode(button1,INPUT_PULLUP);
pinMode(button2,INPUT_PULLUP);
pinMode(button3,INPUT_PULLUP);
pinMode(button4,INPUT_PULLUP);

Serial.begin(9600);
pinMode(13,OUTPUT);
  analogWrite(6,Contrast);
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  // Print a message to the LCD.
}

void loop(){
  digitalWrite(13,LOW);
  delay(1000); 
  digitalWrite(13,HIGH);
  lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Type Password  ");
  char keys[8],temp;
  int i=0;
  while(1){
    temp = keypad.waitForKey();
    if(temp=='#' || i>=8){
      break;
    }
    else if(temp=='*' && i>0){
      keys[i]='\0';
      i--;
      continue;
    }
    else if(temp=='*' && i==0){
      continue;
    }
    else{
      keys[i]=temp;
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Type Password  ");
      lcd.setCursor(0, 1);
      for(int j=0;j<=i;j++){
        lcd.print(keys[j]);
      }
      
      
      //Display 
      i++;
    }
    
      
       
  }
  keys[8]='\0';
  String final_key=String(keys);
  Serial.println(final_key);
  
  
  if (final_key=="11113333"){
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Vote Now");
    
    int flag=0,votenumber=0;
  
    while(flag!=1){  
      buttonState1=digitalRead(button1);
      buttonState2=digitalRead(button2);
      buttonState3=digitalRead(button3);
      buttonState4=digitalRead(button4);
      
      
       if(buttonState1==HIGH){
        digitalWrite(led1,HIGH);
        delay(2000);
        digitalWrite(led1,LOW);
        votenumber=1;
        flag=1;
        } 
       else if(buttonState2==HIGH){
        digitalWrite(led2,HIGH);
        delay(2000);
        digitalWrite(led2,LOW);
        votenumber=2;
        flag=1;
        }
        else if(buttonState3==HIGH){
        digitalWrite(led3,HIGH);
        delay(2000);
        digitalWrite(led3,LOW);
        votenumber=3;
        flag=1;
        }
        /*
        else if(buttonState4==HIGH){
        digitalWrite(led4,HIGH);
        delay(2000);
        digitalWrite(led4,LOW);
        votenumber=4;
        flag=1;
        }
        */
        Serial.println(votenumber);
    }
    lcd.clear();
    
    lcd.setCursor(0, 0);
    lcd.print("Voted");
    
  }
  else{
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Wrong");
    
  }
  for(int j=0;j<8;j++){
      keys[j]='\0';
      
  }
    
  }
