#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int tall;  
    float m, wei, bmi;  
    scanf("%d %f",&tall,&wei);    
    m =  tall / 100.0f;    
    bmi = wei / ( m*m );  
    if (bmi>=24)  
        printf("%.2f �ӭD\n",bmi);  
    else if (bmi<18)  
        printf("%.2f �ӽG\n",bmi);  
    else  
        printf("%.2f �з�\n",bmi);  
    system("pause");     
    return 0;  
}  
