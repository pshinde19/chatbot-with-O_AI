import random
import string
from flask import Flask,request,jsonify,render_template,redirect,session
from call_llm2 import perform_llm_call
import pandas as pd
# import plotly.graph_objects as go
# from plotly.io   import write_html,to_html
import plotly.io as pio


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/get_tables')
def get_values():
    my_list = ['value1', 'value2', 'value3']
    return jsonify(my_list)


@app.route('/getanswer',methods=['POST'])
def getanswer():
    try:
        if request.method == 'POST':
            que=request.form['que']
            tablename=request.form['tablename']
            print('---------------',tablename,que)
            # response, new_data, graph_img, generated_response = perform_llm_call(que)
            # print(new_data)
            new_data1=''
            graph_html=''
            # config = {'responsive': True}
            # if(graph_img != None):
            #     graph_html = pio.to_html(graph_img,config=config,include_plotlyjs=False,full_html=True) 
            #     print(graph_html)
            # if(isinstance(new_data, pd.DataFrame)):
            #     new_data1=new_data.to_html()
            #     id=generate_random_id(10)
            #     # print('--------id',id)
            #     new_data1 = new_data1.replace('<table', f'<table class="my_table" id="{id}"', 1)
            # if(generated_response == None):
                # generated_response=''
            # if(response == None):
            #     response="Sales location with the highest revenue is 'PARIS' with a total revenue of 1039157.53."
            result={
             'graph_html':"""
<html>
<head><meta charset="utf-8" /></head>
<body>
    <div>                            <div id="1cb7677e-5ade-4926-ae94-c4c83ae0945d" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("1cb7677e-5ade-4926-ae94-c4c83ae0945d")) {                    Plotly.newPlot(                        "1cb7677e-5ade-4926-ae94-c4c83ae0945d",                        [{"x":["AARHUS","ABU DHABI","ACCRA","ADDIS ABABA","AHMEDABAD (GUJARAT)","AJMAN CITY","AMSTERDAM","ANCONA","ANNECY","ANTANANARIVO","ARNHEM","ATHENS","AUCKLAND","BAHRAIN","BANGALORE (KARNATAKA)","BANGKOK","BARCELONA","BEIJING","BELFORT","BELGRADE","BERGEN","BERLIN (WEST)","BIARRITZ","BILBAO","BIRMINGHAM","BOLOGNA","BOMBAY (MAH)","BORDEAUX","BRATISLAVA","BREMEN","BREST","BRISBANE","BRUSSELS","BUCHAREST","BUDAPEST","CAEN","CALICUT (KERALA)","CAPE TOWN","CHANDIGARH (PUNJAB)","CHENNAI (TN)","CHOLET","CLERMONT FERRAND","COCHIN (KERALA)","COLOGNE","COLOMBO","CONAKRY","COPENHAGEN","CREIL","DAKAR","DELHI (DEL)","DHAKA","DUBAI","DUBLIN","DUISBURG","DURBAN","EAST LONDON","EINDHOVEN","ESSEN","FLORENCE","FRANKFURT","FT DE FRANCE","GABORONE","GANZHOU","GENEVA","GUANGZHOU","HAIFA","HAMBURG","HARARE","HELSINKI","HO CHI MINH CITY","HONG KONG","HYDERABAD (AP)","ISTANBUL","JAIPUR (RAJASTHAN)","JALLANDHAR (PUNJAB)","JEDDAH","JOHANNESBURG","KANO","KIEL","KIEV","KITWE","KOLKATA (WB)","KORTRIJK","KUALA LUMPUR","LAGOS","LAUSANNE","LEEDS","LIBREVILLE","LINZ","LISBON","LJUBLJANA","LOME","LONDON","LONDON GATWICK AIRPORT","LONDON HEATHROW AIRPORT","LUCKNOW (UP)","LUSAKA","LUXEMBOURG","LYON","MADRID","MALAGA","MALMO","MANILA","MANSTON","MAPUTO","MARSEILLE","MAURITIUS","MELBOURNE \u002fTULLAMARINE APT.","MEXICO CITY","MILAN","MOSCOW","MUNICH","NAIROBI\u002fJOMO KENYATTA INTL.APT","NANTES","NAPLES","NELSON","NICE","NIORT","NUREMBERG","OPORTO","OREBRO","OSLO","PADERBORN","PALMA DE MALLORCA","PARIS","PERTH","PISA","PRAGUE","PRESTON","PRETORIA","QUIMPER","RAJKOT (GUJARAT)","READING","RENNES","RIJEKA","RIMINI","RODRIGUES IS","ROME","ROTTERDAM","ROUEN","RZESZOW","SANTO DOMINGO","SHANGHAI","SINGAPORE","ST DENIS DE LA REUNION","ST PIERRE REU","STOCKHOLM","STRASBOURG","STUTTGART","SYDNEY","TEL AVIV YAFO","TOKYO","TOULOUSE","TULEAR","TURIN","VADODARA (GUJARAT)","VENICE \u002fMARCO POLO APT.","VERONA","VIENNA","WARSAW","WINDHOEK","YAOUNDE","ZAGREB","ZLIN","ZURICH"],"y":[913.7,725.7,500.87,176.56,2068.39,436.81,31692.27,3407.7,129.74,59717.71,4131.82,7386.51,2063.78,148.68,2232.46,2246.37,1958.73,1442.6999999999998,9355.89,1211.74,434.01,77799.58,3880.67,13144.5,22272.96,1252.42,46795.14,8547.75,3433.3,48339.93,679.74,52469.33,41084.72,14078.99,10838.56,494.22,591.0,264451.21,102.21,6783.24,226.5,543.75,197.0,4433.9,8908.84,1605.84,59026.54,927.92,176.56,34304.020000000004,3862.5,51822.09,13846.63,3064.89,51510.14,289.41,1637.51,2502.37,1079.65,172469.21,1809.55,4943.63,2004.6399999999999,33038.79,1347.79,1484.8,250.48,1676.38,5615.68,684.0600000000001,6578.92,511.44,339.62,374.08,510.15999999999997,327.11,467694.15,286.21,1391.44,3839.76,1304.22,505.35,678.0,23518.79,512.96,3853.3599999999997,919.6600000000001,3826.12,7462.75,17141.9,5228.52,305.13,871956.25,2701.41,11779.19,731.33,1514.0300000000002,11440.529999999999,42906.03,32911.5,806.2999999999998,2799.67,3302.99,6718.5199999999995,1955.59,52352.3,1011446.73,50982.700000000004,739.13,72742.01,171.91,61119.54,10959.730000000001,5749.36,3930.91,13812.55,21701.63,5444.74,2194.0,9364.17,57.56,28835.63,1528.6299999999999,1294.72,1039157.53,36270.31,3539.06,65346.82,15777.11,4732.5,520.94,251.3,7678.57,2764.6200000000003,2414.4,5629.06,45319.02,18617.7,963.7799999999999,1786.58,245.94,19513.88,489.09000000000003,18666.66,110372.78,5337.4800000000005,56149.56,7180.7,865.9199999999998,150227.63,16779.86,711.0699999999999,30852.78,880.4000000000001,913.96,233.31,13493.5,2891.6,992.48,51079.1,2727.77,1706.3,557.78,5562.86,18717.59],"type":"bar"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"title":{"text":"Total Revenue by Sales Location"},"xaxis":{"title":{"text":"Sales Location"}},"yaxis":{"title":{"text":"Total Revenue"}}},                        {"responsive": true}                    )                };                            </script>        </div>
</body>
</html>
                            """,
             'new_data':"""<table class="my_table" id="hiiiuuxybk" border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SalesLocationName</th>
      <th>Pax_Rev_InclYQYREUR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AARHUS</td>
      <td>913.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ABU DHABI</td>
      <td>725.70</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ACCRA</td>
      <td>500.87</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ADDIS ABABA</td>
      <td>176.56</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AHMEDABAD (GUJARAT)</td>
      <td>2068.39</td>
    </tr>
    <tr>
      <th>5</th>
      <td>AJMAN CITY</td>
      <td>436.81</td>
    </tr>
    <tr>
      <th>6</th>
      <td>AMSTERDAM</td>
      <td>31692.27</td>
    </tr>
    <tr>
      <th>7</th>
      <td>ANCONA</td>
      <td>3407.70</td>
    </tr>
    <tr>
      <th>8</th>
      <td>ANNECY</td>
      <td>129.74</td>
    </tr>
    <tr>
      <th>9</th>
      <td>ANTANANARIVO</td>
      <td>59717.71</td>
    </tr>
    <tr>
      <th>10</th>
      <td>ARNHEM</td>
      <td>4131.82</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ATHENS</td>
      <td>7386.51</td>
    </tr>
    <tr>
      <th>12</th>
      <td>AUCKLAND</td>
      <td>2063.78</td>
    </tr>
    <tr>
      <th>13</th>
      <td>BAHRAIN</td>
      <td>148.68</td>
    </tr>
    <tr>
      <th>14</th>
      <td>BANGALORE (KARNATAKA)</td>
      <td>2232.46</td>
    </tr>
    <tr>
      <th>15</th>
      <td>BANGKOK</td>
      <td>2246.37</td>
    </tr>
    <tr>
      <th>16</th>
      <td>BARCELONA</td>
      <td>1958.73</td>
    </tr>
    <tr>
      <th>17</th>
      <td>BEIJING</td>
      <td>1442.70</td>
    </tr>
    <tr>
      <th>18</th>
      <td>BELFORT</td>
      <td>9355.89</td>
    </tr>
    <tr>
      <th>19</th>
      <td>BELGRADE</td>
      <td>1211.74</td>
    </tr>
    <tr>
      <th>20</th>
      <td>BERGEN</td>
      <td>434.01</td>
    </tr>
    <tr>
      <th>21</th>
      <td>BERLIN (WEST)</td>
      <td>77799.58</td>
    </tr>
    <tr>
      <th>22</th>
      <td>BIARRITZ</td>
      <td>3880.67</td>
    </tr>
    <tr>
      <th>23</th>
      <td>BILBAO</td>
      <td>13144.50</td>
    </tr>
    <tr>
      <th>24</th>
      <td>BIRMINGHAM</td>
      <td>22272.96</td>
    </tr>
    <tr>
      <th>25</th>
      <td>BOLOGNA</td>
      <td>1252.42</td>
    </tr>
    <tr>
      <th>26</th>
      <td>BOMBAY (MAH)</td>
      <td>46795.14</td>
    </tr>
    <tr>
      <th>27</th>
      <td>BORDEAUX</td>
      <td>8547.75</td>
    </tr>
    <tr>
      <th>28</th>
      <td>BRATISLAVA</td>
      <td>3433.30</td>
    </tr>
    <tr>
      <th>29</th>
      <td>BREMEN</td>
      <td>48339.93</td>
    </tr>
    <tr>
      <th>30</th>
      <td>BREST</td>
      <td>679.74</td>
    </tr>
    <tr>
      <th>31</th>
      <td>BRISBANE</td>
      <td>52469.33</td>
    </tr>
    <tr>
      <th>32</th>
      <td>BRUSSELS</td>
      <td>41084.72</td>
    </tr>
    <tr>
      <th>33</th>
      <td>BUCHAREST</td>
      <td>14078.99</td>
    </tr>
    <tr>
      <th>34</th>
      <td>BUDAPEST</td>
      <td>10838.56</td>
    </tr>
    <tr>
      <th>35</th>
      <td>CAEN</td>
      <td>494.22</td>
    </tr>
    <tr>
      <th>36</th>
      <td>CALICUT (KERALA)</td>
      <td>591.00</td>
    </tr>
    <tr>
      <th>37</th>
      <td>CAPE TOWN</td>
      <td>264451.21</td>
    </tr>
    <tr>
      <th>38</th>
      <td>CHANDIGARH (PUNJAB)</td>
      <td>102.21</td>
    </tr>
    <tr>
      <th>39</th>
      <td>CHENNAI (TN)</td>
      <td>6783.24</td>
    </tr>
    <tr>
      <th>40</th>
      <td>CHOLET</td>
      <td>226.50</td>
    </tr>
    <tr>
      <th>41</th>
      <td>CLERMONT FERRAND</td>
      <td>543.75</td>
    </tr>
    <tr>
      <th>42</th>
      <td>COCHIN (KERALA)</td>
      <td>197.00</td>
    </tr>
    <tr>
      <th>43</th>
      <td>COLOGNE</td>
      <td>4433.90</td>
    </tr>
    <tr>
      <th>44</th>
      <td>COLOMBO</td>
      <td>8908.84</td>
    </tr>
    <tr>
      <th>45</th>
      <td>CONAKRY</td>
      <td>1605.84</td>
    </tr>
    <tr>
      <th>46</th>
      <td>COPENHAGEN</td>
      <td>59026.54</td>
    </tr>
    <tr>
      <th>47</th>
      <td>CREIL</td>
      <td>927.92</td>
    </tr>
    <tr>
      <th>48</th>
      <td>DAKAR</td>
      <td>176.56</td>
    </tr>
    <tr>
      <th>49</th>
      <td>DELHI (DEL)</td>
      <td>34304.02</td>
    </tr>
    <tr>
      <th>50</th>
      <td>DHAKA</td>
      <td>3862.50</td>
    </tr>
    <tr>
      <th>51</th>
      <td>DUBAI</td>
      <td>51822.09</td>
    </tr>
    <tr>
      <th>52</th>
      <td>DUBLIN</td>
      <td>13846.63</td>
    </tr>
    <tr>
      <th>53</th>
      <td>DUISBURG</td>
      <td>3064.89</td>
    </tr>
    <tr>
      <th>54</th>
      <td>DURBAN</td>
      <td>51510.14</td>
    </tr>
    <tr>
      <th>55</th>
      <td>EAST LONDON</td>
      <td>289.41</td>
    </tr>
    <tr>
      <th>56</th>
      <td>EINDHOVEN</td>
      <td>1637.51</td>
    </tr>
    <tr>
      <th>57</th>
      <td>ESSEN</td>
      <td>2502.37</td>
    </tr>
    <tr>
      <th>58</th>
      <td>FLORENCE</td>
      <td>1079.65</td>
    </tr>
    <tr>
      <th>59</th>
      <td>FRANKFURT</td>
      <td>172469.21</td>
    </tr>
    <tr>
      <th>60</th>
      <td>FT DE FRANCE</td>
      <td>1809.55</td>
    </tr>
    <tr>
      <th>61</th>
      <td>GABORONE</td>
      <td>4943.63</td>
    </tr>
    <tr>
      <th>62</th>
      <td>GANZHOU</td>
      <td>2004.64</td>
    </tr>
    <tr>
      <th>63</th>
      <td>GENEVA</td>
      <td>33038.79</td>
    </tr>
    <tr>
      <th>64</th>
      <td>GUANGZHOU</td>
      <td>1347.79</td>
    </tr>
    <tr>
      <th>65</th>
      <td>HAIFA</td>
      <td>1484.80</td>
    </tr>
    <tr>
      <th>66</th>
      <td>HAMBURG</td>
      <td>250.48</td>
    </tr>
    <tr>
      <th>67</th>
      <td>HARARE</td>
      <td>1676.38</td>
    </tr>
    <tr>
      <th>68</th>
      <td>HELSINKI</td>
      <td>5615.68</td>
    </tr>
    <tr>
      <th>69</th>
      <td>HO CHI MINH CITY</td>
      <td>684.06</td>
    </tr>
    <tr>
      <th>70</th>
      <td>HONG KONG</td>
      <td>6578.92</td>
    </tr>
    <tr>
      <th>71</th>
      <td>HYDERABAD (AP)</td>
      <td>511.44</td>
    </tr>
    <tr>
      <th>72</th>
      <td>ISTANBUL</td>
      <td>339.62</td>
    </tr>
    <tr>
      <th>73</th>
      <td>JAIPUR (RAJASTHAN)</td>
      <td>374.08</td>
    </tr>
    <tr>
      <th>74</th>
      <td>JALLANDHAR (PUNJAB)</td>
      <td>510.16</td>
    </tr>
    <tr>
      <th>75</th>
      <td>JEDDAH</td>
      <td>327.11</td>
    </tr>
    <tr>
      <th>76</th>
      <td>JOHANNESBURG</td>
      <td>467694.15</td>
    </tr>
    <tr>
      <th>77</th>
      <td>KANO</td>
      <td>286.21</td>
    </tr>
    <tr>
      <th>78</th>
      <td>KIEL</td>
      <td>1391.44</td>
    </tr>
    <tr>
      <th>79</th>
      <td>KIEV</td>
      <td>3839.76</td>
    </tr>
    <tr>
      <th>80</th>
      <td>KITWE</td>
      <td>1304.22</td>
    </tr>
    <tr>
      <th>81</th>
      <td>KOLKATA (WB)</td>
      <td>505.35</td>
    </tr>
    <tr>
      <th>82</th>
      <td>KORTRIJK</td>
      <td>678.00</td>
    </tr>
    <tr>
      <th>83</th>
      <td>KUALA LUMPUR</td>
      <td>23518.79</td>
    </tr>
    <tr>
      <th>84</th>
      <td>LAGOS</td>
      <td>512.96</td>
    </tr>
    <tr>
      <th>85</th>
      <td>LAUSANNE</td>
      <td>3853.36</td>
    </tr>
    <tr>
      <th>86</th>
      <td>LEEDS</td>
      <td>919.66</td>
    </tr>
    <tr>
      <th>87</th>
      <td>LIBREVILLE</td>
      <td>3826.12</td>
    </tr>
    <tr>
      <th>88</th>
      <td>LINZ</td>
      <td>7462.75</td>
    </tr>
    <tr>
      <th>89</th>
      <td>LISBON</td>
      <td>17141.90</td>
    </tr>
    <tr>
      <th>90</th>
      <td>LJUBLJANA</td>
      <td>5228.52</td>
    </tr>
    <tr>
      <th>91</th>
      <td>LOME</td>
      <td>305.13</td>
    </tr>
    <tr>
      <th>92</th>
      <td>LONDON</td>
      <td>871956.25</td>
    </tr>
    <tr>
      <th>93</th>
      <td>LONDON GATWICK AIRPORT</td>
      <td>2701.41</td>
    </tr>
    <tr>
      <th>94</th>
      <td>LONDON HEATHROW AIRPORT</td>
      <td>11779.19</td>
    </tr>
    <tr>
      <th>95</th>
      <td>LUCKNOW (UP)</td>
      <td>731.33</td>
    </tr>
    <tr>
      <th>96</th>
      <td>LUSAKA</td>
      <td>1514.03</td>
    </tr>
    <tr>
      <th>97</th>
      <td>LUXEMBOURG</td>
      <td>11440.53</td>
    </tr>
    <tr>
      <th>98</th>
      <td>LYON</td>
      <td>42906.03</td>
    </tr>
    <tr>
      <th>99</th>
      <td>MADRID</td>
      <td>32911.50</td>
    </tr>
    <tr>
      <th>100</th>
      <td>MALAGA</td>
      <td>806.30</td>
    </tr>
    <tr>
      <th>101</th>
      <td>MALMO</td>
      <td>2799.67</td>
    </tr>
    <tr>
      <th>102</th>
      <td>MANILA</td>
      <td>3302.99</td>
    </tr>
    <tr>
      <th>103</th>
      <td>MANSTON</td>
      <td>6718.52</td>
    </tr>
    <tr>
      <th>104</th>
      <td>MAPUTO</td>
      <td>1955.59</td>
    </tr>
    <tr>
      <th>105</th>
      <td>MARSEILLE</td>
      <td>52352.30</td>
    </tr>
    <tr>
      <th>106</th>
      <td>MAURITIUS</td>
      <td>1011446.73</td>
    </tr>
    <tr>
      <th>107</th>
      <td>MELBOURNE /TULLAMARINE APT.</td>
      <td>50982.70</td>
    </tr>
    <tr>
      <th>108</th>
      <td>MEXICO CITY</td>
      <td>739.13</td>
    </tr>
    <tr>
      <th>109</th>
      <td>MILAN</td>
      <td>72742.01</td>
    </tr>
    <tr>
      <th>110</th>
      <td>MOSCOW</td>
      <td>171.91</td>
    </tr>
    <tr>
      <th>111</th>
      <td>MUNICH</td>
      <td>61119.54</td>
    </tr>
    <tr>
      <th>112</th>
      <td>NAIROBI/JOMO KENYATTA INTL.APT</td>
      <td>10959.73</td>
    </tr>
    <tr>
      <th>113</th>
      <td>NANTES</td>
      <td>5749.36</td>
    </tr>
    <tr>
      <th>114</th>
      <td>NAPLES</td>
      <td>3930.91</td>
    </tr>
    <tr>
      <th>115</th>
      <td>NELSON</td>
      <td>13812.55</td>
    </tr>
    <tr>
      <th>116</th>
      <td>NICE</td>
      <td>21701.63</td>
    </tr>
    <tr>
      <th>117</th>
      <td>NIORT</td>
      <td>5444.74</td>
    </tr>
    <tr>
      <th>118</th>
      <td>NUREMBERG</td>
      <td>2194.00</td>
    </tr>
    <tr>
      <th>119</th>
      <td>OPORTO</td>
      <td>9364.17</td>
    </tr>
    <tr>
      <th>120</th>
      <td>OREBRO</td>
      <td>57.56</td>
    </tr>
    <tr>
      <th>121</th>
      <td>OSLO</td>
      <td>28835.63</td>
    </tr>
    <tr>
      <th>122</th>
      <td>PADERBORN</td>
      <td>1528.63</td>
    </tr>
    <tr>
      <th>123</th>
      <td>PALMA DE MALLORCA</td>
      <td>1294.72</td>
    </tr>
    <tr>
      <th>124</th>
      <td>PARIS</td>
      <td>1039157.53</td>
    </tr>
    <tr>
      <th>125</th>
      <td>PERTH</td>
      <td>36270.31</td>
    </tr>
    <tr>
      <th>126</th>
      <td>PISA</td>
      <td>3539.06</td>
    </tr>
    <tr>
      <th>127</th>
      <td>PRAGUE</td>
      <td>65346.82</td>
    </tr>
    <tr>
      <th>128</th>
      <td>PRESTON</td>
      <td>15777.11</td>
    </tr>
    <tr>
      <th>129</th>
      <td>PRETORIA</td>
      <td>4732.50</td>
    </tr>
    <tr>
      <th>130</th>
      <td>QUIMPER</td>
      <td>520.94</td>
    </tr>
    <tr>
      <th>131</th>
      <td>RAJKOT (GUJARAT)</td>
      <td>251.30</td>
    </tr>
    <tr>
      <th>132</th>
      <td>READING</td>
      <td>7678.57</td>
    </tr>
    <tr>
      <th>133</th>
      <td>RENNES</td>
      <td>2764.62</td>
    </tr>
    <tr>
      <th>134</th>
      <td>RIJEKA</td>
      <td>2414.40</td>
    </tr>
    <tr>
      <th>135</th>
      <td>RIMINI</td>
      <td>5629.06</td>
    </tr>
    <tr>
      <th>136</th>
      <td>RODRIGUES IS</td>
      <td>45319.02</td>
    </tr>
    <tr>
      <th>137</th>
      <td>ROME</td>
      <td>18617.70</td>
    </tr>
    <tr>
      <th>138</th>
      <td>ROTTERDAM</td>
      <td>963.78</td>
    </tr>
    <tr>
      <th>139</th>
      <td>ROUEN</td>
      <td>1786.58</td>
    </tr>
    <tr>
      <th>140</th>
      <td>RZESZOW</td>
      <td>245.94</td>
    </tr>
    <tr>
      <th>141</th>
      <td>SANTO DOMINGO</td>
      <td>19513.88</td>
    </tr>
    <tr>
      <th>142</th>
      <td>SHANGHAI</td>
      <td>489.09</td>
    </tr>
    <tr>
      <th>143</th>
      <td>SINGAPORE</td>
      <td>18666.66</td>
    </tr>
    <tr>
      <th>144</th>
      <td>ST DENIS DE LA REUNION</td>
      <td>110372.78</td>
    </tr>
    <tr>
      <th>145</th>
      <td>ST PIERRE REU</td>
      <td>5337.48</td>
    </tr>
    <tr>
      <th>146</th>
      <td>STOCKHOLM</td>
      <td>56149.56</td>
    </tr>
    <tr>
      <th>147</th>
      <td>STRASBOURG</td>
      <td>7180.70</td>
    </tr>
    <tr>
      <th>148</th>
      <td>STUTTGART</td>
      <td>865.92</td>
    </tr>
    <tr>
      <th>149</th>
      <td>SYDNEY</td>
      <td>150227.63</td>
    </tr>
    <tr>
      <th>150</th>
      <td>TEL AVIV YAFO</td>
      <td>16779.86</td>
    </tr>
    <tr>
      <th>151</th>
      <td>TOKYO</td>
      <td>711.07</td>
    </tr>
    <tr>
      <th>152</th>
      <td>TOULOUSE</td>
      <td>30852.78</td>
    </tr>
    <tr>
      <th>153</th>
      <td>TULEAR</td>
      <td>880.40</td>
    </tr>
    <tr>
      <th>154</th>
      <td>TURIN</td>
      <td>913.96</td>
    </tr>
    <tr>
      <th>155</th>
      <td>VADODARA (GUJARAT)</td>
      <td>233.31</td>
    </tr>
    <tr>
      <th>156</th>
      <td>VENICE /MARCO POLO APT.</td>
      <td>13493.50</td>
    </tr>
    <tr>
      <th>157</th>
      <td>VERONA</td>
      <td>2891.60</td>
    </tr>
    <tr>
      <th>158</th>
      <td>VIENNA</td>
      <td>992.48</td>
    </tr>
    <tr>
      <th>159</th>
      <td>WARSAW</td>
      <td>51079.10</td>
    </tr>
    <tr>
      <th>160</th>
      <td>WINDHOEK</td>
      <td>2727.77</td>
    </tr>
    <tr>
      <th>161</th>
      <td>YAOUNDE</td>
      <td>1706.30</td>
    </tr>
    <tr>
      <th>162</th>
      <td>ZAGREB</td>
      <td>557.78</td>
    </tr>
    <tr>
      <th>163</th>
      <td>ZLIN</td>
      <td>5562.86</td>
    </tr>
    <tr>
      <th>164</th>
      <td>ZURICH</td>
      <td>18717.59</td>
    </tr>
  </tbody>
</table>""",
             'generated_response':'',
             'response':"Sales location with the highest revenue is 'PARIS' with a total revenue of 1039157.53."
            }
            return jsonify({'msg':'success','result':result})
    except Exception as e:
        print(e)
        return jsonify({'msg':'error','error':e})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

def generate_random_id(length=10):
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    # First character should be a letter
    first_char = random.choice(string.ascii_lowercase)
    
    # Remaining characters can be letters or digits
    characters = string.ascii_lowercase + '123456789'
    remaining_chars = ''.join(random.choice(characters) for _ in range(length - 1))
    
    # Combine the first character with the remaining ones
    random_id = first_char + remaining_chars
    return random_id


if __name__ == '__main__':
    app.run(debug=True)
