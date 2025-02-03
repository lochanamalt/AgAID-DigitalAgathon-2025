package com.example.agaid_crop_residue;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class DisplayImageActivity extends AppCompatActivity {

    private ImageView imageView;
    private Button clearButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_image);

        imageView = findViewById(R.id.imageView);
        clearButton = findViewById(R.id.btnClear);

        // Get image URI from Intent
        String imageUriString = getIntent().getStringExtra("imageUri");
        if (imageUriString != null) {
            Uri imageUri = Uri.parse(imageUriString);
            imageView.setImageURI(imageUri);
        } else {
            Toast.makeText(this, "Error loading image", Toast.LENGTH_SHORT).show();
            finish();
        }

        // Clear image and go back to MainActivity
        clearButton.setOnClickListener(v -> {
            imageView.setImageDrawable(null);
            startActivity(new Intent(DisplayImageActivity.this, MainActivity.class));
            finish();
        });
    }
}
