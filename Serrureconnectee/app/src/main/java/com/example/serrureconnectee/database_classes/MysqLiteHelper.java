package com.example.serrureconnectee.database_classes;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

import androidx.annotation.Nullable;

public class MysqLiteHelper extends SQLiteOpenHelper {

    public static final String TABLE_USERS = "users";
    public static final String TABLE_ENTREES = "entrees";

    //Données  de la table user
    public static final String COLUMN_USER_ID = "id_user";
    public static final String COLUMN_USER_NAME = "user_name";
    public static final String COLUMN_USER_PASSWORD = "user_password";
    public static final String COLUMN_USER_PICTURE_PATH = "user_chemin_photo";

    //Données de la table entrées
    public static final String COLUMN_ENTREES_ID = "id_entree";
    public static final String COLUMN_ENTREES_USER_ID = "id_user";
    public static final String COLUMN_ENTREES_DATE = "date";

    private static final String DATABASE_NAME = "serrure_connectee.db";
    private static final int DATABASE_VERSION = 1;

    private static final String DATABASE_CREATE = "create table "
            + TABLE_USERS + "(" + COLUMN_USER_ID
            + " integer primary key autoincrement, " + COLUMN_USER_NAME
            + " text not null ,"+ COLUMN_USER_PICTURE_PATH +" text not null ,"+ COLUMN_USER_PASSWORD + " text not null );";

    private static final String DATABASE_CREATE_TABLE_ENTREES = "create table "
            + TABLE_ENTREES + "(" + COLUMN_ENTREES_ID
            + " integer primary key autoincrement, " + COLUMN_ENTREES_USER_ID
            + " text not null, "+ COLUMN_ENTREES_DATE +" text not null);";

    public MysqLiteHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(DATABASE_CREATE);
        db.execSQL(DATABASE_CREATE_TABLE_ENTREES);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        Log.w("Mysq",
                "Upgrading database from version " + oldVersion + " to "
                        + newVersion + ", which will destroy all old data");
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        onCreate(db);
    }
}
