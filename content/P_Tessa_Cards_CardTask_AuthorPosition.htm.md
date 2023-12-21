# CardTask.AuthorPosition - свойство
Должность автора задания или null, если задание не было создано и в качестве
автора используется текущий пользователь или если должность автора будет
определена автоматически при сохранении. Автоматическое определение возможно,
если значение свойства [AuthorName](P_Tessa_Cards_CardTask_AuthorName.htm)
равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string AuthorPosition { get; set; }
VB __Копировать
     Public Property AuthorPosition As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ AuthorPosition {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member AuthorPosition : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
