#include <stdio.h>
#include <stdlib.h>
int s(int b)
{
    int fy = b + 1911;  
      
    if( fy % 400 == 0   )  
        return 1;  
    else if ( (fy % 4) == 0  && (fy % 100 != 0 ) )  
       return 1;  
         
    else  
        return 0;
}  
int main()
{
	int a , b;
	scanf("%d" , &a);
	b=s(a);
	//printf("%d\n" , b);
	switch(b)
	{
		case 1:
			printf("366\n");
			break;
		case 0:
			printf("365\n");
			break; 
	}
	
	system("pause");   
    return 0;  
}
