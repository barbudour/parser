# ValidationHelper.ExecuteWithCatchExceptionAsync(Func<CancellationToken,
Task>, CancellationToken) - метод
Выполняет actionAsync и возникшие исключения помещает в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static Task<ValidationResult> ExecuteWithCatchExceptionAsync(
    	[NotNullAttribute] Func<CancellationToken, Task> actionAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Public Shared Function ExecuteWithCatchExceptionAsync ( 
    	<NotNullAttribute> actionAsync As Func(Of CancellationToken, Task),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ValidationResult)
C++ __Копировать
     public:
    [NotNullAttribute]
    static Task<ValidationResult^>^ ExecuteWithCatchExceptionAsync(
    	[NotNullAttribute] Func<CancellationToken, Task^>^ actionAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    static member ExecuteWithCatchExceptionAsync : 
            [<NotNullAttribute>] actionAsync : Func<CancellationToken, Task> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValidationResult> 
#### Параметры
actionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
     Выполняемое действие 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат выполнения
## __См. также
#### Ссылки
[ValidationHelper - ](T_Tessa_Applications_ValidationHelper.htm)
[ExecuteWithCatchExceptionAsync -
перегрузка](Overload_Tessa_Applications_ValidationHelper_ExecuteWithCatchExceptionAsync.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
