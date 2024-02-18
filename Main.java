import java.util.Scanner;

class network {
    private int numLayers;
    private int[] numNodes;
    private int[][][] weights;

    public network(int numLayers, int[] numNodes) {
        this.numLayers = numLayers;
        this.numNodes = numNodes;
        this.weights = new int[numLayers - 1][][];
        for (int i = 0; i < numLayers - 1; i++) {
            weights[i] = new int[numNodes[i]][numNodes[i + 1]];
        }
    }

    public void setWeights(Scanner scanner) {
        for (int i = 0; i < numLayers - 1; i++) {
            System.out.println("Enter weights for layer " + (i + 1) + " to layer " + (i + 2) + ":");
            for (int j = 0; j < numNodes[i]; j++) {
                for (int k = 0; k < numNodes[i + 1]; k++) {
                    System.out.print("Weight from node " + (j + 1) + " to node " + (k + 1) + ": ");
                    weights[i][j][k] = scanner.nextInt();
                }
            }
        }
    }

    public int getWeight(int layer, int fromNode, int toNode) {
        return weights[layer - 1][fromNode - 1][toNode - 1];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the num of layers: ");
        int numLayers = scanner.nextInt();

        int[] numNodes = new int[numLayers];
        for (int i = 0; i < numLayers; i++) {
            System.out.print("Enter the num of nodes in layer " + (i + 1) + ": ");
            numNodes[i] = scanner.nextInt();
        }

        network network = new network(numLayers, numNodes);
        network.setWeights(scanner);

        System.out.print("Enter the layer num: ");
        int layer = scanner.nextInt();

        System.out.print("Enter the 'from' node num: ");
        int fromNode = scanner.nextInt();

        System.out.print("Enter the 'to' node num: ");
        int toNode = scanner.nextInt();

        int weight = network.getWeight(layer, fromNode, toNode);
        System.out.println("Weight from node " + fromNode + " to node " + toNode + " in layer " + layer + ": " + weight);
    }
}
