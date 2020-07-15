
import java.io.*;
import java.net.MalformedURLException;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

public class FileExample extends Application implements
  	EventHandler<ActionEvent> {

	private Label textArea;
	private Stage stage;
	private Button openButton;
	private Button saveButton;
	private ImageView img;
	private String imagenRuta;

	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage primaryStage) {

		stage = primaryStage;
		stage.setTitle("ECO-Sistema Inteligente de Reconocimiento de Desechos");
		
		// -- TOP --
		VBox top = new VBox();
		VBox margen = new VBox();
	    margen.setMinSize(100, 100);
	    
	    HBox aux = new HBox();
	    HBox margen2 = new HBox();
	    margen2.setMinSize(200, 200);
	    
		img = new ImageView();
		img.setFitHeight(400);
		img.setFitWidth(800);
		
		aux.getChildren().addAll(margen2,img);
		top.getChildren().addAll(margen,aux);
		
		
		// -- CENTER --
		VBox center = new VBox();
		center.setPrefSize(200, 100);
		VBox margen3 = new VBox();
	    margen3.setMinSize(50, 50);
	    
	    
	    HBox aux2 = new HBox();
	    final Pane margen4 = new Pane();
	    HBox.setHgrow(margen4, Priority.ALWAYS);
	    margen4.setMinSize(2, 2);
	    
	    
		final Button openButton = new Button("Abrir");
	    openButton.setMinSize(Button.USE_PREF_SIZE, Button.USE_PREF_SIZE);
	    openButton.setOnAction(this);
	    
	    final Pane spacer = new Pane();
	    HBox.setHgrow(spacer, Priority.ALWAYS);
	    spacer.setMinSize(1, 1);
	    
	    final Button evalButton = new Button("Identificar");
	    evalButton.setMinSize(Button.USE_PREF_SIZE, Button.USE_PREF_SIZE);
	    evalButton.setOnAction(this);
	    
	    openButton.setMinWidth(center.getPrefWidth()); 
	    evalButton.setMinWidth(center.getPrefWidth()); 
	    
		aux2.getChildren().addAll(margen4,openButton,spacer, evalButton);
		center.getChildren().addAll(margen3,aux2);
	    
	    // -- BOTTOM --
	    
		VBox bottom = new VBox();
		VBox margen5 = new VBox();
	    margen5.setMinSize(50, 50);
	    
	    HBox aux3 = new HBox();
	    HBox margen6 = new HBox();
	    margen6.setMinSize(200, 200);
	    
		textArea = new Label();
		textArea.setFont(new Font("Arial",20));
		
		aux3.getChildren().addAll(margen6,textArea);
		bottom.getChildren().addAll(margen5,aux3);

		

	    
		Group root = new Group();
		Scene scene = new Scene(root, 1200, 800, Color.WHITE);

		BorderPane border = new BorderPane();
		border.setTop(top);
		border.setCenter(center);
		border.setBottom(bottom);
		root.getChildren().add(border);

		primaryStage.setScene(scene);
		primaryStage.show();

	}

	@Override
	public void handle(ActionEvent event) {
		Button b = (Button) event.getSource();

		if (b.getText().equals("Abrir")) {
			FileChooser fileChooser = new FileChooser();
			fileChooser.setTitle("Selección de imagen");
			fileChooser.getExtensionFilters().addAll(new FileChooser.ExtensionFilter("Extensión imagenes", "*.bmp", "*.png", "*.jpg", "*.gif"));
			File file = fileChooser.showOpenDialog(stage);
	        if(file != null) {
                String imagepath;
				try {
					imagepath = file.toURI().toURL().toString();
	                System.out.println("file:" + imagepath);
	                Image image = new Image(imagepath);
	                System.out.println("height:"+image.getHeight()+"\nWidth:"+image.getWidth());
	                img.setImage(image);
	                imagenRuta=file.getAbsolutePath();
	                

				} catch (MalformedURLException e) {
					e.printStackTrace();
				}
	        }
	        else
	        {
	        	Alert alert = new Alert(Alert.AlertType.INFORMATION);
	        	alert.setTitle("Informacion");
	        	alert.setHeaderText("Porfavor, seleccione una imagen");
	        	/*alert.setContentText("You didn't select a file!");*/
	        	alert.showAndWait();
	        }
	        
		} else if (b.getText().equals("Identificar")) {
			
			try {
				
	            Main main= new Main();
	            String pred=main.identificar(imagenRuta);
	            textArea.setText(pred);
	            
	            
			}catch(Exception e){
				
				Alert alert = new Alert(Alert.AlertType.INFORMATION);
	        	alert.setTitle("Informacion");
	        	alert.setHeaderText("Compruebe que la imagen tenga dimensiones 400 x 800");
	        	alert.showAndWait();
			}
		}

	}
}

