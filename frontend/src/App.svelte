<script>
  let message = "Loading...";

  async function fetchMessage() {
      const res = await fetch("http://localhost:8000/");
      const data = await res.json();
      message = data.message;
  }

  fetchMessage();
</script>

<h1>{message}</h1>
