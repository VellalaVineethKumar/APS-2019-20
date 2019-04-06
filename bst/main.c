/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>


typedef struct bst
{
    int data;
    struct bst *left;
    struct bst *right;
    
}BST;

BST * insert_bst(BST * root)
{
    BST *newnode;
    newnode=(BST*)malloc(sizeof(BST));
    
    if(newnode==NULL){
        printf("mem error\n");
        return root;
    }
    
    
    printf("enter new element \n");
    scanf("%d",&newnode->data);
    newnode->left=NULL;
    newnode->right=NULL;
    
    if(root==NULL)
    {
        return newnode;
    }
    
    BST *prev=NULL,*cur=root;
    
    while(cur!=NULL)
    {
        prev=cur;
        
        if(cur->data>newnode->data)
        {
            cur=cur->left;
        }
        else
        {
            cur=cur->right;
        }
    }
    
    if(prev->data>newnode->data)
    {
        prev->left=newnode;
        
    }
    else
    prev->right=newnode;
    
    
    return root;
}


void inorder(BST *root){
    
    
    if(root!=NULL)
    {
        inorder(root->left);
        
        printf("%d",root->data);
        
        inorder(root->right);
    }
}




BST *delete_bst(BST *root)
{
    if(root==NULL){
        
        printf("epmty tree\n")
        return root;
    }
    
    int  data;
    printf("Enter data element\n");
    scanf("%d",data);
    
    
    BST *parent,*curr,*succ,*p;
    
    cur=root;
    
    parent=NULL;
    
    while(curr!=NULL && curr->data!=data)
    {
        parent=curr;
        
        if(curr->data>data){
            curr=curr->left;
        }
        else
        {
            curr=curr->right;
        }
        
        if(curr==NULL){
            printf("element not found\n");
            return root;
        }
        
        if(curr->left==NULL){
            p=curr->right;
        }
        
        else if(curr->right==NULL)
        p=cur->left;
        
        else{
            
            succ=curr->right;
            
            while(succ->left!=NULL){
                succ=succ->left;
                succ->left=curr->left;
                p=curr->right;
            }
            
            if(parent==NULL){
                free(curr);
                return p;
            }
            if(p==curr->left)
            {
                parent->left=p;
            }
            else
            {
                parent->right=p;
            }
        }
        
    free(curr);
    return root;
        
    }
}

int main()
{
    printf("Hello World");

    return 0;
}
