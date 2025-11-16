// NOTE: This script is ONLY for uploading comments ONCE.
// Run it on your computer with:  node upload.js

const admin = require("firebase-admin");
const fs = require("fs");

// ---------------------------------------------------------
// IMPORTANT:
// 1. Place serviceAccountKey.json in this folder
// 2. Place comments.json in this folder
// 3. Replace YOUR_PROJECT_ID below
// 4. Use the SAME appId as your website (must match)
// ---------------------------------------------------------

const serviceAccount = require("./serviceAccountKey.json");
const comments = JSON.parse(fs.readFileSync("./comments.json", "utf8"));

const appId = "default-labeler-app"; // MUST MATCH your HTML file

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com" // Replace with your actual URL
});

const db = admin.firestore();

async function uploadComments() {
  console.log(`Starting upload for ${comments.length} comments...`);

  const batch = db.batch();

  comments.forEach((comment) => {
    const commentData = {
      text: comment.Comments,       // Make sure your JSON has "Comments"
      originalLabel: comment.Class, // Store original class for reference
      isLabeled: false,
      label: null,
      labeledBy: null,
      labeledAt: null,
      labeledByEmail: null
    };

    // The path MUST match the front-end exactly
    const docRef = db
      .collection("artifacts")
      .doc(appId)
      .collection("public")
      .doc("data")
      .collection("comments")
      .doc(); // auto-ID

    batch.set(docRef, commentData);
  });

  await batch.commit();
  console.log("Upload complete!");
}

uploadComments().catch((err) => {
  console.error("Upload failed:", err);
});
