# CardTask.AuthorName - свойство
Имя автора задания или null, если задание не было создано и в качестве автора
используется текущий пользователь или если имя автора будет определено
автоматически при сохранении. Автоматическое определение возможно, если
значение этого свойства равно null. Внимание! Должность автора
[AuthorPosition](P_Tessa_Cards_CardTask_AuthorPosition.htm) автоматически
заполняется только в том случае, если имя указано как null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string AuthorName { get; set; }
VB __Копировать
     Public Property AuthorName As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ AuthorName {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member AuthorName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
