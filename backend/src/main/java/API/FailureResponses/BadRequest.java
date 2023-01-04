package API.FailureResponses;

import com.squareup.moshi.Moshi;

public class BadRequest {

  /**
   * Response object to send if the request was missing a needed field, or the field was
   * ill-formed
   */
  public record BadRequestFailureResponse(String result) {
    public BadRequestFailureResponse() { this("error_bad_request"); }

    /**
     * @return this response, serialized as Json
     */
    public String serialize() {
      Moshi moshi = new Moshi.Builder().build();
      return moshi.adapter(BadRequestFailureResponse.class).toJson(this);
    }
  }

}
