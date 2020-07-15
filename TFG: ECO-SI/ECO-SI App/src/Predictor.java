

import org.tensorflow.*;
import java.io.IOException;
import java.util.Iterator;

public class Predictor {
	
	public boolean pred;
	public float prob[][];
	
	public Predictor() {
		pred=false;
		prob= new float[1][2];
	}
	
	public boolean getPred() {
		return pred;
	}

	public double getProb() {
		return (double)prob[0][0];
	}
	
	public void prediccion(Tensor imagen, int red)throws IOException {
		try( SavedModelBundle b = SavedModelBundle.load("./Redes/"+red,"serve")){
			
			Session s = b.session();
			
			Tensor probConv = Tensor.create(1.0f);
			Tensor probOc = Tensor.create(1.0f);
			
			Tensor res = s.runner().feed("Placeholder", imagen).feed("Placeholder_2", probConv).feed("Placeholder_3", probOc)
					.fetch("Softmax").run().get(0);
			res.copyTo(prob);

			if(prob[0][0]>prob[0][1])
				pred=true;
		}
		
	}

	
}
