from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def quiz_count(self):
        return self.quiz_set.count()

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name='Quiz Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizzes'
    
    @property
    def question_count(self):
        return self.question_set.count()

class Update(models.Model):
    updated = models.DateTimeField(auto_now_add=True)  
    class Meta:
        abstract = True

class Question(Update):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name='Question Title')
    difficulty = models.CharField(max_length=1, choices=(('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')), default='E')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Questions'
    
    
class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=300, verbose_name='Answer Text')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    
    class Meta:
        verbose_name_plural = 'Answers'