for i in range(1, 40):
    filename = f"Ilaria-code/random/json/code{i}.html"
    content = f"""<html>
  <head>
    <script src="https://cdn.anychart.com/releases/8.8.0/js/anychart-core.min.js"></script>
    <script src="https://cdn.anychart.com/releases/8.8.0/js/anychart-graph.min.js"></script>
    <script src="https://cdn.anychart.com/releases/8.8.0/js/anychart-data-adapter.min.js"></script>
    <style type="text/css">
      html, body, #container {{
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }}
    </style>
  </head>
  <body>
    <div id="container"></div>
    <script>

      anychart.onDocumentReady(function () {{
        anychart.data.loadJsonFile("./data_images{i}.json", function (data) {{

          // create a chart from the loaded data
          var chart = anychart.graph(data);

          // set the title
          chart.title("Network Graph showing some of our idea connections");

          // access nodes
          var nodes = chart.nodes();

          // set the size of nodes
          nodes.normal().height(60);
          nodes.hovered().height(45);
          nodes.selected().height(45);

          // set the stroke of nodes
          nodes.normal().stroke(null);
          nodes.hovered().stroke("#333333", 3);
          nodes.selected().stroke("#333333", 3);

          // enable the labels of nodes
          chart.nodes().labels().enabled(true);

          // configure the labels of nodes
          chart.nodes().labels().format("{{%id}}");
          chart.nodes().labels().fontSize(12);
          chart.nodes().labels().fontWeight(600);

          // draw the chart
          chart.container("container").draw();

        }});
      }});

    </script>
  </body>
</html>"""
    
    with open(filename, 'w') as file:
        file.write(content)
