# BusinessCalendarService.ValidateCalendarAsync - метод
Интерфейс API бизнес календаря.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<ValidationResult> ValidateCalendarAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function ValidateCalendarAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    virtual Task<ValidationResult^>^ ValidateCalendarAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract ValidateCalendarAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
    override ValidateCalendarAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>
#### Реализации
[IBusinessCalendarService.ValidateCalendarAsync(CancellationToken)](M_Tessa_BusinessCalendar_IBusinessCalendarService_ValidateCalendarAsync.htm)  
##  __См. также
#### Ссылки
[BusinessCalendarService -
](T_Tessa_BusinessCalendar_BusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
