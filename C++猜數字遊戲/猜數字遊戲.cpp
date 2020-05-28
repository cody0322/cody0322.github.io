#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
int main(void)
{
   srand( (unsigned)time(NULL));
   int max = 10, guessNo=0, guess=-1;
   printf("輸入上下限(low, high):");
   int low, high;
   scanf("%d %d", &low, &high);
   int ans= low + rand() % (high - low + 1); 
   while(guess!=ans && guessNo<max)
   {
   	   printf("請猜一個數字(%d ~ %d):", low, high);
   	   scanf("%d", &guess);
   	   guessNo++;
   	   if(ans==guess)
   	     printf("恭喜猜對了，共猜了%d次", guessNo); 
   	   else
	   {
		    if(guess > ans )
		        high = guess-1;
		    else
			    low = guess+1;    		
	   }      	
   }
   if(guessNo == max && guess!=ans)
      printf("太遜了喔，猜了 %d次 還沒猜中", guessNo);  

  system("pause");
  return 1;
}

