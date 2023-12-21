# ApplicationsWebProxy.GetApplicationsAsync - метод
Возвращает список всех приложений, доступных пользователю.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<List<ApplicationPackage>> GetApplicationsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetApplicationsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of ApplicationPackage))
C++ __Копировать
     public:
    Task<List<ApplicationPackage^>^>^ GetApplicationsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetApplicationsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<ApplicationPackage>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>>  
Список приложений, доступных пользователю.
##  __См. также
#### Ссылки
[ApplicationsWebProxy -
](T_Tessa_Applications_Services_TessaServer_ApplicationsWebProxy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
