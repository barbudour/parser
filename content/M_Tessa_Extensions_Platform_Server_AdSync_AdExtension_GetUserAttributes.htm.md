# AdExtension.GetUserAttributes - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task<List<string>> GetUserAttributes(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetUserAttributes ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of String))
C++ __Копировать
     public:
    virtual Task<List<String^>^>^ GetUserAttributes(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetUserAttributes : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<string>> 
    override GetUserAttributes : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<string>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>>
#### Реализации
[IAdExtension.GetUserAttributes(CancellationToken)](M_Tessa_Extensions_Platform_Server_AdSync_IAdExtension_GetUserAttributes.htm)  
##  __См. также
#### Ссылки
[AdExtension - ](T_Tessa_Extensions_Platform_Server_AdSync_AdExtension.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
