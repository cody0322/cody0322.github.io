#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
int main(void)
{
   srand( (unsigned)time(NULL));
   int max = 10, guessNo=0, guess=-1;
   printf("��J�W�U��(low, high):");
   int low, high;
   scanf("%d %d", &low, &high);
   int ans= low + rand() % (high - low + 1); 
   while(guess!=ans && guessNo<max)
   {
   	   printf("�вq�@�ӼƦr(%d ~ %d):", low, high);
   	   scanf("%d", &guess);
   	   guessNo++;
   	   if(ans==guess)
   	     printf("���߲q��F�A�@�q�F%d��", guessNo); 
   	   else
	   {
		    if(guess > ans )
		        high = guess-1;
		    else
			    low = guess+1;    		
	   }      	
   }
   if(guessNo == max && guess!=ans)
      printf("�ӻ��F��A�q�F %d�� �٨S�q��", guessNo);  

  system("pause");
  return 1;
}

