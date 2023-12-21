# CardRepairExtension - класс
Базовый класс для расширения на исправление структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardRepairExtension : ICardRepairExtension, 
    	ICardExtension, IExtension
VB __Копировать
     Public MustInherit Class CardRepairExtension
    	Implements ICardRepairExtension, ICardExtension, IExtension
C++ __Копировать
     public ref class CardRepairExtension abstract : ICardRepairExtension, 
    	ICardExtension, IExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardRepairExtension = 
        class
            interface ICardRepairExtension
            interface ICardExtension
            interface IExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRepairExtension
Derived
[Tessa.Cards.Extensions.Templates.CardSatelliteRepairExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteRepairExtension.htm)
[Tessa.Cards.Extensions.Templates.CardSatelliteTransferRepairExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension.htm)
[Tessa.Cards.Extensions.Templates.TaskSatelliteRepairExtension](T_Tessa_Cards_Extensions_Templates_TaskSatelliteRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions.KrPermissionsRulesRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsRulesRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrProcessRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrSecondaryProcessRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrSecondaryProcessRepairExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.UniversalSatelliteRepairExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_UniversalSatelliteRepairExtension.htm)
[Tessa.Extensions.Platform.Server.Workflow.WorkflowEngineRepairExtension](T_Tessa_Extensions_Platform_Server_Workflow_WorkflowEngineRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.BusinessProcessTemplateExtendedRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_BusinessProcessTemplateExtendedRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.BusinessProcessTemplateRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_BusinessProcessTemplateRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.ErrorRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_ErrorRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.JsonRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_JsonRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Cards.TemplateRepairExtension](T_Tessa_Extensions_Platform_Shared_Cards_TemplateRepairExtension.htm)
[Tessa.Extensions.Platform.Shared.Conditions.ConditionsCardRepairExtensionBase](T_Tessa_Extensions_Platform_Shared_Conditions_ConditionsCardRepairExtensionBase.htm)
Подробнее __Less __
Implements
    [ICardExtension](T_Tessa_Cards_Extensions_ICardExtension.htm), [ICardRepairExtension](T_Tessa_Cards_Extensions_ICardRepairExtension.htm), [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Конструкторы
[CardRepairExtension](M_Tessa_Cards_Extensions_CardRepairExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardRepairExtension  
---|---  
##  __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequest.htm)|
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
[BeforeRequest](M_Tessa_Cards_Extensions_CardRepairExtension_BeforeRequest.htm)|
Действие, выполняемое перед исправлением структуры карточки.  
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
