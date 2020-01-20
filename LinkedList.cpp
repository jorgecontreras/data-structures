//https://www.codesdope.com/blog/article/c-linked-lists-in-c-singly-linked-list/

#include <iostream>

using namespace std;

struct node 
{
    int data;
    node *next;
};

class list
{
    private:
        node *head, *tail;

    public:
        list()
        {
            head = NULL;
            tail = NULL;
        }

        void add_node(int n)
        {
            node *tmp = new node;
            tmp->data = n;
            tmp->next = NULL;

            if(head == NULL){
                head = tmp;
                tail = tmp;
            } 
            else
            {
                tail->next = tmp;
                tail = tail->next;
            } 
        }
};

int main()
{
    cout << "Linked List";
    list a;
    a.add_node(1);
    a.add_node(2);
    return 0;
}
