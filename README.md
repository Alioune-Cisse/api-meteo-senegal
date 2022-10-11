<!DOCTYPE html>
<html lang="en">
<head>
  <!--title>Meteo Sénégal API</title-->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <!--script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script-->
</head>
<body>

<div class="container">
  <h2>API Météo Sénégal à temps réel</h2>
    <p>La météo de toutes les communes du Sénégal à n'importe quelle date et n'importe quelle heure.</p>

  <h3>Paramètres</h3>
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Clé</th>
        <th>Descriptions</th>
        <th>Valeurs ou Formats</th>
          <th>Par défaut</th>
          <th>Exemples</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>moment</td>
        <td>Le type de date que l'on veut récupérer la météo</td>
        <td>['hour', 'day', 'month']</td>
          <td>'hour'</td>
          <td>GET <a href="/api/v1?moment=day">/api/v1?moment=day</a></td>
      </tr>
      <tr>
        <td>start</td>
        <td>La date à partir de laquelle nous voulons extraire des informations</td>
        <td>jj/mm/aaaa hh:mn:ss</td>
          <td>7 jours avant l'instant d'exécution</td>
          <td>GET <a href="/api/v1?start=11/10/2022 00:13:34">/api/v1?start=11/10/2022 00:13:34</a></td>
      </tr>
      <tr>
        <td>end</td>
        <td>La date jusqu'à laquelle nous voulons extraire des informations</td>
        <td>jj/mm/aaaa hh:mn:ss</td>
          <td>12 heures après l'instant d'exécution</td>
          <td>GET <a href="/api/v1?moment=month&start=11/10/2022 00:13:34">/api/v1?moment=month&start=11/10/2022 00:13:34</a></td>
      </tr>
    </tbody>
  </table>
    <p>Exemple d'utilisation complet : GET <a href="/api/v1?moment=hour&start=12/09/2022 23:45:32&end=12/10/2022 00:00:00">/api/v1?moment=hour&start=12/09/2022 23:45:32&end=12/10/2022 00:00:00</a></p>
    <hr>
</div>
<div>
    <h3>Sorties : Format JSON</h3>
    <table class="table table-bordered res">
    <thead>
      <tr>
        <th>Variables</th>
        <th>Descriptions</th>
        <th>Format</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Date</td>
        <td>La date de l'observation</td>
        <td>date</td>
      </tr>
      <tr>
        <td>Address</td>
        <td>L'emplacement exact'</td>
        <td>string</td>
      </tr>
      <tr>
        <td>Department</td>
        <td>Le département où se trouve l'adresse</td>
        <td>string</td>
      </tr>
    <tr>
        <td>Latitude</td>
        <td>La latitude de l'adresse</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>Longitude</td>
        <td>La longitude de l'adresse</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>Altitude</td>
        <td>L'altitude' de l'adresse</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>tavg</td>
        <td>La température moyenne de l'air en °C</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>tmin</td>
        <td>La température minimale de l'air en °C</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>tmax</td>
        <td>La température maximale de l'air en °C</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>prcp</td>
        <td>Le total des précipitations (horaires, quotidiennes, mensuelles) en mm</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>snow</td>
        <td>L'épaisseur maximale de neige en mm</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>wdir</td>
        <td>La direction moyenne du vent en °C</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>wspd</td>
        <td>La vitesse moyenne du vent en °C</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>wpgt</td>
        <td>La rafale de vent maximale en km/h</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>pres</td>
        <td>La pression atmosphérique moyenne au niveau de la mer en hPa</td>
        <td>numeric</td>
      </tr>
    <tr>
        <td>tsun</td>
        <td>L'ensoleillement quotidien total en minutes (m)</td>
        <td>numeric</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
