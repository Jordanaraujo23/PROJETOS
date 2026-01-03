
with open('carousel_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('<div class="owl-carousel owl-theme" id="municipios-carousel">\n')
    for i in range(1, 41):
        f.write(f'    <div class="item"><img src="./YanTec_files/{i}.svg" class="mun-logo mb-2"><h6 class="mt-2 fw-semibold text-muted">Município</h6></div>\n')
    f.write('</div>')
