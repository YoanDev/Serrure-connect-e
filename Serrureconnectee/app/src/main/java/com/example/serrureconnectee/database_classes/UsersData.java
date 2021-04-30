package com.example.serrureconnectee.database_classes;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;
import java.util.List;

public class UsersData {

    private SQLiteDatabase database;
    private MysqLiteHelper dbHelper;
    private String[] allColumns = { MysqLiteHelper.COLUMN_USER_ID,
            MysqLiteHelper.COLUMN_USER_NAME};

    public UsersData(Context context) {
        dbHelper = new MysqLiteHelper(context);
    }


    public void open() throws SQLException {
        database = dbHelper.getWritableDatabase();
    }

    public void close() {
        dbHelper.close();
    }

    public Users_db createUser(String name) {
        ContentValues values = new ContentValues();
        values.put(MysqLiteHelper.COLUMN_USER_NAME, name);
        values.put(MysqLiteHelper.COLUMN_USER_PICTURE_PATH, "Test_chemin");
        values.put(MysqLiteHelper.COLUMN_USER_PASSWORD, "admin");
        long insertId = database.insert(MysqLiteHelper.TABLE_USERS, null,
                values);
        Cursor cursor = database.query(MysqLiteHelper.TABLE_USERS,
                allColumns, MysqLiteHelper.COLUMN_USER_ID + " = " + insertId, null,
                null, null, null);
        cursor.moveToFirst();
        Users_db newComment = cursorToUser(cursor);
        cursor.close();
        return newComment;
    }

    public void deleteUsers(Users_db user) {
        long id = user.getId();
        System.out.println("Comment deleted with id: " + id);
        database.delete(MysqLiteHelper.TABLE_USERS, MysqLiteHelper.COLUMN_USER_ID
                + " = " + id, null);
    }

    public List<Users_db> getAllUsers() {
        List<Users_db> users_list = new ArrayList<Users_db>();

        Cursor cursor = database.query(MysqLiteHelper.TABLE_USERS,
                allColumns, null, null, null, null, null);

        cursor.moveToFirst();
        while (!cursor.isAfterLast()) {
            Users_db user = cursorToUser(cursor);
            users_list.add(user);
            cursor.moveToNext();
        }
        // assurez-vous de la fermeture du curseur
        cursor.close();
        return users_list;
    }

    private Users_db cursorToUser(Cursor cursor) {
        Users_db user = new Users_db();
        user.setId(cursor.getLong(0));
        user.setName(cursor.getString(1));
        return user;
    }

}
