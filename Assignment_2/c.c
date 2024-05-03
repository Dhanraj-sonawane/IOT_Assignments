
#include<stdio.h>
#pragma pack(1)
int main()
{
    struct emp 
    {
        short a;
        int b;
    };

 struct emp var={5,120};
 printf("%hd %d",var.a,var.b);

    
}