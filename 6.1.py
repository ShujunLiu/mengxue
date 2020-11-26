# coding=gbk
class Health:
    def _init_(self,height,weight):
        self.weight = weight
        self.height = height

    def get_BMI(self):
        BMI=self.weight / (self.height ** 2)
        if BMI < 18.5:
            result = [BMI,'过轻']
        elif BMI < 24:
                result = [BMI,'正常']
        elif BMI < 27:
                result = [BMI,'过重']
        elif BMI < 32:
                result = [BMI,'肥胖']
        else:
                result = [BMI,'非常肥胖']
        return result

        def show_BMI(self):
            BMI = self.get_BMI()
            print("BMI是{},显示{}。".format(round(BMI[0], 1),BMI[1]))

class Person:
    """对人的简单表示"""
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
        print('我的名字叫{}，我是一位{}士'.format(self.name.self.gender))

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
        print('我的名字叫{},我是一位{},来自{}学院{}专业'.format(self.name,self.gender,self.school,self.major)

    @classmethod
    def get_num_person(cls):
        return cls.num_student

def receive_advice(self,teacher_name,advice):
        print("学生{}收到{}老师的建议，\n。".format(self.name,teacher_name,advice))
        self.advice_;ist.append(advice)

class Teacher(Person):
    """大学教师"""
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
yue = Person('王月','男', 1.62, 70)
yue.show_p_BMI()
jia =Student('刘佳','男',1.75,60,'2019312022','信息','信息管理')
jia.show_p_BMI()
li = Teacher('李宝','女',1.88,60,'2013122222','文化与传媒','团委办公室')
li.ask_introduction_student(jia)


print('Person类已经创建{}个实例,format(Person.nim_person))
print('Student类已经创建了%s个实例' % Student.num_student)

student_list = [['name':'赵甲','gender':'男','height':1.63,'weight':60,'stu_id':'20183122201','school':'信息','maior':'信息管理']
                ['name':'钱乙','gender':'女','height':1.75,'weight':70,'stu_id':'20183122202','school':'金融', 'maior':'金融学']
                ['name':'孙丙','gender':'男','height':1.83,'weight':80,'stu_id':'20183122203','school':'金融','maior':'金融工程']
                ['name':'李丁','gender':'女','height':1.95,'weight':90,'stu_id':'20183122204','school':'会计','maior':'财务会计']
                ['name':'周戊','gender':'男','height':1.65,'weight':60,'stu_id':'20183122205','school':'财政','maior':'财政学']
                ['name':'吴已','gender':'女','height':1.75,'weight':70,'stu_id':'20183122206','school':'税务','maior':'税收学']
                ['name':'郑庚','gender':'男','height':1.85,'weight':80,'stu_id':'20183122207','school':'保险','maior':'保险学']
                ['name':'王辛','gender':'女','height':1.65,'weight':60,'stu_id':'20183122208','school':'统数','maior':'统计学']
                ['name':'冯壬','gender':'男','height':1.75,'weight':70,'stu_id':'20183122209','school':'经济','maior':'经济学']
                ['name':'陈庚','gender':'女','height':1.85,'weight':80,'stu_id':'20183122210','school':'文传','maior':'视觉传达']]

students = University_head_teacher.read_students(student_list)
yue = University_head_teacher('王月','男',1.62,70,'2014312200,'信息','信息管理','信管18', students)
print('(1)给学生建议：')
yue.give_advice('认真学习',students[0])
yue.give_advice('要读文献',students[0])
print('(2)班级介绍:')
yue.ask_introduction_class()
