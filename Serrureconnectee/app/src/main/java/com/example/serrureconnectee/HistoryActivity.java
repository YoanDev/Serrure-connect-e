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

import com.example.serrureconnectee.database_classes.EntreesData;
import com.example.serrureconnectee.database_classes.Entrees_db;
import com.example.serrureconnectee.database_classes.UsersData;
import com.example.serrureconnectee.database_classes.Users_db;

import java.util.ArrayList;
import java.util.List;

public class HistoryActivity extends AppCompatActivity {

    ListView listView;
    ArrayList<String> arrayList;
    ArrayAdapter arrayAdapter;

    int[] IMAGES = {R.drawable.ic_baseline_history_24};


    private EntreesData entreesdatasource;
    private UsersData usersdatasource;
    List<Entrees_db> entree;
    List<Users_db> user;
    Users_db u = new Users_db();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);

        usersdatasource = new UsersData(this);
        entreesdatasource = new EntreesData(this);
        entreesdatasource.open();
        usersdatasource.open();
        entree = entreesdatasource.getAllEntrees();
        user = usersdatasource.getAllUsers();

        listView = (ListView) findViewById(R.id.history_listview);

        CustomAdapter customAdapter = new CustomAdapter();

        listView.setAdapter(customAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            }
        });
    }

    class CustomAdapter extends BaseAdapter {

        @Override
        public int getCount() {
            return entree.size();
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
            convertView = getLayoutInflater().inflate(R.layout.customlayout,null);

            ImageView imageView = (ImageView) convertView.findViewById(R.id.history_list_imageView);
            TextView textView_nom = (TextView) convertView.findViewById(R.id.history_list_textView_username);
            TextView textView_date = (TextView) convertView.findViewById(R.id.history_list_textView_date);

            for(int i=0; i<entree.size();i++) {
                u = u.recuperer_user((ArrayList<Users_db>) user,entree.get(i).getId_user());
                imageView.setImageResource(IMAGES[0]);
                textView_nom.setText(u.getName());
                textView_date.setText(entree.get(i).getDate());
            }

            return convertView;
        }
    }
}