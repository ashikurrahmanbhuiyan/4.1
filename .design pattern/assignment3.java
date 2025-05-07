abstract class Approver{
    protected Approver nextApprover;

    public void setNextApprover(Approver nextApprover){
        this.nextApprover = nextApprover;
    }
    
    public abstract void approveWithdrawl(double amount);
}


class Cashier extends Approver{
    @Override
    public void approveWithdrawl(double amount){
        if(amount < 10000){
            System.out.println("cashier approved");
        }
        else if(nextApprover != null){
            nextApprover.approveWithdrawl(amount);
        }
    }
}


class SeniorOfficer extends Approver {
    @Override
    public void approveWithdrawl(double amount) {
        if (amount <= 1000000) {
            System.out.println("Senior Officer approved withdrawal of Tk. " + amount);
        } else if (nextApprover != null) {
            nextApprover.approveWithdrawl(amount);
        }
    }
}


class Manager extends Approver{
    @Override
    public void approveWithdrawl(double amount){
        System.out.println("manager approved");
    }
}

public class assignment3 {
    public static void main(String[] args) {
        Approver cashier = new Cashier();
        Approver seniorOfficer = new SeniorOfficer();
        Approver manager = new Manager();

        cashier.setNextApprover(seniorOfficer);
        seniorOfficer.setNextApprover(manager);

        System.out.println("---- Test Cases ----");
        cashier.approveWithdrawl(5000); // Cashier handles
        cashier.approveWithdrawl(200000); // Senior Officer handles
        cashier.approveWithdrawl(2000000); // Manager handles
    }
}
