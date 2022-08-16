function validar()
		{
			var user = document.getElementById("user").value;
			var pass = document.getElementById("pass").value;	

			if(user == "steveen" && pass == "1234")
			{
				//alert("Usuario y Contraseña validos");
				window.open("{{ url_for('tabled') }}")
			}
			else
			{
				window.open("{{ url_for('tabled') }}")
			}
		}