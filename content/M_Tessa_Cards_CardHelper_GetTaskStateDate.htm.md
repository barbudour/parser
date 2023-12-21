# CardHelper.GetTaskStateDate - метод
Возвращает дату, актуальную для состояния задания. Состояние можно получить
вызовом метода [GetTaskState(String, String,
Nullable<Guid>)](M_Tessa_Cards_CardHelper_GetTaskState.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static DateTime GetTaskStateDate(
    	DateTime created,
    	DateTime? inProgress,
    	DateTime? completed
    )
VB __Копировать
     Public Shared Function GetTaskStateDate ( 
    	created As DateTime,
    	inProgress As DateTime?,
    	completed As DateTime?
    ) As DateTime
C++ __Копировать
     public:
    static DateTime GetTaskStateDate(
    	DateTime created, 
    	Nullable<DateTime> inProgress, 
    	Nullable<DateTime> completed
    )
F# __Копировать
     static member GetTaskStateDate : 
            created : DateTime * 
            inProgress : Nullable<DateTime> * 
            completed : Nullable<DateTime> -> DateTime 
#### Параметры
created [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата создания задания.
inProgress
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
     Дата взятия задания в работу или null, если задание ещё не было взято в работу. 
completed
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>
     Дата завершения задания или null, если задание ещё не было завершено. 
#### Возвращаемое значение
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)  
Дата, актуальная для состояния задания.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
