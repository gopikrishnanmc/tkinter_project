import pymysql

def connect():
    #conn = pymysql.connect("opencab1.miniserver.com","3306","ok_gopi","Optometry123","ok_mcd")
    conn = pymysql.connect(host='opencab1.miniserver.com', user='ok_gopi', passwd='Optometry123', db='ok_mcd', charset='utf8', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS `patient_data` (`id` int(10) NOT NULL,\
        `patient_name` varchar(50) DEFAULT NULL,\
        `year_of_birth` int(10) DEFAULT NULL,\
        PRIMARY KEY (`id`))")
        cur.execute("CREATE TABLE IF NOT EXISTS `family_history_enquiry` (`id` int(10) NOT NULL AUTO_INCREMENT,\
        `Jewish_ancestry` varchar(10) DEFAULT NULL,\
        `BRCA1_BRCA2_TP53` varchar(10) DEFAULT NULL,\
        `Childhood_adrenal_carcinomas_relative` varchar(10) DEFAULT NULL,\
        `Glioma_relative` varchar(10) DEFAULT NULL,\
        `Multiple_cancers_at_a_young_age_relative` varchar(10) DEFAULT NULL,\
        `Sarcoma_diagnosed_less_than_45_years_relative` varchar(10) DEFAULT NULL,\
        `patient_id` int(10) NOT NULL,\
        PRIMARY KEY (`id`))")
        cur.execute("CREATE TABLE IF NOT EXISTS `patient_history` (`id` int(10) NOT NULL AUTO_INCREMENT,\
        `Family_history_of_cancer` varchar(10) DEFAULT NULL,\
        `Personal_history_of_breast_cancer` varchar(10) DEFAULT NULL,\
        `Personal_history_of_melanoma` varchar(10) DEFAULT NULL,\
        `patient_id` int(10) NOT NULL,\
        PRIMARY KEY (`id`))")
        cur.execute("CREATE TABLE IF NOT EXISTS `relative_bilateral_breast_cancer_info` (`id` int(10) NOT NULL AUTO_INCREMENT,\
        `Breast_cancer_bilateral` varchar(10) DEFAULT NULL,\
        `patient_id` int(10) NOT NULL,\
        PRIMARY KEY (`id`)")
        cur.execute("CREATE TABLE IF NOT EXISTS `relative_cancer_info` (`id` int(10) NOT NULL AUTO_INCREMENT,\
        `Name_of_relative_affected` varchar(50) DEFAULT NULL,\
        `Type_of_relative_affected` varchar(20) DEFAULT NULL,\
        `Type_of_cancer` varchar(20) DEFAULT NULL,\
        `Other_cancer_type` varchar(50) DEFAULT NULL,\
        `Age_of_diagnosis` int(10) DEFAULT NULL,\
        `Age_of_death` int(10) DEFAULT NULL,\
        `patient_id` int(10) NOT NULL,\
        PRIMARY KEY (`id`))")
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def view():
    conn = pymysql.connect(host='opencab1.miniserver.com', user='ok_gopi', passwd='Optometry123', db='ok_mcd', charset='utf8', port=3306)
    cur  = conn.cursor()
    cur.execute("SELECT * FROM patient_data ")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(id="",patient_name="",year_of_birth=""):
    conn = pymysql.connect(host='opencab1.miniserver.com', user='ok_gopi', passwd='Optometry123', db='ok_mcd', charset='utf8', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient_data where id=%s OR patient_name=%s OR year_of_birth=%s",(id,patient_name,year_of_birth))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(patient_name,year_of_birth,id):
    conn = pymysql.connect(host='opencab1.miniserver.com', user='ok_gopi', passwd='Optometry123', db='ok_mcd', charset='utf8', port=3306)
    cur = conn.cursor()
    cur.execute("UPDATE patient_data SET patient_name=%s, year_of_birth=%s WHERE id=%s",(patient_name,year_of_birth,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = pymysql.connect(host='opencab1.miniserver.com', user='ok_gopi', passwd='Optometry123', db='ok_mcd', charset='utf8', port=3306)
    cur = conn.cursor()
    cur.execute("DELETE a.*,b.*,c.*,d.* FROM patient_data a \
                LEFT JOIN family_history_enquiry b ON a.id = b.patient_id \
                LEFT JOIN patient_history c ON a.id = c.patient_id \
                LEFT JOIN relative_cancer_info d ON a.id = d.patient_id \
                WHERE a.id = %s",(id))
    conn.commit()
    conn.close()


#connect()
#print(view())
#update('George',1985,1123)
#search(print(search(year_of_birth=1944)))
#delete(1123)
