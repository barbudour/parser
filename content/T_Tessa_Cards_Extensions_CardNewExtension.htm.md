# CardNewExtension - класс
Базовый класс расширений для процесса создания структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardNewExtension : ICardNewExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardNewExtension
    	Implements ICardNewExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardNewExtension abstract : ICardNewExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardNewExtension = 
        class
            interface ICardNewExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardNewExtension
Derived
[Tessa.Extensions.Default.Server.BusinessCalendar.CalendarNewExtension](T_Tessa_Extensions_Default_Server_BusinessCalendar_CalendarNewExtension.htm)
[Tessa.Extensions.Default.Server.Cards.CardPermissionsNewExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsNewExtension.htm)
[Tessa.Extensions.Default.Server.Cards.DocLoadBarcodeTemplateNewExtension](T_Tessa_Extensions_Default_Server_Cards_DocLoadBarcodeTemplateNewExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrDocStateNewExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateNewExtension.htm)
[Tessa.Extensions.Default.Server.Cards.SatelliteRemoveCardNewExtension](T_Tessa_Extensions_Default_Server_Cards_SatelliteRemoveCardNewExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrWarnCannotCreateWhenCreatingTemplate](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrWarnCannotCreateWhenCreatingTemplate.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Actions.CardNewEventEmitter](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Actions_CardNewEventEmitter.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrCreateBasedOnNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrCreateBasedOnNewExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrSetDefaultSettingsValuesNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetDefaultSettingsValuesNewExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrSetTemplateDocTypeNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrSetTemplateDocTypeNewExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrCardNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCardNewExtension.htm)
[Tessa.Extensions.Platform.Client.Cards.TemplateRecordNewExtension](T_Tessa_Extensions_Platform_Client_Cards_TemplateRecordNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.BusinessProcessCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CompletionOptionNewExtension](T_Tessa_Extensions_Platform_Server_Cards_CompletionOptionNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FileConverterCacheNewExtension](T_Tessa_Extensions_Platform_Server_Cards_FileConverterCacheNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.FunctionRoleNewExtension](T_Tessa_Extensions_Platform_Server_Cards_FunctionRoleNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.LicenseNewExtension](T_Tessa_Extensions_Platform_Server_Cards_LicenseNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.MergeWithBilletCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_MergeWithBilletCardNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteNewExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SequenceNewExtension](T_Tessa_Extensions_Platform_Server_Cards_SequenceNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SingletonNewExtension](T_Tessa_Extensions_Platform_Server_Cards_SingletonNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateByTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateByTemplateNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateCardNewExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.TemplateNewExtension](T_Tessa_Extensions_Platform_Server_Cards_TemplateNewExtension.htm)
[Tessa.Extensions.Platform.Server.Numbers.NumberNewExtension](T_Tessa_Extensions_Platform_Server_Numbers_NumberNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.CheckPersonalRolePermissionsNewExtension](T_Tessa_Extensions_Platform_Server_Roles_CheckPersonalRolePermissionsNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.FixPersonalRoleTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixPersonalRoleTemplateNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.FixRolesNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.FixRolesTemplateNewExtension](T_Tessa_Extensions_Platform_Server_Roles_FixRolesTemplateNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.PersonalRoleDeputiesPermissionsNewExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleDeputiesPermissionsNewExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.PersonalRoleNewExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleNewExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.FillTimeZoneInRolesNewExtension](T_Tessa_Extensions_Platform_Server_TimeZones_FillTimeZoneInRolesNewExtension.htm)
[Tessa.Extensions.Platform.Server.TimeZones.TimeZonesNewExtension](T_Tessa_Extensions_Platform_Server_TimeZones_TimeZonesNewExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardNewExtension](M_Tessa_Cards_Extensions_CardNewExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardNewExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardNewExtension_AfterRequest.htm)|
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardNewExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardNewExtension_BeforeRequest.htm)|
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.  
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
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
