# CardNewGetExtension - класс
Базовый класс расширений для расширений
[ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm) для
процесса создания карточки (файла, задания) и
[ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm) для
процесса загрузки карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardNewGetExtension : ICardNewExtension, 
    	ICardExtension, IExtension, ICardGetExtension
VB __Копировать
     Public MustInherit Class CardNewGetExtension
    	Implements ICardNewExtension, ICardExtension, IExtension, ICardGetExtension
C++ __Копировать
     public ref class CardNewGetExtension abstract : ICardNewExtension, 
    	ICardExtension, IExtension, ICardGetExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardNewGetExtension = 
        class
            interface ICardNewExtension
            interface ICardExtension
            interface IExtension
            interface ICardGetExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardNewGetExtension
Derived
[Tessa.Extensions.Default.Server.Cards.DefaultConfigurationVersionNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrPermissionRuleNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrPermissionRuleNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrPersonalRolesNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrPersonalRolesNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Cards.KrVirtualFileNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrStageGroupNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrStageGroupNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrCompilers.Requests.KrTemplateNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrCompilers_Requests_KrTemplateNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.KrStrictSecurityCardNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_KrStrictSecurityCardNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrLocalTilesNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrLocalTilesNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrStagePermissionsNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrStagePermissionsNewGetExtension.htm)
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests.KrTileNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTileNewGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.CardStrictSecurityNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_CardStrictSecurityNewGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.NotificationSubscriptionsCardGetExtension](T_Tessa_Extensions_Platform_Server_Cards_NotificationSubscriptionsCardGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SealedApplicationNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedApplicationNewGetExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.SealedSingletonNewGetExtension](T_Tessa_Extensions_Platform_Server_Cards_SealedSingletonNewGetExtension.htm)
[Tessa.Extensions.Platform.Server.Roles.StrictSecurityRoleNewGetExtension](T_Tessa_Extensions_Platform_Server_Roles_StrictSecurityRoleNewGetExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowTilesNewGetExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowTilesNewGetExtension.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardGetExtension](T_Tessa_Cards_Extensions_ICardGetExtension.htm), [ICardNewExtension](T_Tessa_Cards_Extensions_ICardNewExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardNewGetExtension](M_Tessa_Cards_Extensions_CardNewGetExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardNewGetExtension  
---|---  
##  __Методы
[AfterRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequest.htm)|
Действие, выполняемое после получения карточки как при успешном, так и при
неудачном результате.  
---|---  
[AfterRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequest_1.htm)|
Действие, выполняемое после создания структуры карточки как при успешном, так
и при неудачном результате.  
[AfterRequestFinally(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.  
[AfterRequestFinally(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequestFinally_1.htm)|
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest.htm)|
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.  
[BeforeRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest_1.htm)|
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
