package com.example.serrureconnectee.database_classes;

public class Entrees_db {
    private long id;
    private long id_user;
    private String date;

    public Entrees_db() {
    }

    public Entrees_db(long id_user, String date) {
        this.id_user = id_user;
        this.date = date;
    }


    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public long getId_user() {
        return id_user;
    }

    public void setId_user(long id_user) {
        this.id_user = id_user;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    @Override
    public String toString() {
        return "Entrees{" +
                "id=" + id +
                ", id_user=" + id_user +
                ", date='" + date + '\'' +
                '}';
    }
}
