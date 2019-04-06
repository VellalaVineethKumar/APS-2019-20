#include <stdio.h>
#define ss 5

	struct stack{
	    int items[ss];
	    int top;
	    int rear;
	};
	typedef struct stack S;	
	


int main(void) {
	// your code goes here
	S s;
	s.top=0;
	s.rear=-1;
	
	int choice;
	while(1)
	{
	  	printf("enter your option 1)enque \n2)dequeue \n3)print \n");
	scanf("%d",&choice);
	switch(choice)
	{
	    
	    case 1:
	   enque(&s);
	   break;
	   
	   case 2:
	   dequeue(&s);
	   break;
	   
	   case 3:
	   print(&s);
	   break;
	}  
	    
	}
}



	void enque(S *s)
	{
	    if(s->top==ss-1)
	    {
	        printf("queue full\n");
	    }
	    else
	    {
	        int x;
	        printf("enter a numbers\n");
	        scanf("%d",x);
	        s->items[++(s->top)]=x;
	        s->rear++;
	    }
	}
		void dequeue(S *s)
	{
	    if(s->top==-1)
	    {
	        printf("queue emply\n");
	    }
	    else
	    {
            int x;
	        x=s->items[(s->top)--];
	        s->rear--;
	        printf("dequeued elemet  is %d\n",x);
	    }
	}
	



