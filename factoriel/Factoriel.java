package factoriel;

public class Factoriel {
	
	/**
	 *on a porté notre retour de fonction est de type double(8bits) 
	 *avec Double on aura plus de resultat que Int (4bits)
	 */
	public Double factorielRecursive(Double nombre) {
		if (nombre == 0) {
			nombre = 1.; 
		}
		else {
			nombre = nombre * factorielRecursive(nombre - 1);
		}
		return nombre ;
	}
	
	// fonction avec boucle 
	public Double factorielBoucle(Double nombre) {
		Double resultat = 1.; 
		if (nombre != 0.){
			for (int i = 1; i<=nombre; i++) {
				resultat = resultat * i	;
			}	
		}		
		return resultat ;
	}
	
	
	public static void main(String[] args) {
		Factoriel fact = new Factoriel();
		System.out.println("resultat avec Recursive = "+fact.factorielRecursive(17.));
		// le resultat sera Infinity parce que la valeur de 171! depasse type Double
		System.out.println("resultat avec Boucle = "+fact.factorielBoucle(171.));
	}
}

/**
 * Rapidement le calcul du factoriel d'un nombre donné peut retourner
 * des resultats qui ne seront pas lisible par l'homme 
 * Pour un type Double (8 bits ) peut retourner un resultat pour une valeur 
 * donné inferieur ou egale a 170
 * 
 */
