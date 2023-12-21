# SessionContext - класс
Контекст, переопределяющий токен для текущей сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionContext : ISessionContext
VB __Копировать
     Public NotInheritable Class SessionContext
    	Implements ISessionContext
C++ __Копировать
     public ref class SessionContext sealed : ISessionContext
F# __Копировать
     [<SealedAttribute>]
    type SessionContext = 
        class
            interface ISessionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionContext
Implements
    [ISessionContext](T_Tessa_Platform_Runtime_ISessionContext.htm)
##  __Конструкторы
[SessionContext](M_Tessa_Platform_Runtime_SessionContext__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Current](P_Tessa_Platform_Runtime_SessionContext_Current.htm)|  Текущий
контекст [ISessionContext](T_Tessa_Platform_Runtime_ISessionContext.htm).  
---|---  
[HasCurrent](P_Tessa_Platform_Runtime_SessionContext_HasCurrent.htm)|  Признак
того, что текущий код выполняется внутри операции с контекстом
[ISessionContext](T_Tessa_Platform_Runtime_ISessionContext.htm), а свойство
[Current](P_Tessa_Platform_Runtime_SessionContext_Current.htm) ссылается на
действительный контекст.  
[Token](P_Tessa_Platform_Runtime_SessionContext_Token.htm)| Токен с
информацией по сессии.  
[Unknown](P_Tessa_Platform_Runtime_SessionContext_Unknown.htm)|  Неизвестный
контекст [ISessionContext](T_Tessa_Platform_Runtime_ISessionContext.htm).  
## __Методы
[Create(ISessionContext)](M_Tessa_Platform_Runtime_SessionContext_Create.htm)|
Создаёт область операции, в которой заданный контекст будет являться текущим.  
---|---  
[Create(ISessionToken)](M_Tessa_Platform_Runtime_SessionContext_Create_1.htm)|
Создаёт область операции, в которой заданный токен будет являться текущим в
контексте.  
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
