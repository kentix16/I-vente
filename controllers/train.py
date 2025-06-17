import xlsxwriter

def generate_fic_excel(title,column_title, datas,):
    # Créer un nouveau fichier Excel
    workbook = xlsxwriter.Workbook(f'{title}.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(column_title)):
        worksheet.write(0,i,str(column_title[i]))

    for data in enumerate(datas):
        for item in enumerate(data[1]):
            worksheet.write(data[0]+1,item[0], str(item[1]))

    # Fermer le fichier
    workbook.close()

data = [('banane',2),('citron',5),('orange',6),('pommes','8')]
generate_fic_excel('fruit5',('modeles','quantité'),data)