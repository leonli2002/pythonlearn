#include<iostream>
#include "code0.h"

void doNothing(int&)
{

}

void cout(void)
{
    std::cout<<"defined cout";
}

int main()
{
    // int i=5;
    // mylabel:
    //     cout<<"goto my label"<<endl;
    //     if(i-->0) goto mylabel;

    // int x;
    // doNothing(x);
    // cout<<x;

    cout();
    std::cout<<"\n standard cout\n";
    // cout<<"sizeof INT:"<<sizeof(int);
    std::cout<<fun_0(5);
    return 0;
}