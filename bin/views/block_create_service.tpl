    <p>
        <form action="" method="POST"  style="text-align: center">
            <label for="discription_text">Description of service:</label>
			<br>
            <textarea
                class="form-control"
                id="description_text"
                name="description_text"
                rows="60"
				cols="80"
                required >
{
  "Name": "web",
  "TaskTemplate": {
    "ContainerSpec": {
      "Image": "nginx:alpine",
      "Mounts": [
        {
          "ReadOnly": true,
          "Source": "web-data",
          "Target": "/usr/share/nginx/html",
          "Type": "volume",
          "VolumeOptions": {
            "DriverConfig": {
            },
            "Labels": {
              "com.example.something": "something-value"
            }
          }
        }
      ],
      "User": "33"
    }
  },
  "Mode": {
    "Replicated": {
      "Replicas": 4
    }
  },
  "EndpointSpec": {
    "Ports": [
      {
        "Protocol": "tcp",
        "PublishedPort": 8080,
        "TargetPort": 80
      }
    ]
  }
}
			</textarea>
			<br>
            <button class="btn btn-default" type="submit">Create</button>
        </form>
    </p>
