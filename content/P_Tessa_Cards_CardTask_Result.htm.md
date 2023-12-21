# CardTask.Result - свойство
Результат завершения задания, или null, если либо задание не завершается, либо
результат устанавливается серверными расширениями или не устанавливается
вообще. Результат может быть установлен не только при завершении задания, но и
при создании записи в истории заданий посредством указания флага
[CreateHistoryItem](T_Tessa_Cards_CardTaskFlags.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string Result { get; set; }
VB __Копировать
     Public Property Result As String
    	Get
    	Set
C++ __Копировать
     public:
    property String^ Result {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     member Result : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Свойство заполняется платформой.
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
