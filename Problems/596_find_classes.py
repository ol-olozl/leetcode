import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    num_student_per_class = courses.groupby("class")["student"].count().reset_index(name="num_student")
    df = num_student_per_class[num_student_per_class["num_student"] >= 5]
    return df[["class"]]
