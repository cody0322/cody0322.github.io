#include <stdio.h>
#include <stdlib.h>
int main(void)
{
  char s[100];
  printf("��J�r��:"); 
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
  printf("�ഫ��:%s\n", s);
  printf("�j�g�^��:%d, �p�g�^��:%d, �Ʀr:%d", upper,lower,digit);
   system("pause"); 
   return 0;  
}  
