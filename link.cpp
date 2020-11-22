#include <stdio.h>
#include <stdlib.h>
class  linkNode {
	public:
	int data;
    linkNode*  ptr = NULL;
} ; 
void prt( linkNode*  tmp ) {//印出內容 

    while ( tmp->ptr != NULL)  {
         printf("data=%d  ",tmp->data);
         tmp = tmp->ptr ;
}
printf("data=%d  ",tmp->data);
}

void  add ( linkNode*  tmp, int  i)  {//加入數值 
     
    while ( tmp->ptr != NULL)  {
         tmp = tmp->ptr ;
}

linkNode* node = new linkNode;
node->data = i ;  
tmp->ptr = node;
}

int snode(linkNode* tmp , int x , int ans)//尋找並插入 
{

	while(tmp->ptr!=NULL)
	{
		if(tmp->data == x)
		{
			
			linkNode *newnode;
			newnode = (linkNode *) malloc(sizeof(linkNode));
			newnode->data = ans;
			newnode->ptr = tmp->ptr;
			tmp->ptr=newnode;

			break;
		}
		tmp = tmp->ptr;
	}

}



int main(int argc, char** argv) {
	int sw , x , pl;
	linkNode*  first = new linkNode;
	first->data=0;
	/*prt(first);
	add(first,1);
	add(first,3); add(first,5);  prt(first);
	add(first,7); add(first,9); add(first,11); prt(first);
	snode(first, 1 , 2);
	printf("\n");
	prt(first);*/
	for(;;)
	{
		printf("\n選擇執行：\n0.結束\n1.新增資料\n2.印出資料\n3.插入資料\n");
		scanf("%d" , &sw);
		if (sw == 0)
		{
			break;
		}
		switch(sw)
		{
			case 1:
			{	
				printf("輸入資料:");
				scanf("%d" , &x);
				add(first , x);
				break;
			}
			case 2:
			{
				prt(first);
				break;
			}
			case 3:
			{
				printf("請輸入要插入的位置:");
				scanf("%d" , &pl);
				printf("請輸入插入的資料:");
				scanf("%d" , &x);
				snode(first,pl , x);
				break;
			}
		}
	}
	return 0;
}


