# AdminServerInitializationExtension - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Initialization](N_Tessa_Extensions_Platform_Server_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AdminServerInitializationExtension : ServerInitializationExtension
VB __Копировать
     Public NotInheritable Class AdminServerInitializationExtension
    	Inherits ServerInitializationExtension
C++ __Копировать
     public ref class AdminServerInitializationExtension sealed : public ServerInitializationExtension
F# __Копировать
     [<SealedAttribute>]
    type AdminServerInitializationExtension = 
        class
            inherit ServerInitializationExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ServerInitializationExtension](T_Tessa_Platform_Initialization_ServerInitializationExtension.htm) __ AdminServerInitializationExtension
##  __Конструкторы
[AdminServerInitializationExtension](M_Tessa_Extensions_Platform_Server_Initialization_AdminServerInitializationExtension__ctor.htm)|
Инициализирует новый экземпляр класса AdminServerInitializationExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Platform_Initialization_ServerInitializationExtension_AfterRequest.htm)|
Выполняет инициализацию приложения со стороны сервера после формирования
базового ответа от сервера, в т.ч. добавление обработчиков инициализации.  
(Унаследован от
[ServerInitializationExtension](T_Tessa_Platform_Initialization_ServerInitializationExtension.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Platform_Initialization_ServerInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны сервера как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
(Унаследован от
[ServerInitializationExtension](T_Tessa_Platform_Initialization_ServerInitializationExtension.htm))  
[BeforeRequest](M_Tessa_Extensions_Platform_Server_Initialization_AdminServerInitializationExtension_BeforeRequest.htm)|  
(Переопределяет
[ServerInitializationExtension.BeforeRequest(IServerInitializationExtensionContext)](M_Tessa_Platform_Initialization_ServerInitializationExtension_BeforeRequest.htm))  
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
[Tessa.Extensions.Platform.Server.Initialization - пространство
имён](N_Tessa_Extensions_Platform_Server_Initialization.htm)
