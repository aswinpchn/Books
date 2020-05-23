package com.aswin;

import java.io.*;

public class Main {

  public static void main(String[] args) {
    File file = new File("file.txt");

    try(BufferedWriter bw = new BufferedWriter(new FileWriter(file))) {
      bw.write("First line");
      bw.newLine();
      bw.write("Second line");
    } catch (IOException e) {
      System.out.println("Cannot write file" + file.toString());
    }
  }

  /*

    Initially, you have to so much setup code to do tasks like file reading and all. It was very verbose.
    That why try catch with resources feature came from Java 7. (https://www.baeldung.com/java-try-with-resources)

    The thing is that we can avoid the finally block and all. (As closing and all is take care by try itself in this method).
   */
}
