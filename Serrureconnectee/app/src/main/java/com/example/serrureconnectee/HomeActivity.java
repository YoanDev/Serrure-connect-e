package com.example.serrureconnectee;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class HomeActivity extends AppCompatActivity implements View.OnClickListener {

    private Button bt_home;
    private Button bt_history;
    private Button bt_users;
    private Button bt_now;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        bt_home = (Button) findViewById(R.id.bt_home_home);
        bt_history = (Button) findViewById(R.id.bt_home_history);
        bt_users = (Button) findViewById(R.id.bt_home_users);
        bt_now = (Button) findViewById(R.id.bt_home_now);

        bt_home.setOnClickListener(this);
        bt_history.setOnClickListener(this);
        bt_users.setOnClickListener(this);
        bt_now.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.bt_home_home:
                break;

            case R.id.bt_home_history:
                Intent intent_history=new Intent(this,HistoryActivity.class);
                startActivity(intent_history);
                break;

            case R.id.bt_home_users:
                Intent intent_users=new Intent(this,UsersActivity.class);
                startActivity(intent_users);
                break;

            case R.id.bt_home_now:
                Intent intent_now=new Intent(this,AutorisationActivity.class);
                startActivity(intent_now);
                break;
        }
    }
}