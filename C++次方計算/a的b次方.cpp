#include <stdio.h>
#include <stdlib.h>
int main(void)
{
   int a , b , i;  
   int ans = 1;  
   scanf ("%d %d",&a,&b);  
   for (i = 1; i <=b ; i++)  
      ans = ans * a ; 
   printf("%dªº%d¦¸¤è=%d\n",a,b,ans);  
     
   system("pause");  
   return 0;  
}  
