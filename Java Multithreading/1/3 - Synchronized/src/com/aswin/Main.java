package com.aswin;

public class Main {

  int count = 0;

  public static void main(String[] args) {

    Main app = new Main();

    //app.naive();
    //app.withJoin();
    app.withJoinAndSynchronized();
  }

  void incrementCount() {
    count++;
  }

  // This method restricts that only one thread can access the method at any point of time.
  public synchronized void incrementCountSynchronized() {
    count++;
  }

  public void naive() {
    Thread t1 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCount();
        }
      }
    };

    Thread t2 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCount();
        }
      }
    };

    t1.start();
    t2.start();

    System.out.println("Count is: " + count); // In this naive function, with incrementCount, the count wont be 20000 because, t1 thread will start its works, t2 will start its work and then this print line is executed before their completion.
  }

  public void withJoin() {
    Thread t1 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCount();
        }
      }
    };

    Thread t2 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCount();
        }
      }
    };

    t1.start();
    t2.start();

    // java.lang.Thread class provides the join() method which allows one thread to wait until another thread completes its execution.
    // Main thread will wait till t1 and t2 thread stops executing.
    try {
      t1.join();
      t2.join();
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    System.out.println("Count is: " + count); // Still this wont work because, t1 and t2 parallelly call incrementCount method which can cause inconsistency.
    // We have to use synchronised keyword for increment count method to keep things consistent.
  }

  public void withJoinAndSynchronized() {
    Thread t1 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCountSynchronized();
        }
      }
    };

    Thread t2 = new Thread() {
      public void run() {
        for(int i = 0; i < 10000; i++) {
          incrementCountSynchronized();
        }
      }
    };

    t1.start();
    t2.start();

    try {
      t1.join();
      t2.join();
    } catch (InterruptedException e) {
      e.printStackTrace();
    }

    System.out.println("Count is: " + count); // This will properly work as Join feature is used and synchronized increment is used.
  }

  /*

    This tutorial explains us about the use of "synchronized" method that should be used when various threads access the same resource.
    https://www.udemy.com/course/java-multithreading/learn/lecture/108950#overview

    Note: This tutorial also accidentally explains .join() method, (java.lang.Thread class provides the join() method which allows one thread to wait until another thread completes its execution.)

   */
}
