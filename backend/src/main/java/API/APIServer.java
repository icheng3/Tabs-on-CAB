package API;

import static spark.Spark.after;

import API.Handlers.RemoveFromWatchlistHandler;
import API.Handlers.AddToWatchlistHandler;
import spark.Spark;
//import database.AddToCourseInfo;

public class APIServer {
  public static void main(String[] args) {

    Spark.port(3232);
    after((request, response) -> {
      response.header("Access-Control-Allow-Origin", "*");
      response.header("Access-Control-Allow-Methods", "*");
    });

    // Setting up the handlers for the GET endpoint
    Spark.get("add", new AddToWatchlistHandler());
    Spark.get("remove", new RemoveFromWatchlistHandler());
    Spark.init();
    Spark.awaitInitialization();
    System.out.println("Server started.");
  }

}
