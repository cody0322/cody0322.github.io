#include <stdio.h>
#include <stdlib.h>
int main()
{
	int op , x;
	int ary[10]={10 , 50 , 20};
	int num=3;
	while(2)
	{
		printf("\n**********************\n*1.��J���          *\n*2.�L�X���          *\n*3.�L�X�ϰ}�C        *\n*4.�Ƨ�              *\n*0.����              *\n**********************\n");
		printf("�п�J�ﶵ:" , op);
		scanf("%d" , &op);
		if(op==0)
			break;
		switch(op)
		{
			case 1:
				printf("��J:" , x);
				scanf("%d" , &x);
				ary[num]=x;
				num++;
				break;
			case 2:
				for( int i=0; i<num ; i++)
					if(i==0)
						printf("%d" , ary[i]);
					else
						printf(",%d" , ary[i]);
					break;
			case 3:
				for(int a=num-1; a>=0 ; a--)
					if(a==num-1)
						printf("%d" , ary[a]);
					else
						printf(",%d" , ary[a]);
					break;
			case 4:
				for(int i=0; i<num ; i++){
					for(int j=1 ; j<num-i-1 ; j++){
						if(ary[j]>ary[j+1]){
							int big=ary[j];
							ary[j]=ary[j+1];
							ary[j+1]=big;
						}
					}
				}
				for(int p=0 ; p<num ; p++)
				if(p==0)
						printf("%d" , ary[p]);
					else
						printf(",%d" , ary[p]);
				break;
		}
	}
   system("pause");
   return 1;
}

