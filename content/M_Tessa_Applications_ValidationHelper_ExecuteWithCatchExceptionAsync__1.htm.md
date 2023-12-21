# ValidationHelper.ExecuteWithCatchExceptionAsync<T>(Func<CancellationToken,
Task<T>>, CancellationToken) - метод
Выполняет funcAsync и возникшие исключения помещает в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static Task<(T , ValidationResult result)> ExecuteWithCatchExceptionAsync<T>(
    	[NotNullAttribute] Func<CancellationToken, Task<T>> funcAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
    <NotNullAttribute>
    Public Shared Function ExecuteWithCatchExceptionAsync(Of T) ( 
    	<NotNullAttribute> funcAsync As Func(Of CancellationToken, Task(Of T)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of ( As T, result As ValidationResult))
C++ __Копировать
     public:
    [NotNullAttribute]
    generic<typename T>
    static Task<ValueTuple<T, ValidationResult^>>^ ExecuteWithCatchExceptionAsync(
    	[NotNullAttribute] Func<CancellationToken, Task<T>^>^ funcAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     [<NotNullAttribute>]
    static member ExecuteWithCatchExceptionAsync : 
            [<NotNullAttribute>] funcAsync : Func<CancellationToken, Task<'T>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<'T, ValidationResult>> 
#### Параметры
funcAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>
     Выполняемое действие 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<T,
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>>  
Результат выполнения
## __См. также
#### Ссылки
[ValidationHelper - ](T_Tessa_Applications_ValidationHelper.htm)
[ExecuteWithCatchExceptionAsync -
перегрузка](Overload_Tessa_Applications_ValidationHelper_ExecuteWithCatchExceptionAsync.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
