package com.aswin;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    // Here we are throwing the expception there and making sure we are handling that using Try catch in the main function.
    try {
      openFile();
    }catch (FileNotFoundException e) {
      System.out.println("File not found exception");
    }

    // When you are catching multiple exception, catch the more specific exceptions first and then less specific exceptions after that.

    System.out.println("Code won't be abruptly stopped as we use try catch.");
  }

  public static void openFile() throws FileNotFoundException {
    String fileName = "texty";
    File textFile = new File(fileName);

    Scanner in = new Scanner(textFile);

    while(in.hasNextLine()) {
      System.out.println(in.nextLine());
    }

    in.close();
  }

  /*

    The thing is that you can handle an exception in two ways,
      1. Throws. - The problem with throws is that, it can abruptly stop the program, which is not a good pattern.
      2. Try catch.

   */

}
