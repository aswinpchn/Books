package com.aswin;

import java.io.*;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) {

    Person p1 = new Person("Aswin", 23);
    Person p2 = new Person("Visaal", 21);

    // Create FileOutputStream, then an ObjectOutputStream and then Write Object into it.
    try(FileOutputStream fs = new FileOutputStream("write.bin"); ObjectOutputStream os = new ObjectOutputStream(fs);) { // The file wont be in readable format.

      os.writeObject(p1);
      os.writeInt(25);

    } catch (IOException e) {
      e.printStackTrace();
    }



    try(FileInputStream fs = new FileInputStream("write.bin"); ObjectInputStream is = new ObjectInputStream(fs);) {

      Person p = (Person)is.readObject(); // Read object from that file and then Typecast it for Person Class type.
      System.out.println(p.toString());

      Integer i = (Integer)is.readInt();
      System.out.println(i);

    } catch (IOException | ClassNotFoundException e) {
      e.printStackTrace();
    }


  }

  /*

    Serialization is a mechanism of converting the state of an object into a byte stream. Deserialization is the reverse process where the byte stream is used to recreate the actual Java object in memory. This mechanism is used to persist the object.

    https://www.udemy.com/course/java-tutorial/learn/lecture/424118#overview
    https://www.geeksforgeeks.org/serialization-in-java/
   */
}
