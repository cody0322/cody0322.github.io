#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int a,b,c;  
    scanf("%d %d %d", &a, &b, &c);  
    if( a+b > c && a+c > b && b+c > a   )  
    {  
        printf("合理");  
        if(a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a)    
            printf(",直角三角形");  
        else  
            printf(",不是直角三角形");   
    }  
    else  
        printf("不合理");  
    printf("\n");  
  
    system("pause");   
    return 0;  
}  
