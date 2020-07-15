

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;

import javax.imageio.ImageIO;

import org.tensorflow.*;


public class Main {
	
	private static Tensor constructAndExecuteGraphToNormalizeImage(byte[] imageBytes) {
		  
		    try (Graph g = new Graph()) {
		      GraphBuilder b = new GraphBuilder(g);
		      
		      // - The colors, represented as R, G, B in 1-byte each were converted to
		      //   float using (value - Mean)/Scale.
		      final int H = 800; //Alto
		      final int W = 400; //Ancho
		      final float mean = 117f;
		      final float scale = 1f;

		      // Since the graph is being constructed once per execution here, we can use a constant for the
		      // input image. If the graph were to be re-used for multiple input images, a placeholder would
		      // have been more appropriate.
		      final Output input = b.constant("input", imageBytes);
		      final Output output =
		          b.div(
		              b.sub(
		                  b.resizeBilinear(
		                      b.expandDims(
		                          b.cast(b.decodeJpeg(input, 3), DataType.FLOAT),
		                          b.constant("make_batch", 0)),
		                      b.constant("size", new int[] {H, W})),
		                  b.constant("mean", mean)),
		              b.constant("scale", scale));
		      try (Session s = new Session(g)) {
		        return s.runner().fetch(output.op().name()).run().get(0);
		      }
		    }
		  }
	public String idObjetos (boolean p1, boolean p2, boolean p3, boolean p4, boolean p5 ) {
		String prediccion="";
		
		 if (p1 && p2 && p3 && p4 && p5)
		 	prediccion="Lata, bolsa, colilla, brick y plastico"; 
		 else if (p2 && p3 && p4 && p5)
			prediccion="Bolsa, colilla, brick y plastico"; 
		 else if (p1 && p2 && p3 && p5)
			prediccion="Lata, colilla, brick y plastico";
		 else if (p1 && p4 && p3 && p2)
	        prediccion="Lata, bolsa, brick y plastico";
		 else if (p1 && p4 && p5 && p2)
	        prediccion="Lata, bolsa,colilla y plastico";
		 else if (p1 && p4 && p5 && p3)
	        prediccion="Lata, bolsa, colilla y brick";
		 else if (p5 && p2 && p3)
	        prediccion="Colilla, plastico y brick";
		 else if (p4 && p3 && p2)
	        prediccion="Bolsa, brick y plastico";
		 else if (p4 && p5 && p2)
	        prediccion="Bolsa, colilla y plastico";
		 else if (p4 && p5 && p3)
	        prediccion="Bolsa, colilla y brick";
		 else if (p1 && p5 && p3)
	        prediccion="Lata, colilla y brick";
		 else if (p1 && p3 && p2)
	        prediccion="Lata, brick y plastico";
		 else if (p1 && p4 && p5)
	        prediccion="Lata, bolsa y colilla";
		 else if (p1 && p5 && p2)
	        prediccion="Lata, colilla y plastico";
		 else if (p1 && p4 && p2)
			 prediccion="Lata, bolsa y plastico";
		 else if (p1 && p4 && p3)
			 prediccion="Lata, bolsa y brick";
		 else if (p2 && p3)
			 prediccion="Plastico y brick";
		 else if (p5 && p2)
	         prediccion="Colilla y plastico";
		 else if (p5 && p3)
			 prediccion="Colilla y brick";
		 else if (p4 && p2)
	         prediccion="Bolsa y plastico";
		 else if (p4 && p3)
	         prediccion="Bolsa y brick";
		 else if (p4 && p5)
	         prediccion="Bolsa y colilla";
		 else if (p1 && p2)
	         prediccion="Lata y plastico";
		 else if (p1 && p3)
			 prediccion="Lata y brick";
		 else if (p1 && p5)
	         prediccion="Lata y colilla";
		 else if (p1 && p4)
	         prediccion="Lata y bolsa";
		 else if (p1)
	         prediccion="Lata";
		 else if (p3)
	         prediccion="Brick";
		 else if (p5)
			 prediccion="Colilla";
		 else if (p4)
	         prediccion="Bolsa";
		 else if (p2)
	         prediccion="Plastico";
		 else
			 prediccion="Error, clase no identificada";
		
		return prediccion;
	}
	  
	public String identificar (String imgRuta) {
		
		BufferedImage img = null;  
		String aux = "Error calculando la prediccion";
		
		try {
			byte[] imageBytes = Files.readAllBytes(Paths.get(imgRuta));
			Tensor imagen=constructAndExecuteGraphToNormalizeImage(imageBytes);
		
			Predictor red1 = new Predictor();
			red1.prediccion(imagen, 1);
			
			Predictor red2= new Predictor();
			red2.prediccion(imagen, 2);

			Predictor red3 = new Predictor();
			red3.prediccion(imagen, 3);

			Predictor red4= new Predictor();
			red4.prediccion(imagen, 4);
			
			Predictor red5= new Predictor();
			red5.prediccion(imagen, 5);
			
			String objetos = new Main().idObjetos(red1.getPred(), red2.getPred(), red3.getPred(), red4.getPred(), red5.getPred());
			aux= "Identificados: " + objetos 
					+ " \nProbabilidades: " + "Lata - "+ red1.prob[0][0] + " Plastico - " + red2.prob[0][0] + " Brick - " + red3.prob[0][0] + " Bolsa - " + red4.prob[0][0] + " Colilla - " + red5.prob[0][0] ;

			
		} catch (IOException  e1) {

			e1.printStackTrace();
		}
	return aux;	
	
	}
	
	static class GraphBuilder {
	    GraphBuilder(Graph g) {
	      this.g = g;
	    }

	    Output div(Output x, Output y) {
	      return binaryOp("Div", x, y);
	    }

	    Output sub(Output x, Output y) {
	      return binaryOp("Sub", x, y);
	    }

	    Output resizeBilinear(Output images, Output size) {
	      return binaryOp("ResizeBilinear", images, size);
	    }

	    Output expandDims(Output input, Output dim) {
	      return binaryOp("ExpandDims", input, dim);
	    }

	    Output cast(Output value, DataType dtype) {
	      return g.opBuilder("Cast", "Cast").addInput(value).setAttr("DstT", dtype).build().output(0);
	    }

	    Output decodeJpeg(Output contents, long channels) {
	      return g.opBuilder("DecodeJpeg", "DecodeJpeg")
	          .addInput(contents)
	          .setAttr("channels", channels)
	          .build()
	          .output(0);
	    }

	    Output constant(String name, Object value) {
	      try (Tensor t = Tensor.create(value)) {
	        return g.opBuilder("Const", name)
	            .setAttr("dtype", t.dataType())
	            .setAttr("value", t)
	            .build()
	            .output(0);
	      }
	    }

	    private Output binaryOp(String type, Output in1, Output in2) {
	      return g.opBuilder(type, type).addInput(in1).addInput(in2).build().output(0);
	    }

	    private Graph g;
	  }
}
