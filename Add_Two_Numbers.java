class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode temp1 = new ListNode(0);
        ListNode l3 = temp1;
        int carry = 0;
        while(l1!=null && l2!=null){
            int result = l1.val + l2.val + carry;
            int value = result % 10;
            carry = result / 10;
            ListNode newNode = new ListNode(value);
            l3.next = newNode;
            l3 = l3.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        while(l1!=null){
            int result = l1.val + carry;
            int value = result % 10;
            carry = result / 10;
            ListNode newNode = new ListNode(value);
            l3.next = newNode;
            l3 = l3.next;
            l1 = l1.next;
        }

        while(l2!=null){
            int result = l2.val + carry;
            int value = result % 10;
            carry = result / 10;
            ListNode newNode = new ListNode(value);
            l3.next = newNode;
            l3 = l3.next;
            l2 = l2.next;
        }

        if(carry>0){
           ListNode newNode = new ListNode(carry);
           l3.next = newNode;
           l3 = l3.next;
        }
        return temp1.next;
        
    }
}
