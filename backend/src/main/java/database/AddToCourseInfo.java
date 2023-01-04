package database;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Handler;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class AddToCourseInfo {

  private String filepath = "/Users/yuliannacruz-trinidad/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/python/Scraper/cabscraper/spiders/data.json";

  public AddToCourseInfo() {
    adding();
  }

  public void adding(){
    try{
      //Here, we parse the JSON file and create an object so that we can iterate through it
      JSONParser parser = new JSONParser();
      JSONObject obj = (JSONObject)parser.parse(new FileReader(filepath));

      //Here, we are connecting to the SQL database
      Class.forName("org.sqlite.JDBC");
      String urlToDB = "jdbc:sqlite:" + "/Users/yuliannacruz-trinidad/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/java/database/CabData.db";
      Connection conn = DriverManager.getConnection(urlToDB);
      Statement stat = conn.createStatement();
      stat.executeUpdate("PRAGMA foreign_keys=ON;");

      //Here, we iterate through the object and put the data into the database
      JSONArray array = (JSONArray) obj.get("code" + "name" + "instructor" + "time"); //get the data that belongs to this i'm guessing also in the json file, there isn't any sections???
      for(Object object : array){
        JSONObject record = (JSONObject) object;
        String course_code = (String) record.get("course_code");
        String course_name = (String) record.get("course_name");
        String section = (String) record.get("section");
        String time = (String) record.get("time");
        String instructor = (String) record.get("instructor");
        PreparedStatement prep = conn.prepareStatement("INSERT INTO course_info(dept_code, course_code, course_name,"
            + " section, time, instructor) VALUE (?, ?, ?, ?, ?);");
        prep.setString(1,course_code);
        prep.setString(2, course_name);
        prep.setString(3, section);
        prep.setString(4, time);
        prep.setString(5, instructor);
        prep.executeUpdate();
      }

      //while

    } catch (SQLException | ClassNotFoundException | IOException | ParseException e) {
      System.out.println("Error connecting to SQLite database");
      e.printStackTrace();
    }
    System.out.println("created table");
  }
}
