#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 int main()
 {
     int n,i;
     float p,m,z;
     scanf("%d",&n);
     int a[n];
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
         if(a[i]>0)
         {
             p++;
         }
         else if(a[i]<0)
         {
             m++;
         }
         else{
             z++;
         }
          
     }
     p=p/n;
     z=z/n;
     m=m/n;
     printf("%f",p);
    printf("\n%f",m);
   printf("\n%f",z);
     
     return 0;

     
     
          

     
 }
