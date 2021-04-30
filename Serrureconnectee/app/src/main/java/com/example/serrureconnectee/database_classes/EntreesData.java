package com.example.serrureconnectee.database_classes;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;
import java.util.List;

public class EntreesData {

    private SQLiteDatabase database;
    private MysqLiteHelper dbHelper;
    private String[] allColumns = { MysqLiteHelper.COLUMN_ENTREES_ID, MysqLiteHelper.COLUMN_ENTREES_USER_ID, MysqLiteHelper.COLUMN_ENTREES_DATE};

    public EntreesData(Context context) {

        dbHelper = new MysqLiteHelper(context);
    }

    public void open() throws SQLException {
        database = dbHelper.getWritableDatabase();
    }

    public void close() {
        dbHelper.close();
    }

    public Entrees_db createEntree(Entrees_db entree) {
        ContentValues values = new ContentValues();
        values.put(MysqLiteHelper.COLUMN_ENTREES_USER_ID, entree.getId_user());
        values.put(MysqLiteHelper.COLUMN_ENTREES_DATE, entree.getDate());
        long insertId = database.insert(MysqLiteHelper.TABLE_ENTREES, null,
                values);
        Cursor cursor = database.query(MysqLiteHelper.TABLE_ENTREES,
                allColumns, MysqLiteHelper.COLUMN_ENTREES_ID + " = " + insertId, null,
                null, null, null);
        cursor.moveToFirst();
        Entrees_db newEntree = cursorToEntree(cursor);
        cursor.close();
        return newEntree;
    }

    public List<Entrees_db> getAllEntrees() {
        List<Entrees_db> entrees_list = new ArrayList<Entrees_db>();

        Cursor cursor = database.query(MysqLiteHelper.TABLE_ENTREES,
                allColumns, null, null, null, null, null);

        cursor.moveToFirst();
        while (!cursor.isAfterLast()) {
            Entrees_db entree = cursorToEntree(cursor);
            entrees_list.add(entree);
            cursor.moveToNext();
        }
        // assurez-vous de la fermeture du curseur
        cursor.close();
        return entrees_list;
    }

    private Entrees_db cursorToEntree(Cursor cursor) {
        Entrees_db entree = new Entrees_db();
        entree.setId(cursor.getLong(0));
        entree.setId_user(cursor.getLong(1));
        entree.setDate(cursor.getString(2));
        return entree;
    }

}
