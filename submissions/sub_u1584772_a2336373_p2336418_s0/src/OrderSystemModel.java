/**
 * CS 251: Data Structures and Algorithms
 * Project 2: Part 4
 *
 * TODO: Complete OrderSystemModel.
 *
 * @author: TODO
 * @username: TODO
 * @sources TODO: list your sources here
 */

import java.security.NoSuchAlgorithmException;

public class OrderSystemModel {
    private BetterCustomerOrderQueue orderList;
    private int capacityThreshold;
    private int ordersDelayed;
    private int ordersOnTime;
    private int ordersCanceled;
    private int time;
    private int totalDelayTime;

    public int getOrdersDelayed() {
        return ordersDelayed;
    }

    public int getOrdersOnTime() {
        return ordersOnTime;
    }

    public int getOrdersCanceled() {
        return ordersCanceled;
    }

    public int getTotalDelayTime() {
        return totalDelayTime;
    }

    public BetterCustomerOrderQueue getOrderList() {
        return orderList;
    }

    /**
     * Constructor of the class.
     *
     * Initialize a new OrderSystemModel and OrderSystemModel
     *
     */
    public OrderSystemModel(int capacityThreshold) {
        this.capacityThreshold = capacityThreshold;
        this.orderList = new BetterCustomerOrderQueue(this.capacityThreshold);
        this.ordersDelayed = 0;
        this.ordersOnTime = 0;
        this.ordersCanceled = 0;
        this.time = 0;
        this.totalDelayTime = 0;
    }


    /**
     *
     * TODO: Process a new CustomerOrder with a given name.
     *
     */
    public String process(String name, int orderTime, int deliveryTime) throws NoSuchAlgorithmException {


        int result = orderList.insert(new CustomerOrder(name, orderTime, deliveryTime));

        if (result != -1) {
            System.out.println("Added: " + name);
            return name;
        }



        /**
         * if new order is earlier than current time, complete the new order
         */
        if (deliveryTime < orderList.getMax().getOrderDeliveryTime()) {
            time++;
            if (time > deliveryTime) {
                ordersDelayed++;
                totalDelayTime += (time - deliveryTime);
            } else {
                ordersOnTime++;
            }
            return null;
        }

        /**
         * if new order is later
         */

        CustomerOrder queueMax = orderList.delMax();

        time++;
        if (time > queueMax.getOrderDeliveryTime()) {
            ordersDelayed++;
            totalDelayTime += (time - queueMax.getOrderDeliveryTime());
        } else {
            ordersOnTime++;
        }
        orderList.insert(new CustomerOrder(name, orderTime, deliveryTime));

        System.out.println("Added: " + name);

        return queueMax.getName();
    }

    /**
     *
     * TODO: Complete the highest priority order
     *
     */
    public String completeNextOrder() throws NoSuchAlgorithmException {


        if (orderList.isEmpty()) {
            return null;
        }

        CustomerOrder completedOrder = orderList.delMax();

        time++;

        if (time > completedOrder.getOrderDeliveryTime()) {
            ordersDelayed++;
            totalDelayTime += (time - completedOrder.getOrderDeliveryTime());
        } else {
            ordersOnTime++;
        }

        System.out.println("Completed: " + completedOrder.getName());

        return completedOrder.getName();
    }

    /**
     *
     * TODO: Update the delivery time of the order for the given name
     *
     */
    public String updateOrderTime(String name, int newDeliveryTime) throws NoSuchAlgorithmException {

        if (orderList.size() == 0) {return null;}

        CustomerOrder order = orderList.get(name);

        if (order == null) {
            System.out.println("Updating: no such customer");
            return null;
        }

        System.out.println("Updating: " + name + " from " + order.getOrderDeliveryTime() + " to " + newDeliveryTime + " @ " + time);

        if (orderList.getMax().getOrderDeliveryTime() > newDeliveryTime) {

            orderList.update(name, newDeliveryTime);

            orderList.remove(name);

            time++;
            ordersOnTime++;

            return name;
        }

        /*if (newDeliveryTime < time && order.getOrderDeliveryTime() > time) {
            orderList.remove(name);
            System.out.println("Cancelled:" + name + " at time: " + time);
            ordersCanceled++;
        }*/

        orderList.update(name, newDeliveryTime);

        return null;
    }

    /**
     *
     * TODO: Cancel the order for the given name
     *
     */
    public CustomerOrder cancelOrder(String name) throws NoSuchAlgorithmException {

        CustomerOrder[] orders = orderList.getOrderList();

        System.out.println();

        for (int i = 0;  i < orders.length; i++) {
            if (orders[i] != null) {
                System.out.print(orders[i].getName() + " (" + i + ") ");
            }
        }

        System.out.println();

        if (name == null) {
            return null;
        }

        System.out.print("Cancelling: " + name);

        CustomerOrder cancelled = orderList.remove(name);

        System.out.println("Cancelled:" + cancelled.getName());

        if (cancelled == null) {
            System.out.println("doesn't exist");
            return null;
        }


        ordersCanceled++;
        return cancelled;
    }


}
