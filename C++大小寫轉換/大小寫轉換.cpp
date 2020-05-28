#include <stdio.h>
#include <stdlib.h>
int main(void)
{
  char s[100];
  printf("輸入字串:"); 
  gets(s); 
  int i = 0, upper=0, lower=0, digit=0;
  while(s[i] !='\0')
  {
  	  if(s[i] >='A' && s[i] <='Z')
  	  {
  	     s[i] = s[i] - 'A' + 'a';
  	     upper++;
      }  	  
  	  else if (s[i] >='a' && s[i] <='z')
  	  {
  	  	 s[i] = s[i] - 'a' + 'A';
  	  	 lower++;
	  } 
  	  else if (s[i] >='0' && s[i]<='9')
		   digit++;   
	 i++;	   
  }
  printf("轉換後:%s\n", s);
  printf("大寫英文:%d, 小寫英文:%d, 數字:%d", upper,lower,digit);
   system("pause"); 
   return 0;  
}  
