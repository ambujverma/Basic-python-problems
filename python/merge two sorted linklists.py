SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
    
    if (head1 == NULL && head2 == NULL) return NULL;
    else if (head1 == NULL) return head2;
    else if (head2 == NULL) return head1;

    if(head1->data <= head2->data)
    head1->next = mergeLists(head1->next, head2);

    else {
    SinglyLinkedListNode*temp = head2;
    head2 = head2->next;
    temp->next = head1;
    head1 = temp;
    head1->next = mergeLists(head1->next, head2);
    }

    return(head1);


}