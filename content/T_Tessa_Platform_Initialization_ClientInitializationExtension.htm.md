# ClientInitializationExtension - класс
Базовый класс для расширения для инициализации приложений со стороны клиента.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ClientInitializationExtension : IClientInitializationExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class ClientInitializationExtension
    	Implements IClientInitializationExtension, IExtension
C++ __Копировать
     public ref class ClientInitializationExtension abstract : IClientInitializationExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ClientInitializationExtension = 
        class
            interface IClientInitializationExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientInitializationExtension
Derived
[Tessa.Extensions.Default.Client.Workflow.KrProcess.Initialization.GlobalButtonsInitalizationExtension](T_Tessa_Extensions_Default_Client_Workflow_KrProcess_Initialization_GlobalButtonsInitalizationExtension.htm)
[Tessa.Extensions.Default.Shared.Initialization.KrClientAndConsoleInitializationExtension](T_Tessa_Extensions_Default_Shared_Initialization_KrClientAndConsoleInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.ExistentSingletonsClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_ExistentSingletonsClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.FileTemplatesClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_FileTemplatesClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.ForumClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_ForumClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.InitResponseClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_InitResponseClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.LocalizationClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_LocalizationClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.PasswordExpiresSoonNotificationInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_PasswordExpiresSoonNotificationInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.SearchQueryClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_SearchQueryClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.UnavailableTypesClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_UnavailableTypesClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.ViewClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_ViewClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.WorkflowGlobalButtonsInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_WorkflowGlobalButtonsInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization.WorkplaceClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_WorkplaceClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.AllTablesMetadataClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_AllTablesMetadataClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.CardClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_CardClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.ConditionTypesClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_ConditionTypesClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.ExtensionAssembliesClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_ExtensionAssembliesClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.LicenseClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_LicenseClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Shared.Initialization.SingletonClientInitializationExtension](T_Tessa_Extensions_Platform_Shared_Initialization_SingletonClientInitializationExtension.htm)
Подробнее __Less __
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [IClientInitializationExtension](T_Tessa_Platform_Initialization_IClientInitializationExtension.htm)
##  __Конструкторы
[ClientInitializationExtension](M_Tessa_Platform_Initialization_ClientInitializationExtension__ctor.htm)|
Инициализирует новый экземпляр класса ClientInitializationExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Platform_Initialization_ClientInitializationExtension_AfterRequest.htm)|
Выполняет инициализацию приложения со стороны клиента после отправки запроса
на сервер, в т.ч. добавление обработчиков инициализации.  
---|---  
[AfterRequestFinally](M_Tessa_Platform_Initialization_ClientInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны клиента как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Platform_Initialization_ClientInitializationExtension_BeforeRequest.htm)|
Выполняет инициализацию приложения со стороны клиента перед отправкой запроса
на сервер, в т.ч. добавление обработчиков инициализации.  
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
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
