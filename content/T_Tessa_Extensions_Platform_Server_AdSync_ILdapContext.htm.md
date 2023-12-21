# ILdapContext - интерфейс
Контекст взаимодействия с сервером LDAP/AD по текущим открытым соединениям.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILdapContext : IAsyncDisposable
VB __Копировать
     Public Interface ILdapContext
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class ILdapContext : IAsyncDisposable
F# __Копировать
     type ILdapContext = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[MainConnection](P_Tessa_Extensions_Platform_Server_AdSync_ILdapContext_MainConnection.htm)|  
---|---  
[Settings](P_Tessa_Extensions_Platform_Server_AdSync_ILdapContext_Settings.htm)|  
## __Методы
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
---|---  
[RemoveHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_ILdapContext_RemoveHostConnection.htm)|  
[SetHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_ILdapContext_SetHostConnection.htm)|  
[TryGetHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_ILdapContext_TryGetHostConnection.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
