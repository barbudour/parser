# IBusinessCalendarService.ValidateCalendarAsync - метод
Проверяет календарь на отсутствие пропусков между квантами. Непредвиденные
ошибки при выполнении на клиенте возвращаются в объекте
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm), а при
выполнении на сервере - выбрасываются в виде исключений.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<ValidationResult> ValidateCalendarAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ValidateCalendarAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
    Task<ValidationResult^>^ ValidateCalendarAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ValidateCalendarAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат валидации.
##  __См. также
#### Ссылки
[IBusinessCalendarService -
](T_Tessa_BusinessCalendar_IBusinessCalendarService.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
