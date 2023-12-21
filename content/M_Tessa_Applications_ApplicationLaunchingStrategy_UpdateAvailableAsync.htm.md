# ApplicationLaunchingStrategy.UpdateAvailableAsync - метод
Проверяет необходимость обновления приложения. Возвращает признак наличия
обновления приложения и действительную разрядность приложения на момент
проверки, если обновление доступно (иначе нельзя опираться на возвращённое
значение).
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<(bool UpdateAvailable, bool ActualClient64Bit)> UpdateAvailableAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function UpdateAvailableAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of (UpdateAvailable As Boolean, ActualClient64Bit As Boolean))
C++ __Копировать
     public:
    virtual Task<ValueTuple<bool, bool>>^ UpdateAvailableAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract UpdateAvailableAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, bool>> 
    override UpdateAvailableAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<ValueTuple<bool, bool>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>  
Признак наличия обновления приложения и действительная разрядность приложения
на момент проверки, если обновление доступно (иначе нельзя опираться на
возвращённое значение).
#### Реализации
[IApplicationLaunchingStrategy.UpdateAvailableAsync(CancellationToken)](M_Tessa_Applications_IApplicationLaunchingStrategy_UpdateAvailableAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationLaunchingStrategy -
](T_Tessa_Applications_ApplicationLaunchingStrategy.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
