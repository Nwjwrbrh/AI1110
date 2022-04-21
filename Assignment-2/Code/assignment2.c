#include<stdio.h>
#include<math.h>
int main(){
    for (float x = 0; x < 1; x += 0.1)
    {
      if (asin(x)+asin(1-x) == acos(x) && x != 0)
      {
        printf("The solution to the equation is x = %f",x);
      }
    }  
    return 0;
}