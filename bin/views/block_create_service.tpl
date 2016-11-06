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
    },
    "LogDriver": {
      "Name": "json-file",
      "Options": {
        "max-file": "3",
        "max-size": "10M"
      }
    },
    "Placement": {},
    "Resources": {
      "Limits": {
        "MemoryBytes": 104857600.0
      },
      "Reservations": {
      }
    },
    "RestartPolicy": {
      "Condition": "on-failure",
      "Delay": 10000000000.0,
      "MaxAttempts": 10
    }
  },
  "Mode": {
    "Replicated": {
      "Replicas": 4
    }
  },
  "UpdateConfig": {
    "Delay": 30000000000.0,
    "Parallelism": 2,
    "FailureAction": "pause"
  },
  "EndpointSpec": {
    "Ports": [
      {
        "Protocol": "tcp",
        "PublishedPort": 8080,
        "TargetPort": 80
      }
    ]
  },
  "Labels": {
    "foo": "bar"
  }
}
			</textarea>
			<br>
            <button class="btn btn-default" type="submit">Create</button>
        </form>
    </p>
