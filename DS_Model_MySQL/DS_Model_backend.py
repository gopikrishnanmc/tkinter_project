import pymysql
from SPARQLWrapper import SPARQLWrapper, JSON

ns = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX foaf:<http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX rp: <http://www.semanticweb.org/abjb788/ontologies/2015/3/untitled-ontology-208#>
    PREFIX d: <http://localhost:3030/HierarchicalModel/data/Dental_pain_model>
    """


def Pain_present_insert_yes():
    v1 = "Yes"
    conn = pymysql.connect("localhost", "db_test", "111222", "iswc")
    cur = conn.cursor()
    cur.execute("DELETE FROM pain_present")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_present_Plus_1', 1, '9_ObservationPresent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_present_Plus_2', 2, '9_ObservationPresent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_absent_Plus_1', 1, '9_ObservationAbsent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_absent_Plus_2', 2, '9_ObservationAbsent')")
    conn.commit()
    conn.close()
    return v1


def Pain_present_insert_no():
    v1 = "No"
    conn = pymysql.connect("localhost", "db_test", "111222", "iswc")
    cur = conn.cursor()
    cur.execute("DELETE FROM pain_present")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_absent_Plus_1', 1, '9_ObservationPresent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_absent_Plus_2', 2, '9_ObservationPresent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_present_Plus_1', 1, '9_ObservationAbsent')")
    cur.execute("INSERT INTO pain_present values(NULL,'Pain_present_Plus_2', 2, '9_ObservationAbsent')")
    conn.commit()
    conn.close()
    return v1


# Pain_present_insert_yes()

def add_data():
    sparql=SPARQLWrapper("http://localhost:3030/HierarchicalModel/update")
    sparql.setQuery(ns+"""
    COPY d: to DEFAULT;
        """)
    sparql.setMethod('POST')
    sparql.setReturnFormat(JSON)
    result=sparql.query().convert()
    return(result)



def view():
    sparql = SPARQLWrapper("http://localhost:3030/HierarchicalModel/query")
    sparql.setQuery(ns+"""
        SELECT ?Label ?DiagnosisWeight
        WHERE
        {
        ?PulpalDiagnosis  rp:hasDiagnosisObsWeight ?DiagnosisWeight.
        ?PulpalDiagnosis a ?Diagnosis.
        ?Diagnosis rdfs:subClassOf* rp:Pulpal_Disease.
        ?Diagnosis rdfs:label ?Label
        } ORDER BY desc (?DiagnosisWeight)
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return (results)


def insertDSModel():

    sparql=SPARQLWrapper("http://localhost:3030/HierarchicalModel/update")
    sparql.setQuery(ns+"""
        INSERT {?Diagnosis rp:hasDiagnosisObsWeight ?DiagnosisObsWeight}
        WHERE
        {SELECT (SUM (?Weight)AS ?DiagnosisObsWeight) ?Diagnosis
         {?Diagnosis ?property ?Observation.
         ?property rdfs:subPropertyOf rp:Observation_Diagnosis_properties.
         SERVICE<http://localhost:2020/sparql>{
        ?Observation rp:hasWeight ?Weight.
        ?Observation rp:hasObservationStatus "9_ObservationPresent".
          }}
        GROUP BY ?Diagnosis
        }
        """)
    sparql.setMethod('POST')
    sparql.setReturnFormat(JSON)
    result=sparql.query().convert()
    return(result)


def clear():
    sparql = SPARQLWrapper("http://localhost:3030/HierarchicalModel/update")
    sparql.setQuery("""
        CLEAR SILENT DEFAULT;
    """)
    sparql.setMethod('POST')
    sparql.setReturnFormat(JSON)
    result=sparql.query().convert()
    return(result)

clear()
#add_data()
#insertDSModel()
#view()

