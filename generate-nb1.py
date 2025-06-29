import requests
from bs4 import BeautifulSoup

# Aici se va pune logica de scraping real
with open("nb1-ungaria-program.html", "w", encoding="utf-8") as f:
    f.write("""<h2>📅 Runda 1 – NB I Ungaria</h2>
<table class='superliga-tabel'><thead><tr><th>Data</th><th>Ora</th><th>Meci</th></tr></thead><tbody>
<tr><td><strong>26.07.</strong></td><td>18:00</td><td><strong>Kazincbarcika</strong> – <strong>Puskas Academy</strong></td></tr>
</tbody></table>""")
