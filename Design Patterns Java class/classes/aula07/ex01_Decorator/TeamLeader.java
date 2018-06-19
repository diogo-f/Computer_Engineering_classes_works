/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula07.ex01_Decorator;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 *
 * @author diogo
 */
public class TeamLeader extends EmployeeDecorator {

    private Date dataInicio;
    private Date dataFim;
    private DateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy - HH:mm:ss");

    public TeamLeader(EmployeeInterface empInt) {
        super(empInt);
        this.dataInicio = new Date();
        this.dataFim = null;
    }

    public void plan() {
        System.out.println("Planeio");
    }

    @Override
    public void works() {
        super.empInt.works();
        this.plan();
    }

    @Override
    public void endDate(Date d) {
        this.dataFim = d;
    }

    @Override
    public String toString() {
        if (dataFim == null) {
            return "\nTeamLeader\n - dataInicio: " + dateFormat.format(dataInicio) + ", dataFim: sem data\n" + super.toString();
        } else {
            return "\nTeamLeader\n - dataInicio: " + dateFormat.format(dataInicio) + ", dataFim: " + dateFormat.format(dataFim) + "\n" + super.toString();
        }
    }

}
