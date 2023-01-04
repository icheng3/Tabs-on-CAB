package FirebaseStuff;

import java.io.FileInputStream;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.FirebaseApp;
import com.google.firebase.database.*;
import com.google.auth.oauth2.GoogleCredentials;
import java.io.IOException;

public class FirebaseHandler {
  FileInputStream serviceAccount =
      new FileInputStream("/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/java/FirebaseStuff/sample_firebase_data.java");

  FirebaseOptions options = FirebaseOptions.builder()
      .setCredentials(GoogleCredentials.fromStream(serviceAccount))
      .setDatabaseUrl("https://tabsoncab-default-rtdb.firebaseio.com")
      .build();
  FirebaseApp.initializeApp(options);
  public FirebaseHandler() throws IOException {
  }

  // As an admin, the app has access to read and write all data, regardless of Security Rules
  DatabaseReference ref = FirebaseDatabase.getInstance()
      .getReference("restricted_access/secret_document");
ref.addListenerForSingleValueEvent(new ValueEventListener() {
    @Override
    public void onDataChange(DataSnapshot dataSnapshot) {
      Object document = dataSnapshot.getValue();
      System.out.println(document);
    }

    @Override
    public void onCancelled(DatabaseError error) {
    }
  });

}
