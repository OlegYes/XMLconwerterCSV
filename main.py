from bs4 import BeautifulSoup
import csv
import datetime
import re

def ConwertDateFormat(date_strings):
    #print(date_strings)
    dt = datetime.datetime.strptime(date_strings, "%b %d, %Y %H:%M")
    date_time = dt.strftime("%m/%d/%Y, %H:%M")
    #print(date_time)
    return (date_time)


def parseXMLfile():
    title_list = []
    list_object = []
    with open('wc_surveys_all (1).xml', 'r') as f:
        data = f.read()
    bs_data = BeautifulSoup(data, 'xml')
    ssData_tag = bs_data.find_all("ss:Data")
    iterat = 0
    question = False
    write_title = True

    for element in ssData_tag:
        iterat += 1

        font_tag = element.find_all("Font")
        # is COMPLETED?
        first_font = element.find("Font")
        if first_font.text.strip() == "COMPLETED":
            #print(font_tag)

            for j in font_tag:
                if j.text.strip() != "COMPLETED":
                    dirty_item = j.text.strip().split(":")
                    key = dirty_item[0].strip()
                    #print(key)
                    value = dirty_item[1].strip()
                    #print(title_list.count("Response ID"))

                    if title_list.count("Response ID") == 0:
                        if key == "Response ID":
                            title_list.append(key)
                            list_object.append(value)

                    if title_list.count("Start time") == 0:
                        if key == "Start time":
                            title_list.append(key)
                            #print(value)
                            value = value+":"+dirty_item[2].strip()
                            full_month_date = value
                            #print(ConwertDateFormat(full_month_date))
                            time_Start =ConwertDateFormat(full_month_date).replace(',', '')
                            # print(time_Start)
                            list_object.append(time_Start)
                    if title_list.count("Time taken") == 0:
                        if key == "Time taken":
                            title_list.append(key)
                            list_object.append(value)
                    if title_list.count("Collector") == 0:
                        if key == "Collector":
                            title_list.append(key)
                            list_object.append(value)

        first_font = element.find("Font")
        if first_font.text.strip() == "Respondent Variables":
            for j in font_tag:
                if j.text.strip() != "Respondent Variables":
                    dirty_item = j.text.strip()
                    ch = '$'
                    if "1." in dirty_item:


                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Industry Sectors")
                            list_object.append(value)
                    if "2." in dirty_item:


                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Employment Status")
                            list_object.append(value)
                    if "3." in dirty_item:


                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("US - Education")
                            list_object.append(value)
                    if "4." in dirty_item:


                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Marital Status")
                            list_object.append(value)
                    if "5." in dirty_item:

                            title_list.append("United States household income (yearly)")
                    if "$" in dirty_item:

                            list_object.append(dirty_item)
                    if "6." in dirty_item:

                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Age")
                            list_object.append(value)
                    if "7." in dirty_item:

                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Age range")
                            list_object.append(value)
                    if "8." in dirty_item:

                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Gender")
                            list_object.append(value)
                    if "9." in dirty_item:

                            item = dirty_item.split(":")
                            value = item[1].strip()
                            title_list.append("Country")
                            list_object.append(value)
        value=""
        if "Q" in first_font.text.strip():
            w=""
            counter = 1
            cou = 0
            for j in font_tag:
                #print(j.text.strip())
                dirty_item = j.text.strip()
                condition = "Q" in dirty_item
                if "Q" in dirty_item:
                    dirty_item = "|"+dirty_item + "|"

                w = w +" "+ dirty_item

            list = w.split("|")
            list.pop(0)
            print(list)
            iterat = 0
            for i in list:
                iterat +=1
                if iterat % 2 >0:
                    title_list.append(i)
                if iterat %2 ==0:
                    list_object.append(i)





            #     if condition == False:
            #         w = w+dirty_item
            #     if counter != cou:
            #         list_object.append(w)
            #         w=""
            # list_object.append(w)

            # title_list.append(w[0])
            # list_object.append(w[1])
            #     dirty_item = j.text.strip()
            #     #print("Q" in dirty_item)
            #
            #
            #     if "Q" in dirty_item:
            #         title_list.append(dirty_item)
            #     else:
            #         value = value + " " + dirty_item
            # list_object.append(value)
            # value = ""

        with open("Table.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=" ")
            if title_list.count("Q22. Is there anything you'd like us to include that we haven't asked about?"):
                if write_title:
                    writer.writerow(title_list)
                    #write_title = False
                writer.writerow(list_object)
                title_list.clear()
                list_object.clear()

        # print(title_list)
        # print(list_object)

        # for j in font_tag:
        #     value = j.text
        #     print(value)


if __name__ == '__main__':
    parseXMLfile()


