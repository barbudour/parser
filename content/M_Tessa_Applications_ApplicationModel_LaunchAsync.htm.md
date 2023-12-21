# ApplicationModel.LaunchAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task LaunchAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LaunchAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ LaunchAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LaunchAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override LaunchAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[IApplicationModel.LaunchAsync(CancellationToken)](M_Tessa_Applications_IApplicationModel_LaunchAsync.htm)  
##  __Исключения
[NullReferenceException](https://learn.microsoft.com/dotnet/api/system.nullreferenceexception)|
The address is a null pointer.  
---|---  
## __См. также
#### Ссылки
[ApplicationModel - ](T_Tessa_Applications_ApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
