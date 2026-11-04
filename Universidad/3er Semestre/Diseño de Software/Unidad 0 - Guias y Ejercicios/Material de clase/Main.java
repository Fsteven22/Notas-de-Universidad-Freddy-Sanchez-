package ds2026;

import java.util.ArrayList;
import java.util.List;

interface EmployeeTasks {
	void work();
	void manage();
}

abstract class Employee {
	private String name;
	private String email;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public abstract double calculateBonus();

	public void generatePayslipPdf() {
		System.out.println("Generating PDF payslip for " + name + "...");
	}

	public void sendEmail(String message) {
		System.out.println("Sending email to " + email + ": " + message);
	}
}

class PermanentEmployee extends Employee implements EmployeeTasks {
	@Override
	public double calculateBonus() {
		return 10;
	}

	@Override
	public void work() {
		System.out.println("done");
	}

	@Override
	public void manage() {
		System.out.println("managed");
	}
}

class TemporaryEmployee extends Employee implements EmployeeTasks {
	@Override
	public double calculateBonus() {
		throw new UnsupportedOperationException("Temp earns no bonus");
	}

	@Override
	public void work() {
		System.out.println("done");
	}

	@Override
	public void manage() {
		throw new UnsupportedOperationException("Temp cannot manage others");
	}
}

class MySql {
	public void saveEmployee(Employee employee) {
		System.out.println("Save employee ok...");
	}
}

class ServicePerson {
	public void saveEmployee(Employee employee) {
		MySql mysql = new MySql();
		mysql.saveEmployee(employee);
	}
}

class BonusReport {
	public String describe(Employee employee) {
		if (employee instanceof PermanentEmployee) {
			return employee.getName() + ": bono fijo";
		} else if (employee instanceof TemporaryEmployee) {
			return employee.getName() + ": sin bono";
		}
		return employee.getName() + ": tipo desconocido";
	}
}

class Payroll {
	public double totalBonus(List<Employee> employees) {
		double total = 0;
		for (Employee e : employees) {
			total += e.calculateBonus();
		}
		return total;
	}
}

public class Main {
	public static void main(String[] args) {
		Employee ana = new PermanentEmployee();
		ana.setName("Ana");
		ana.setEmail("ana@empresa.com");

		Employee luis = new TemporaryEmployee();
		luis.setName("Luis");
		luis.setEmail("luis@empresa.com");

		List<Employee> employees = new ArrayList<>();
		employees.add(ana);
		employees.add(luis);

		ServicePerson service = new ServicePerson();
		BonusReport report = new BonusReport();
		for (Employee e : employees) {
			service.saveEmployee(e);
			System.out.println(report.describe(e));
			e.generatePayslipPdf();
			e.sendEmail("Su rol de pagos esta listo");
		}

		Payroll payroll = new Payroll();
		System.out.println("Total bonos: " + payroll.totalBonus(employees));
	}
}