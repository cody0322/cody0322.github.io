#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int a,b,c;  
    scanf("%d %d %d", &a, &b, &c);  
    if( a+b > c && a+c > b && b+c > a   )  
    {  
        printf("�X�z");  
        if(a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a)    
            printf(",�����T����");  
        else  
            printf(",���O�����T����");   
    }  
    else  
        printf("���X�z");  
    printf("\n");  
  
    system("pause");   
    return 0;  
}  
