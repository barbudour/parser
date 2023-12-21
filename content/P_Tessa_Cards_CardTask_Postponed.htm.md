# CardTask.Postponed - свойство
Дата и время, когда было отложено задание, или null, если задание не было
отложено. Поле устанавливается системой при откладывании задания.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DateTime? Postponed { get; set; }
VB __Копировать
     Public Property Postponed As DateTime?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<DateTime> Postponed {
    	Nullable<DateTime> get ();
    	void set (Nullable<DateTime> value);
    }
F# __Копировать
     member Postponed : Nullable<DateTime> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
##  __Заметки
Свойство заполняется платформой.
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
