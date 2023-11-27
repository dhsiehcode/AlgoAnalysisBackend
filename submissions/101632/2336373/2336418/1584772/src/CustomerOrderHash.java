/**
 * CS 251: Data Structures and Algorithms
 * Project 2: Part 2
 *
 * TODO: Complete CustomerOrderHash.
 *
 * @author: TODO
 * @username: TODO
 * @sources TODO: list your sources here
 */

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;


public class CustomerOrderHash {
    private ArrayList[] table;
    private int numOrders;
    private int tableCapacity;

    /**
     * Constructor of the class.
     * TODO: complete the default Constructor of the class
     *
     * Initilalize a new CustomerOrder array with the argument passed.
     *
     */
    public CustomerOrderHash(int capacity) {
        if (isPrime(capacity)) {
            table = new ArrayList[capacity];
        } else {
            table = new ArrayList[getNextPrime(capacity)];
        }
       numOrders = 0;
       tableCapacity = table.length;
    }

    private int getHashCode(String s) throws NoSuchAlgorithmException {
        MessageDigest digest =  MessageDigest.getInstance("SHA-256");
        byte[] inBytes = digest.digest(s.getBytes());
        String byteOutput = new String(inBytes);


        int hashCode = byteOutput.hashCode();

        hashCode = hashCode % tableCapacity;

        if (hashCode < 0) {
            hashCode += tableCapacity;
        }

        return hashCode;
    }


    /**
     *
     * TODO: return the CustomerOrder with the given name
     * TODO: return null if the CustomerOrder is not in the table
     *
     */
    public CustomerOrder get(String name) throws NoSuchAlgorithmException {

        if (name == null) {
            return null;
        }

        int hashCode = getHashCode(name);

        if (table[hashCode] == null) {
            return null;
        }


        for (int i = 0; i < table[hashCode].size(); i++) {
            CustomerOrder curOrder = (CustomerOrder) table[hashCode].get(i);
            if (name.equals(curOrder.getName())) {
                return curOrder;
            }
        }

        
        return null;
    }


    /**
     *
     * TODO: put CustomerOrder c into the table
     *
     */
    public void put(CustomerOrder c) throws NoSuchAlgorithmException {

        if (c == null) {
            return;
        }

        String name = c.getName();

        if (get(name) != null) {
            return;
        }

        int hashCode = getHashCode(name);

        //System.out.println("Storing " + c.getName() + " at " + hashCode);

        if (table[hashCode] == null) {
            table[hashCode] = new ArrayList();
        }

        table[hashCode].add(c);
        numOrders++;
    }



    /**
     *
     * TODO: remove and return the CustomerOrder with the given name;
     * TODO: return null if CustomerOrder doesn't exist
     *
     */
    public CustomerOrder remove(String name) throws NoSuchAlgorithmException {

        //System.out.println("remove called, removing:" + name);

        if (name == null) {
            return null;
        }

        int hashCode = getHashCode(name);


        /**

        for (int i = 0; i < table.length; i++) {
            System.out.print("slot: " + i);
            if (table[i] == null) {
                System.out.println("n/a");
            } else {
                System.out.println("not empty");
            }
        }
        System.out.println("");
         **/

        if (get(name) == null) {
            return null;
        }


        for (int i = 0; i < table[hashCode].size(); i++) {
            CustomerOrder curOrder = (CustomerOrder) table[hashCode].get(i);
            if (name.equals(curOrder.getName())) {
                numOrders--;
                return (CustomerOrder) table[hashCode].remove(i);
            }
        }

        
        return null;
    }


    /**
     *
     * TODO: return the number of Customers in the table
     *
     */
    public int size() {
        return numOrders;
    }



    //get the next prime number p >= num
    private int getNextPrime(int num) {
        if (num == 2 || num == 3)
            return num;

        int rem = num % 6;

        switch (rem) {
            case 0:
            case 4:
                num++;
                break;
            case 2:
                num += 3;
                break;
            case 3:
                num += 2;
                break;
        }

        while (!isPrime(num)) {
            if (num % 6 == 5) {
                num += 2;
            } else {
                num += 4;
            }
        }

        return num;
    }

    //determines if a number > 3 is prime
    private boolean isPrime(int num) {
        if (num % 2 == 0) {
            return false;
        }

        int x = 3;

        for (int i = x; i < num; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }

    public ArrayList<CustomerOrder>[] getArray() {
        return this.table;
    }

}
