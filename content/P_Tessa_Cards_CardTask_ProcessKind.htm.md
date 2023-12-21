# CardTask.ProcessKind - свойство
Тип бизнес-процесса, к которому относится запись в истории заданий, которая
будет добавлена для задания, или null, если запись не относится к бизнес-
процессу или не содержит информации по его типу. Свойство следует
устанавливать перед изменением или завершением задания, для которого будет
добавлена запись в истории. Свойство не изменяется при изменении записи в
истории. По умолчанию значение равно null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string ProcessKind { get; set; }
VB __Копировать
     Public Property ProcessKind As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ ProcessKind {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member ProcessKind : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
