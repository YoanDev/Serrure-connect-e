package com.example.serrureconnectee;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class AutorisationActivity extends AppCompatActivity implements View.OnClickListener {

    private ImageView image_camera;
    private Button auto_accepter;
    private Button auto_refuser;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_autorisation);

        auto_accepter = findViewById(R.id.auto_accepter_boutton);
        auto_refuser = findViewById(R.id.auto_refuser_boutton);
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.auto_accepter_boutton:


                break;

            case R.id.auto_refuser_boutton:


                break;
        }
    }
}