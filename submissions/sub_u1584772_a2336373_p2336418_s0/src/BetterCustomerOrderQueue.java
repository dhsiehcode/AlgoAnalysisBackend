/**
 * CS 251: Data Structures and Algorithms
 * Project 2: Part 3
 * <p>
 * TODO: Complete CustomerOrderQueue.
 *
 * @author: TODO
 * @username: TODO
 * @sources TODO: list your sources here
 */

import java.security.NoSuchAlgorithmException;


public class BetterCustomerOrderQueue {
    private CustomerOrder[] orderList;
    private CustomerOrderHash table;
    private int numOrders;

    /**
     *
     * Return the CustomerOrderQueue
     *
     */
    public CustomerOrder[] getOrderList() {
        return orderList;
    }

    /**
     *
     * Return the number of orders in the queue
     *
     */
    public int getNumOrders() {
        return numOrders;
    }


    /**
     * Constructor of the class.
     * TODO: complete the default Constructor of the class
     *
     * Initialize a new CustomerOrderQueue and CustomerOrderHash
     *
     */
    public BetterCustomerOrderQueue(int capacity) {
        orderList = new CustomerOrder[capacity];
        table = new CustomerOrderHash(capacity);
        numOrders = 0;
    }

    /**
     * TODO: insert a new customer order.
     *
     * @return return the index at which the customer was inserted;
     * return -1 if the Customer could not be inserted
     *
     */
    public int insert(CustomerOrder c) throws NoSuchAlgorithmException {

        if (numOrders == orderList.length) {
            return -1;
        }

        if (table.get(c.getName()) != null) {
            return -1;
        }

        numOrders++;
        c.setPosInQueue(numOrders - 1);
        orderList[numOrders - 1] = c;

        int loc = numOrders - 1;



        if (loc == 0) {


            /**
            System.out.print("Current customers: ");
            for (int i = 0; i < numOrders; i++) {
                System.out.print(orderList[i].getOrderDeliveryTime() + " ");
            }
            System.out.println(); **/
            table.put(c);
            return loc;
        }

        /**
        System.out.print("Current customers: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + " ");
        }
        System.out.println();
         **/

        int pos = swimUp(loc);


        /**
         * enter into hashtable
         */

        table.put(c);

        return pos;
    }

    /**
     * lets a node swim up
     * @param pos the position in the array it is currently in
     * @return new position
     */
    private int swimUp(int pos) {

        if (pos <= 0) {
            return pos;
        }

        if (orderList[pos].compareTo(orderList[(pos - 1) / 2]) == 1) {
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
    public CustomerOrder delMax() throws NoSuchAlgorithmException {


        //System.out.println("delMax called");

        if (numOrders <= 0) {
            return null;
        }

        /**
         * delMax from queue
         */

        orderList[0].setPosInQueue(-1);

        CustomerOrder toRemove = orderList[0];

        /**
         * remove from hash table
         */
        table.remove(toRemove.getName());


        orderList[0] = orderList[numOrders - 1];

        if (numOrders == 1) {
            numOrders--;
            return toRemove;
        }
        orderList[numOrders - 1] = null;
        orderList[0].setPosInQueue(0);
        numOrders--;

        sinkDown(0);

        /**
        System.out.print("After delMax: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + " ");
        }
        System.out.println();
        **/



        return toRemove;

    }

    /**
     * recursively sinks a node numbered by pos down
     * @param pos
     */
    private void sinkDown(int pos) {

        if (pos >= (numOrders / 2)) {
            return;
        }

        int left = 2 * pos + 1;
        int right = 2 * pos + 2;

        CustomerOrder cur = orderList[pos];

        /**
         * must check if right is null
         */

        if (orderList[right] == null && orderList[pos].compareTo(orderList[left]) == -1) {
            cur.setPosInQueue(left);
            orderList[pos] = orderList[left];
            orderList[pos].setPosInQueue(pos);
            orderList[left] = cur;
            sinkDown(left);
            return;
        } else if (orderList[right] == null && orderList[pos].compareTo(orderList[left]) == 1) {
            return;
        }

        /**
         * must check if left is null
         */

        if (orderList[left] == null && orderList[pos].compareTo(orderList[right]) == -1) {
            cur.setPosInQueue(right);
            orderList[pos] = orderList[right];
            orderList[pos].setPosInQueue(pos);
            orderList[right] = cur;
            sinkDown(left);
            return;
        } else if (orderList[left] == null && orderList[pos].compareTo(orderList[right]) == 1) {
            return;
        }

        if ((orderList[pos].compareTo(orderList[left]) == 1) && (orderList[pos].compareTo(orderList[right]) == 1)) {
            return;
        } else if ((orderList[pos].compareTo(orderList[left]) == 1) && (orderList[pos].compareTo(orderList[right]) == -1)) {
            //swap pos and right
            cur.setPosInQueue(right);
            orderList[pos] = orderList[right];
            orderList[pos].setPosInQueue(pos);
            orderList[right] = cur;
            sinkDown(right);
        } else if ((orderList[pos].compareTo(orderList[left]) == -1) && (orderList[pos].compareTo(orderList[right]) == 1)) {
            //swap pos and left
            cur.setPosInQueue(left);
            orderList[pos] = orderList[left];
            orderList[pos].setPosInQueue(pos);
            orderList[left] = cur;
            sinkDown(left);
        } else if ((orderList[pos].compareTo(orderList[left]) == -1) && (orderList[pos].compareTo(orderList[right]) == -1)) {
            if (orderList[left].compareTo(orderList[right]) == 1) {
                //swap pos and left
                cur.setPosInQueue(left);
                orderList[pos] = orderList[left];
                orderList[pos].setPosInQueue(pos);
                orderList[left] = cur;
                sinkDown(left);
            } else if (orderList[left].compareTo(orderList[right]) == -1) {
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
     * TODO: return but do not remove the customer with the maximum priority
     *
     * @return return the customer with the maximum priority
     *
     */
    public CustomerOrder getMax() {

        return orderList[0];
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
     * TODO: return the number of Customers currently in the queue
     *
     * @return return the number of Customers currently in the queue
     *
     */
    public int size() {
        return numOrders;
    }

    /**
     *
     * TODO: return the CustomerOrder with the given name
     *
     */
    public CustomerOrder get(String name) throws NoSuchAlgorithmException {
        return table.get(name);
    }

    /**
     *
     * TODO: remove and return the CustomerOrder with the specified name from the queue;
     * TODO: return null if the CustomerOrder isn't in the queue
     *
     */
    public CustomerOrder remove(String name) throws NoSuchAlgorithmException {

        /**
        System.out.print("Before: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + "(" + orderList[i].getPosInQueue() + ") ");
        }
        System.out.println();

        System.out.println("remove called on pos:" + table.get(name).getPosInQueue() + " delivery time:" + table.get(name).getOrderDeliveryTime());
        **/


        CustomerOrder toRemove = table.remove(name);

        if (toRemove == null) {
            return null;
        }

        /** removes from queue **/

        int posInQueue = toRemove.getPosInQueue();

        partialQueueDelMax(posInQueue);

        toRemove.setPosInQueue(-1);


        /**
        System.out.print("After: ");
        for (int i = 0; i < numOrders; i++) {
            System.out.print(orderList[i].getOrderDeliveryTime() + "(" + orderList[i].getPosInQueue() + ") ");
        }
        System.out.println();**/

        return toRemove;
    }

    /**
     *
     * TODO: update the orderDeliveryTime of the Customer with the specified name to newTime
     *
     */
    public void update(String name, int newTime) throws NoSuchAlgorithmException {

        /**
         System.out.println("Original time:" + table.get(name).getOrderDeliveryTime() + " New time: " + newTime);

         System.out.print("Before: ");
         for (int i = 0; i < numOrders; i++) {
         System.out.print(orderList[i].getPosInQueue() + " ");
         }
         System.out.println();
         **/


        if (table.get(name) == null) {
            return;
        }

        table.get(name).setOrderDeliveryTime(newTime);


        int posInQueue = table.get(name).getPosInQueue();

        orderList[posInQueue].setOrderDeliveryTime(newTime);

        if (posInQueue == 0) {
            sinkDown(posInQueue);
        } else if (posInQueue > 0 && posInQueue < numOrders/2) {
            sinkDown(posInQueue);
            swimUp(posInQueue);
        } else {
            swimUp(posInQueue);
        }


        /**
         System.out.print("After: ");
         for (int i = 0; i < numOrders; i++) {
         System.out.print(orderList[i].getPosInQueue() + " ");
         }
         System.out.println();
         **/

    }

    /**
     * removes and returns CustomerOrder fixed at pos. also fixes the queue
     * @param pos
     * @return
     */
    private CustomerOrder partialQueueDelMax(int pos) {

        if (numOrders <= 0) {
            return null;
        }

        if (pos == (numOrders - 1)) {
            CustomerOrder toRemove = orderList[pos];
            orderList[pos].setPosInQueue(0);
            orderList[numOrders - 1] = null;
            numOrders--;
            return toRemove;
        }


        orderList[pos].setPosInQueue(0);

        CustomerOrder toRemove = orderList[pos];


        orderList[pos] = orderList[numOrders - 1];

        if (numOrders == 1) {
            numOrders--;
            return toRemove;
        }
        orderList[numOrders - 1] = null;
        orderList[pos].setPosInQueue(pos);
        numOrders--;

        if (pos == 0) {
            sinkDown(pos);
        } else if (pos > 0 && pos < numOrders/2) {
            sinkDown(pos);
            swimUp(pos);
        } else {
            swimUp(pos);
        }

        return toRemove;
    }


}
