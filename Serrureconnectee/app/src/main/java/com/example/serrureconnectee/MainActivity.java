package com.example.serrureconnectee;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.serrureconnectee.database_classes.EntreesData;
import com.example.serrureconnectee.database_classes.Entrees_db;
import com.example.serrureconnectee.database_classes.UsersData;
import com.example.serrureconnectee.database_classes.Users_db;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private TextView email;
    private TextView mot_de_passe;

    private Button authentification;
    private Button enregistrement;

    private UsersData usersdatasource;
    private EntreesData entreesdatasource;
    List<Users_db> user;
    List<Entrees_db> entree;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        send sendcode = new send();
        sendcode.execute();

        usersdatasource = new UsersData(this);
        entreesdatasource = new EntreesData(this);
        usersdatasource.open();
        entreesdatasource.open();

        Entrees_db end = new Entrees_db(1, "21/04/2021 11:25:50");
        Entrees_db end1 = new Entrees_db(1, "22/04/2021 11:25:50");
        Entrees_db end2 = new Entrees_db(2, "22/04/2021 11:25:50");
        Entrees_db end3 = new Entrees_db(1, "23/04/2021 11:25:50");
        Entrees_db end4 = new Entrees_db(2, "24/04/2021 11:25:50");
        Entrees_db end5 = new Entrees_db(1, "24/04/2021 11:25:50");
        Entrees_db end6 = new Entrees_db(1, "24/04/2021 11:25:50");
        Entrees_db end7 = new Entrees_db(2, "25/04/2021 11:25:50");
        Entrees_db end8 = new Entrees_db(2, "25/04/2021 11:25:50");
        entreesdatasource.createEntree(end1);
        entreesdatasource.createEntree(end2);
        entreesdatasource.createEntree(end3);
        entreesdatasource.createEntree(end4);
        entreesdatasource.createEntree(end5);
        entreesdatasource.createEntree(end6);
        entreesdatasource.createEntree(end7);
        entreesdatasource.createEntree(end8);
        usersdatasource.createUser("Robert Robert");
        usersdatasource.createUser("Valérie Valérie");

        email = (TextView) findViewById(R.id.auth_email_text_view);
        mot_de_passe = (TextView) findViewById(R.id.auth_mdp_text_view);
        authentification = (Button) findViewById(R.id.auth_connexion_button);
        enregistrement = (Button) findViewById(R.id.auth_enregistrement_button);

        authentification.setOnClickListener(this);
        enregistrement.setOnClickListener(this);
    }


    public void Go(View v) {
        //on creer une nouvelle intent on definit la class de depart ici this et la class d'arrivé ici SecondActivite
        Intent intent=new Intent(this,HomeActivity.class);
        //on lance l'intent, cela a pour effet de stoper l'activité courante et lancer une autre activite ici SecondActivite
        startActivity(intent);


    }

    @Override
    public void onClick(View v) {
        switch (v.getId()){
            case R.id.auth_connexion_button:
                this.Go(v);
                break;

            case R.id.auth_enregistrement_button:
                Toast.makeText(MainActivity.this, "Fonctionnalité à venir", Toast.LENGTH_SHORT).show();
                break;

        }
    }

    class send extends AsyncTask<Void,Void,Void> {
        Socket s;
        PrintWriter pw;
        @Override
        protected Void doInBackground(Void...params){
            try {
                s = new Socket("192.168.43.55",1224);
                pw = new PrintWriter(s.getOutputStream());
                pw.write("message");

                //Message retour
                InputStream is = s.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                String retour = br.readLine();
                System.out.println("Message received from the server : " +retour);


                pw.flush();
                pw.close();
                s.close();
            } catch (UnknownHostException e) {
                System.out.println("Fail");
                e.printStackTrace();
            } catch (IOException e) {
                System.out.println("Fail");
                e.printStackTrace();
            }
            return null;
        }
    }


}