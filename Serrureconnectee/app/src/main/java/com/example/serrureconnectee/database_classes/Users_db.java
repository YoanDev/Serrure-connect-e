package com.example.serrureconnectee.database_classes;

import java.util.ArrayList;

public class Users_db {
    private long id;
    private String name;
    private int chemin_photo;

    public Users_db() {
    }

    public Users_db(long id, String name) {
        this.id = id;
        this.name = name;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getChemin_photo() {
        return chemin_photo;
    }

    public void setChemin_photo(int chemin_photo) {
        this.chemin_photo = chemin_photo;
    }

    public Users_db recuperer_user(ArrayList<Users_db> user_list, long id_user){
        Users_db u = new Users_db();

        for(int i=0; i<user_list.size();i++){
            if(user_list.get(i).getId() == id_user){
                u = user_list.get(i);
            }
        }

        return u;
    }

    @Override
    public String toString() {
        return "Users_db{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}
