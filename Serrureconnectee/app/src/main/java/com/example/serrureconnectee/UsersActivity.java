package com.example.serrureconnectee;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.serrureconnectee.database_classes.UsersData;
import com.example.serrureconnectee.database_classes.Users_db;

import java.util.ArrayList;
import java.util.List;

public class UsersActivity extends AppCompatActivity {

    ListView listView;
    ArrayList<String> arrayList;
    ArrayAdapter arrayAdapter;

    private UsersData usersdatasource;
    List<Users_db> user;

    int[] IMAGES = {R.drawable.ic_baseline_person_24};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_users);

        listView = (ListView) findViewById(R.id.users_listview);

        usersdatasource = new UsersData(this);
        usersdatasource.open();
        user = usersdatasource.getAllUsers();

        UsersActivity.CustomUserAdapter customAdapter = new UsersActivity.CustomUserAdapter();

        listView.setAdapter(customAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

            }
        });
    }

    class CustomUserAdapter extends BaseAdapter {

        @Override
        public int getCount() {
            return user.size();
        }

        @Override
        public Object getItem(int position) {
            return null;
        }

        @Override
        public long getItemId(int position) {
            return 0;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            convertView = getLayoutInflater().inflate(R.layout.usercustomlayout,null);

            ImageView imageView = (ImageView) convertView.findViewById(R.id.user_list_imageView);
            TextView textView_nom = (TextView) convertView.findViewById(R.id.user_list_textView_username);

            for(int i=0; i<user.size();i++){
                imageView.setImageResource(IMAGES[0]);
                textView_nom.setText(user.get(i).getName());
            }


            return convertView;
        }
    }
}