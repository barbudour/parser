# WindowsImpersonationContext - класс
Контекст имперсонализации Windows, содержащий информацию об учётной записи
[WindowsIdentity](https://learn.microsoft.com/dotnet/api/system.security.principal.windowsidentity),
от имени которой выполняется код.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WindowsImpersonationContext : IImpersonationContext
VB __Копировать
     Public NotInheritable Class WindowsImpersonationContext
    	Implements IImpersonationContext
C++ __Копировать
     public ref class WindowsImpersonationContext sealed : IImpersonationContext
F# __Копировать
     [<SealedAttribute>]
    type WindowsImpersonationContext = 
        class
            interface IImpersonationContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WindowsImpersonationContext
Implements
    [IImpersonationContext](T_Tessa_Platform_Runtime_IImpersonationContext.htm)
##  __Конструкторы
[WindowsImpersonationContext](M_Tessa_Platform_Runtime_WindowsImpersonationContext__ctor.htm)|
Создаёт экземпляр класса с указанием учётной записи Windows, от имени которой
выполняется имперсонализация.  
---|---  
## __Свойства
[AuthenticationType](P_Tessa_Platform_Runtime_WindowsImpersonationContext_AuthenticationType.htm)|
Тип аутентификации, который был использован для идентификации пользователя.  
---|---  
[Identity](P_Tessa_Platform_Runtime_WindowsImpersonationContext_Identity.htm)|
Объект, специфичный для платформы (операционной системы), и соответствующий
учётной записи пользователя.  
[IsAnonymous](P_Tessa_Platform_Runtime_WindowsImpersonationContext_IsAnonymous.htm)|
Признак того, что аккаунт пользователя был определён системой как анонимный.  
[IsAuthenticated](P_Tessa_Platform_Runtime_WindowsImpersonationContext_IsAuthenticated.htm)|
Признак того, что аутентификация была выполнена.  
[IsGuest](P_Tessa_Platform_Runtime_WindowsImpersonationContext_IsGuest.htm)|
Признак того, что аккаунт пользователя был определён системой как гостевой.  
[IsSystem](P_Tessa_Platform_Runtime_WindowsImpersonationContext_IsSystem.htm)|
Признак того, что аккаунт пользователя был определён системой как системный.  
[Name](P_Tessa_Platform_Runtime_WindowsImpersonationContext_Name.htm)| Имя
учётной записи пользователя, под которой был выполнен вход.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
