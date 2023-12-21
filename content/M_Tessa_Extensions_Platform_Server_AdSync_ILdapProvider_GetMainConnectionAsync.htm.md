# ILdapProvider.GetMainConnectionAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<AdConnection> GetMainConnectionAsync(
    	ILdapContext context,
    	bool alwaysCreateNew = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetMainConnectionAsync ( 
    	context As ILdapContext,
    	Optional alwaysCreateNew As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of AdConnection)
C++ __Копировать
     ValueTask<AdConnection^> GetMainConnectionAsync(
    	ILdapContext^ context, 
    	bool alwaysCreateNew = false, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetMainConnectionAsync : 
            context : ILdapContext * 
            ?alwaysCreateNew : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _alwaysCreateNew = defaultArg alwaysCreateNew false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<AdConnection> 
#### Параметры
context
[ILdapContext](T_Tessa_Extensions_Platform_Server_AdSync_ILdapContext.htm)
alwaysCreateNew
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[AdConnection](T_Tessa_Extensions_Platform_Server_AdSync_AdConnection.htm)>
##  __См. также
#### Ссылки
[ILdapProvider -
](T_Tessa_Extensions_Platform_Server_AdSync_ILdapProvider.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
