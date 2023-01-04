package API.Handlers;

import API.FailureResponses.BadRequest.BadRequestFailureResponse;
import com.squareup.moshi.JsonAdapter;
import com.squareup.moshi.Moshi;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;
import spark.QueryParamsMap;
import spark.Request;
import spark.Response;
import spark.Route;

public class RemoveFromWatchlistHandler implements Route {

  @Override
  public Object handle(Request request, Response response) throws Exception {
    QueryParamsMap qm = request.queryMap();
    if (qm.value("course") == null) {
      return new BadRequestFailureResponse().serialize();
    }
    String watchlist_course = qm.value("course");

    Class.forName("org.sqlite.JDBC");
    String urlToDB = "jdbc:sqlite:" + "/Users/yuliannacruz-trinidad/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/java/database/CabData.db";
    Connection conn = DriverManager.getConnection(urlToDB);
    Statement stat = conn.createStatement();
    stat.executeUpdate("PRAGMA foreign_keys=ON;");

    PreparedStatement prep;
    prep = conn.prepareStatement("CREATE TABLE user_info("
        + "email TEXT PRIMARY KEY,"
        + "name TEXT,");
    prep.executeUpdate();

    prep = conn.prepareStatement(
        "INSERT INTO user_info VALUES (?, ?, ?, ?);");
    prep.setInt(1, 32);
    prep.setString(2, "Software Engineering");
    prep.setString(3, "Fall21");
    prep.setString(4, "tn");
    prep.addBatch();

    prep.setInt(1, 33);
    prep.setString(2, "Computer Systems");
    prep.setString(3, "Fall21");
    prep.setString(4, "twd");
    prep.addBatch();

    prep.setInt(1, 167);
    prep.setString(2, "Operating Systems");
    prep.setString(3, "Spring22");
    prep.setString(4, "twd");
    prep.addBatch();

    prep.executeBatch();

    prep = conn.prepareStatement("CREATE TABLE course_info("
        + "dept TEXT,"
        + "name TEXT,"
        + "code TEXT,"
        + "section TEXT,"
        + "time TEXT,");

    prep = conn.prepareStatement(
        "INSERT INTO course_info VALUES (?, ?, ?, ?);");

    return null;
  }

  public String WatchlistSuccessResponse(String deptCode) {
    HashMap<String, Object> successResponse = new HashMap<String, Object>();
    successResponse.put("result", "successful");
    successResponse.put("DeptCode", deptCode);
    Moshi moshi = new Moshi.Builder().build();
    JsonAdapter<Map> jAdapter = moshi.adapter(Map.class);
    return jAdapter.toJson(successResponse);
  }
}
