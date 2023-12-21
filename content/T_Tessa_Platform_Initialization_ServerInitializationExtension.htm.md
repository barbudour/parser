# ServerInitializationExtension - класс
Базовый класс для расширения для инициализации приложений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ServerInitializationExtension : IServerInitializationExtension, 
    	IExtension
VB __Копировать
     Public MustInherit Class ServerInitializationExtension
    	Implements IServerInitializationExtension, IExtension
C++ __Копировать
     public ref class ServerInitializationExtension abstract : IServerInitializationExtension, 
    	IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ServerInitializationExtension = 
        class
            interface IServerInitializationExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServerInitializationExtension
Derived
[Tessa.Extensions.Default.Server.Initialization.KrServerInitializationExtension](T_Tessa_Extensions_Default_Server_Initialization_KrServerInitializationExtension.htm)
[Tessa.Extensions.Default.Server.Initialization.KrWebDownloadServerInitializationExtension](T_Tessa_Extensions_Default_Server_Initialization_KrWebDownloadServerInitializationExtension.htm)
[Tessa.Extensions.Default.Server.Initialization.KrWebServerInitializationExtension](T_Tessa_Extensions_Default_Server_Initialization_KrWebServerInitializationExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Initialization.GlobalButtonsInitializationExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Initialization_GlobalButtonsInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.AdminServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_AdminServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.AllTablesMetadataServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_AllTablesMetadataServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.CardServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_CardServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.CheckVersionServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_CheckVersionServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.ConditionTypesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_ConditionTypesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.ExistentSingletonsServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_ExistentSingletonsServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.ExtensionAssembliesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_ExtensionAssembliesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.FileTemplatesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_FileTemplatesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.ForumServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_ForumServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.InitResponseServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_InitResponseServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.LicenseServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_LicenseServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.LicenseWarningServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_LicenseWarningServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.LocalizationServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_LocalizationServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.PasswordExpiresSoonInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_PasswordExpiresSoonInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.SearchQueryServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_SearchQueryServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.SingletonServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_SingletonServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.UnavailableTypesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_UnavailableTypesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.UserCipherInfoInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_UserCipherInfoInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.ViewServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_ViewServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebApplicationVersionServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebApplicationVersionServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebAvailableLocalizationsServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebAvailableLocalizationsServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebCheckAccessServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebCheckAccessServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebExistentSingletonsServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebExistentSingletonsServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebFileTemplatesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebFileTemplatesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebLicenseServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebLicenseServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebLocalizationServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebLocalizationServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebSearchQueryServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebSearchQueryServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebThemesServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebThemesServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebViewServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebViewServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WebWorkplaceServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WebWorkplaceServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Initialization.WorkplaceServerInitializationExtension](T_Tessa_Extensions_Platform_Server_Initialization_WorkplaceServerInitializationExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowGlobalButtonsInitializationExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowGlobalButtonsInitializationExtension.htm)
Подробнее __Less __
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm), [IServerInitializationExtension](T_Tessa_Platform_Initialization_IServerInitializationExtension.htm)
##  __Конструкторы
[ServerInitializationExtension](M_Tessa_Platform_Initialization_ServerInitializationExtension__ctor.htm)|
Инициализирует новый экземпляр класса ServerInitializationExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Platform_Initialization_ServerInitializationExtension_AfterRequest.htm)|
Выполняет инициализацию приложения со стороны сервера после формирования
базового ответа от сервера, в т.ч. добавление обработчиков инициализации.  
---|---  
[AfterRequestFinally](M_Tessa_Platform_Initialization_ServerInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны сервера как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Platform_Initialization_ServerInitializationExtension_BeforeRequest.htm)|
Выполняет инициализацию приложения со стороны сервера перед формированием
базового ответа от сервера, в т.ч. добавление обработчиков инициализации.  
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
