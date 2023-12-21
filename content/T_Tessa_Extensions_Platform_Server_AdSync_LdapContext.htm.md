# LdapContext - класс
Контекст взаимодействия с сервером LDAP/AD по текущим открытым соединениям.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class LdapContext : ILdapContext, 
    	IAsyncDisposable
VB __Копировать
     Public Class LdapContext
    	Implements ILdapContext, IAsyncDisposable
C++ __Копировать
     public ref class LdapContext : ILdapContext, 
    	IAsyncDisposable
F# __Копировать
     type LdapContext = 
        class
            interface ILdapContext
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LdapContext
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [ILdapContext](T_Tessa_Extensions_Platform_Server_AdSync_ILdapContext.htm)
##  __Конструкторы
[LdapContext](M_Tessa_Extensions_Platform_Server_AdSync_LdapContext__ctor.htm)|
Инициализирует новый экземпляр класса LdapContext  
---|---  
##  __Свойства
[Connections](P_Tessa_Extensions_Platform_Server_AdSync_LdapContext_Connections.htm)|  
---|---  
[MainConnection](P_Tessa_Extensions_Platform_Server_AdSync_LdapContext_MainConnection.htm)|  
[Settings](P_Tessa_Extensions_Platform_Server_AdSync_LdapContext_Settings.htm)|  
## __Методы
[DisposeAsync](M_Tessa_Extensions_Platform_Server_AdSync_LdapContext_DisposeAsync.htm)|  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_LdapContext_RemoveHostConnection.htm)|  
[SetHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_LdapContext_SetHostConnection.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetHostConnection](M_Tessa_Extensions_Platform_Server_AdSync_LdapContext_TryGetHostConnection.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
