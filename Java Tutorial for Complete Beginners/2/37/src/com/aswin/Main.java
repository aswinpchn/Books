package com.aswin;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws FileNotFoundException {

    String fileName = "text"; // You can either give full path or if file is in same folder you can give end path only. "/Users/aswinprasad/Documents/Java/Java Tutorial for Complete Beginners/2/37/text"
    File textFile = new File(fileName);

    Scanner in = new Scanner(textFile);

    while(in.hasNextLine()) {
      System.out.println(in.nextLine());
    }

    in.close();
  }

}
