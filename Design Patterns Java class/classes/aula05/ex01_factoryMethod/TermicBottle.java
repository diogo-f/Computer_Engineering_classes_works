/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula05.ex01_factoryMethod;

/**
 *
 * @author diogo
 */
public class TermicBottle extends Container {

    @Override
    public String toString() {
        return "\nTermicBottle para: " + getCommodity();
    }

}
