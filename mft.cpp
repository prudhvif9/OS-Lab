#include<iostream> 

using namespace std; 

int main() 

{ 

          int fragment[20],b[20],p[20],i,j,nb,np,temp,lowest=9999,flags[10], allocation[10],pm,highest=0,temp1; 

          static int barray[20],parray[20],bar[20],par[20]; 

          cout<<"Enter the size of physical memory for user processes:"; 

          cin>>pm; 

          cout<<"\nBEST FIT"; 

          cout<<"\nEnter the number of partitions:"; 

          cin>>nb; 

          cout<<"Enter the number of processes:"; 

          cin>>np; 

          cout<<"\nEnter the size of the partitions:-\n"; 

          for(i=1;i<=nb;i++) 

    { 

        cout<<"Partition no."<<i<<":"; 

        cin>>b[i]; 

    } 

          cout<<"\nEnter the size of the processes :-\n"; 

          for(i=1;i<=np;i++) 

    { 

        cout<<"Process no. "<<i<<":"; 

        cin>>p[i]; 

    } 

          for(i=1;i<=np;i++) 

          { 

                   for(j=1;j<=nb;j++) 

                   { 

                             if(barray[j]!=1) 

                             { 

                                      temp=b[j]-p[i]; 

                                      if(temp>=0) 

                                                if(lowest>temp) 

                                                { 

                                                          parray[i]=j; 

                                                          lowest=temp; 

                                      } 

                             } 

  

                   } 

                   fragment[i]=lowest; 

        barray[parray[i]]=1; 

        lowest=10000; 

          } 

          cout<<"\nProcess_no\tProcess_size\tBlock_no\tBlock_size\tFragment"; 

          for(i=1;i<=np && parray[i]!=0;i++) 

          cout<<"\n"<<i<<"\t\t"<<p[i]<<"\t\t"<<parray[i]<<"\t\t"<<b[parray[i]]<<"\t\t"<<fragment[i]; 

    for(i = 0; i < 10; i++) 

          { 

                   flags[i] = 0; 

                   allocation[i] = -1; 

          } 

    for(i = 1; i <= np; i++)         //allocation as per first fit 

                   for(j = 1; j <= nb; j++) 

                             if(flags[j] == 0 && b[j] >= p[i]) 

                             { 

                                      allocation[j] = i; 

                                      flags[j] = 1; 

                                      break; 

                             } 

          //display allocation details 

          cout<<"\n\nFIRST FIT"; 

          cout<<"\nBlock no.\tsize\t\tprocess no.\t\tsize\t\tInternal-Fragmentation"; 

          for(i = 1; i <=nb; i++) 

          { 

                   cout<<"\n"<< i<<"\t\t"<<b[i]<<"\t\t"; 

                   if(flags[i] == 1) 

                             cout<<allocation[i]+1<<"\t\t\t"<<p[allocation[i]]<<"\t\t\t"<<b[i]-p[allocation[i]]; 

                   else 

                             cout<<"Not allocated"; 

          } 

          cout<<"\n\nWORST FIT"; 

    for(i=1;i<=np;i++) 

          { 

                   for(j=1;j<=nb;j++) 

                   { 

                             if(bar[j]!=1) 

                             { 

                                      temp1=b[j]-p[i]; 

                                      if(temp1>=0) 

                                                if(highest<temp1) 

                                                { 

                                                          par[i]=j; 

                                                          highest=temp1; 

                                                } 

                             } 

                   } 

                   fragment[i]=highest; 

        bar[par[i]]=1; 

        highest=0; 

          } 

          cout<<"\nProcess_no\tProcess_size\tBlock_no\tBlock_size\tFragment"; 

          for(i=1;i<=np && par[i]!=0;i++) 

          cout<<"\n"<<i<<"\t\t"<<p[i]<<"\t\t"<<par[i]<<"\t\t"<<b[par[i]]<<"\t\t"<<fragment[i]; 

          return 0; 

} 
