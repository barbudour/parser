# CardTask.PlannedQuants - свойство
Количество квантов календаря от времени на момент загрузки задания до времени
его запланированного завершения [Planned](P_Tessa_Cards_CardTask_Planned.htm)
или null, если задание ещё не было создано. Если возвращаемое количество
квантов отрицательное, то задание просрочено.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int? PlannedQuants { get; set; }
VB __Копировать
     Public Property PlannedQuants As Integer?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<int> PlannedQuants {
    	Nullable<int> get ();
    	void set (Nullable<int> value);
    }
F# __Копировать
     member PlannedQuants : Nullable<int> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
