# coding=gbk
class Health:
    def _init_(self,height,weight):
        self.weight = weight
        self.height = height

    def get_BMI(self):
        BMI=self.weight / (self.height ** 2)
        if BMI < 18.5:
            result = [BMI,'����']
        elif BMI < 24:
                result = [BMI,'����']
        elif BMI < 27:
                result = [BMI,'����']
        elif BMI < 32:
                result = [BMI,'����']
        else:
                result = [BMI,'�ǳ�����']
        return result

        def show_BMI(self):
            BMI = self.get_BMI()
            print("BMI��{},��ʾ{}��".format(round(BMI[0], 1),BMI[1]))

class Person:
    """���˵ļ򵥱�ʾ"""
    num_person = 0

    def _init_(self,name,gender,height,weight):
        self.name = name
        self.gender = gender
        self.height = height
        self.weifht = weight
        self.health - Health(height,weight)
        Person.num_person +=1

    def show_p_BMI(self):
        print('%s'%self.name)
        self.health.show_BMI()

    def introduce_self(self):
        print('�ҵ����ֽ�{}������һλ{}ʿ'.format(self.name.self.gender))

    @classmethod
    def get_num_person(cls):
        return cls.num_person

class Student(Person):
    num_srudent = 0

    def _init_(self,name,gender,height,weight,student_id,school,major):
        super()._init_(name,gender,height,weight)
        self.student_id = student_id
        self.school = school
        self.major = major
        self.advice_list = []
        Student.num_student += 1

    def introduce_self(self):
        print('�ҵ����ֽ�{},����һλ{},����{}ѧԺ{}רҵ'.format(self.name,self.gender,self.school,self.major)

    @classmethod
    def get_num_person(cls):
        return cls.num_student

def receive_advice(self,teacher_name,advice):
        print("ѧ��{}�յ�{}��ʦ�Ľ��飬\n��".format(self.name,teacher_name,advice))
        self.advice_;ist.append(advice)

class Teacher(Person):
    """��ѧ��ʦ"""
    num_teacher = o

     def _init_(self,name,gender,height,weight,job_id,school,department):
        super(Person,self)._init_()
        self.job_id = job.id
        self.school = school
        self.department = department
        Teacher.num_teacher += 1

    @classmethod
    def _init_(self,name,gender,height,weight,job_id,school,department):
        self.job_id =job.id
        self.school = school
        self.department = department
        Teacher.num_teachers += 1

    @classmethod
    def get_num_teacher(cla):
        return cla.num_teachers

     def ask_introduce_student(self,student):
        student.introduce_self()

     def give_advice(self,advice,student)
    student.receive_advice(self.name,advice)

class University_head_teacher(Teacher):
    def _init_(self,name,gender,height,weight,job_id,school,department,lead_class,class_student)
       super(Teacher,self)._init_(name,gender,height,weight)
       self.head_class = lead_class
       self.students = class_student

    def read_students(student_list):
        for i in range(len(student_list)):
            s = students_list[i]
            class_students.append(
                Student(s['name'],s['gender'],s['height'],s['weight'],s['stu_id'],s['school'],s['major'])
            )
        return class_students

    def ask_introduction_class(self):
        for i in range(len(self.students)):
            self.ask_introduce_student(students[i])
yue = Person('����','��', 1.62, 70)
yue.show_p_BMI()
jia =Student('����','��',1.75,60,'2019312022','��Ϣ','��Ϣ����')
jia.show_p_BMI()
li = Teacher('�','Ů',1.88,60,'2013122222','�Ļ��봫ý','��ί�칫��')
li.ask_introduction_student(jia)


print('Person���Ѿ�����{}��ʵ��,format(Person.nim_person))
print('Student���Ѿ�������%s��ʵ��' % Student.num_student)

student_list = [['name':'�Լ�','gender':'��','height':1.63,'weight':60,'stu_id':'20183122201','school':'��Ϣ','maior':'��Ϣ����']
                ['name':'Ǯ��','gender':'Ů','height':1.75,'weight':70,'stu_id':'20183122202','school':'����', 'maior':'����ѧ']
                ['name':'���','gender':'��','height':1.83,'weight':80,'stu_id':'20183122203','school':'����','maior':'���ڹ���']
                ['name':'�','gender':'Ů','height':1.95,'weight':90,'stu_id':'20183122204','school':'���','maior':'������']
                ['name':'����','gender':'��','height':1.65,'weight':60,'stu_id':'20183122205','school':'����','maior':'����ѧ']
                ['name':'����','gender':'Ů','height':1.75,'weight':70,'stu_id':'20183122206','school':'˰��','maior':'˰��ѧ']
                ['name':'֣��','gender':'��','height':1.85,'weight':80,'stu_id':'20183122207','school':'����','maior':'����ѧ']
                ['name':'����','gender':'Ů','height':1.65,'weight':60,'stu_id':'20183122208','school':'ͳ��','maior':'ͳ��ѧ']
                ['name':'����','gender':'��','height':1.75,'weight':70,'stu_id':'20183122209','school':'����','maior':'����ѧ']
                ['name':'�¸�','gender':'Ů','height':1.85,'weight':80,'stu_id':'20183122210','school':'�Ĵ�','maior':'�Ӿ�����']]

students = University_head_teacher.read_students(student_list)
yue = University_head_teacher('����','��',1.62,70,'2014312200,'��Ϣ','��Ϣ����','�Ź�18', students)
print('(1)��ѧ�����飺')
yue.give_advice('����ѧϰ',students[0])
yue.give_advice('Ҫ������',students[0])
print('(2)�༶����:')
yue.ask_introduction_class()
