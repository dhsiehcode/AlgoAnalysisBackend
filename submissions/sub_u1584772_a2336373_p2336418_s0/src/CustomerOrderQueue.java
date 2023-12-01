/**
 * CS 251: Data Structures and Algorithms
 * Project 2: Part 1
 *
 * TODO: Complete CustomerOrderQueue.
 *
 * @author: TODO
 * @username: TODO
 * @sources TODO: list your sources here
 */


public class CustomerOrderQueue {
    private CustomerOrder[] orderList;
    private int numOrders;

    /**
     *
     * @return return the priority queue
     *
     */
    public CustomerOrder[] getOrderList() {
        return orderList;
    }

    /**
     *
     * @return return the number of orders
     *
     */
    public int getNumOrders() {
        return this.numOrders;
    }

    /**
     * Constructor of the class.
     * TODO: complete the default Constructor of the class
     *
     * Initilalize a new CustomerOrder array with the argument passed.
     *
     */
    public CustomerOrderQueue(int capacity) {
        orderList = new CustomerOrder[capacity];
        numOrders = 0;
    }

    /**
     * TODO: insert a new customer order into the priority queue.
     *
     * @return return the index at which the customer was inserted
     *
     */
    public int insert(CustomerOrder c) {



        if (numOrders == orderList.length) {
            return -1;
        }

        numOrders++;
        c.setPosInQueue(numOrders - 1);
        orderList[numOrders - 1] = c;

        int loc = numOrders - 1;



        if (loc == 0) {
            System.out.print("Current customers: ");
            for (int i = 0; i < numOrders; i++) {
                System.out.print(orderList[i].getOrderDeliveryTime() + " ");
            }
            System.out.println();
            return loc;
        }

        System.out.print("Current customers: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + " ");
        }
        System.out.println();

        int pos = swimUp(loc);
        return pos;
    }

    /**
     * lets a node swim p
     * @param pos the position in the array it is currently in
     * @return new position
     */
    private int swimUp(int pos) {

        if (pos <= 0) {
            return pos;
        }

        if (orderList[pos].compareTo(orderList[(pos - 1) / 2]) == 1) {
            System.out.println("swimming up");
            CustomerOrder temp = orderList[(pos - 1) / 2];
            orderList[(pos - 1) / 2] = orderList[pos];
            orderList[(pos - 1) / 2].setPosInQueue((pos - 1) / 2);
            orderList[pos] = temp;
            orderList[pos].setPosInQueue(pos);

            return swimUp((pos - 1)/2);
        }

        return pos;
    }

    /**
     * TODO: remove the customer with the highest priority from the queue
     *
     * @return return the customer removed
     *
     */
    public CustomerOrder delMax() {

        System.out.println("delMax called");

        if (numOrders <= 0) {
            return null;
        }

        /**
         * removing the first element
         */


        CustomerOrder toRemove = orderList[0];
        orderList[0] = orderList[numOrders - 1];

        if (numOrders == 1) {
            numOrders--;
            return toRemove;
        }
        orderList[numOrders - 1] = null;
        orderList[0].setPosInQueue(0);
        numOrders--;
        int loc = 0;

        /**
         * begin sinking down
         */


        sinkDown(0);

        System.out.print("After delMax: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + " ");
        }
        System.out.println();

        return toRemove;
    }

    /**
     * recursively sinks a node numbered by pos down
     * @param pos
     */
    private void sinkDown(int pos) {

        System.out.print("sinking...");

        if (pos >= (numOrders/2)) {
            System.out.println("No child");
            return;
        }

        int left = 2 * pos + 1;
        int right = 2 * pos + 2;

        CustomerOrder cur = orderList[pos];

        /**
         * must check if right is null
         */

        if (orderList[right] == null && orderList[pos].compareTo(orderList[left]) == -1) {
            System.out.println("right child null swap");
            cur.setPosInQueue(left);

            orderList[pos] = orderList[left];
            orderList[pos].setPosInQueue(pos);

            orderList[left] = cur;

            sinkDown(left);
            return;
        } else if (orderList[right] == null && orderList[pos].compareTo(orderList[left]) == 1)  {
            System.out.println("right child null no swap");
            return;
        }

        /**
         * must check if left is null
         */

        if (orderList[left] == null && orderList[pos].compareTo(orderList[right]) == -1) {
            System.out.println("left child null swap");
            cur.setPosInQueue(right);

            orderList[pos] = orderList[right];
            orderList[pos].setPosInQueue(pos);

            orderList[right] = cur;

            sinkDown(left);
            return;
        } else if (orderList[left] == null && orderList[pos].compareTo(orderList[right]) == 1)  {
            System.out.println("left child null no swap");
            return;
        }

        if ((orderList[pos].compareTo(orderList[left]) == 1) && (orderList[pos].compareTo(orderList[right]) == 1)) {
            System.out.println("Current before both child");
            return;
        } else if ((orderList[pos].compareTo(orderList[left]) == 1) && (orderList[pos].compareTo(orderList[right]) == -1)) {
            System.out.println("swap pos and right");
            //swap pos and right

            cur.setPosInQueue(right);

            orderList[pos] = orderList[right];
            orderList[pos].setPosInQueue(pos);

            orderList[right] = cur;

            sinkDown(right);

        } else if ((orderList[pos].compareTo(orderList[left]) == -1) && (orderList[pos].compareTo(orderList[right]) == 1)) {
            System.out.println("swap pos and left");
            //swap pos and left

            cur.setPosInQueue(left);

            orderList[pos] = orderList[left];
            orderList[pos].setPosInQueue(pos);

            orderList[left] = cur;

            sinkDown(left);
        } else if ((orderList[pos].compareTo(orderList[left]) == -1) && (orderList[pos].compareTo(orderList[right]) == -1)) {
            if (orderList[left].compareTo(orderList[right]) == 1) {
                System.out.println("swap pos and left");
                //swap pos and left

                cur.setPosInQueue(left);

                orderList[pos] = orderList[left];
                orderList[pos].setPosInQueue(pos);

                orderList[left] = cur;

                sinkDown(left);
            } else if (orderList[left].compareTo(orderList[right]) == -1) {
                System.out.println("swap pos and right");
                //swap pos and right

                cur.setPosInQueue(right);

                orderList[pos] = orderList[right];
                orderList[pos].setPosInQueue(pos);

                orderList[right] = cur;

                sinkDown(right);
            }
        }


    }

    /**
     * TODO: return the number of Customers currently in the queue
     *
     * @return return the number of Customers currently in the queue
     *
     */
    public int size() {
        return numOrders;
    }

    /**
     * TODO: check if the priority queue is empty or not
     *
     * @return return true if the queue is empty; false else
     *
     */
    public boolean isEmpty() {
        return numOrders == 0;
    }

    /**
     * TODO: return but do not remove the customer with the maximum priority
     *
     * @return return the customer with the maximum priority
     *
     */
    public CustomerOrder getMax() {
        return orderList[0];
    }

}
