# KrClientInitializationExtension - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Initialization](N_Tessa_Extensions_Default_Client_Initialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrClientInitializationExtension : KrClientAndConsoleInitializationExtension
VB __Копировать
     Public NotInheritable Class KrClientInitializationExtension
    	Inherits KrClientAndConsoleInitializationExtension
C++ __Копировать
     public ref class KrClientInitializationExtension sealed : public KrClientAndConsoleInitializationExtension
F# __Копировать
     [<SealedAttribute>]
    type KrClientInitializationExtension = 
        class
            inherit KrClientAndConsoleInitializationExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ClientInitializationExtension](T_Tessa_Platform_Initialization_ClientInitializationExtension.htm) __[KrClientAndConsoleInitializationExtension](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm) __ KrClientInitializationExtension
##  __Конструкторы
[KrClientInitializationExtension](M_Tessa_Extensions_Default_Client_Initialization_KrClientInitializationExtension__ctor.htm)|
Инициализирует новый экземпляр класса KrClientInitializationExtension  
---|---  
##  __Свойства
[CardCache](P_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension_CardCache.htm)|  
(Унаследован от
[KrClientAndConsoleInitializationExtension](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm))  
---|---  
##  __Методы
[AdditionalInitializationAsync](M_Tessa_Extensions_Default_Client_Initialization_KrClientInitializationExtension_AdditionalInitializationAsync.htm)|  
(Переопределяет
[KrClientAndConsoleInitializationExtension.AdditionalInitializationAsync(Guid[],
ListStorage<KrDocType>,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension_AdditionalInitializationAsync.htm))  
---|---  
[AfterRequest](M_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension_AfterRequest.htm)|  
(Унаследован от
[KrClientAndConsoleInitializationExtension](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm))  
[AfterRequestFinally](M_Tessa_Platform_Initialization_ClientInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны клиента как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
(Унаследован от
[ClientInitializationExtension](T_Tessa_Platform_Initialization_ClientInitializationExtension.htm))  
[BeforeRequest](M_Tessa_Platform_Initialization_ClientInitializationExtension_BeforeRequest.htm)|
Выполняет инициализацию приложения со стороны клиента перед отправкой запроса
на сервер, в т.ч. добавление обработчиков инициализации.  
(Унаследован от
[ClientInitializationExtension](T_Tessa_Platform_Initialization_ClientInitializationExtension.htm))  
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
[Tessa.Extensions.Default.Client.Initialization - пространство
имён](N_Tessa_Extensions_Default_Client_Initialization.htm)
