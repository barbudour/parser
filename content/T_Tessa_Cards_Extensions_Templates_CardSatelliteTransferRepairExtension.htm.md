# CardSatelliteTransferRepairExtension - класс
Шаблон расширения для переноса карточек сателлитов на расширения универсальных
карточек сателлитов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CardSatelliteTransferRepairExtension : CardRepairExtension
VB __Копировать
     Public MustInherit Class CardSatelliteTransferRepairExtension
    	Inherits CardRepairExtension
C++ __Копировать
     public ref class CardSatelliteTransferRepairExtension abstract : public CardRepairExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type CardSatelliteTransferRepairExtension = 
        class
            inherit CardRepairExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm) __ CardSatelliteTransferRepairExtension
Derived
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrDialogSatelliteTransferRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrDialogSatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrSatelliteTransferRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrSatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.KrSecondarySatelliteTransferRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrSecondarySatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf.WfSatelliteTransferRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfSatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf.WfTaskSatelliteTransferRepairExtension](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.ForumSatelliteTransferRepairExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_ForumSatelliteTransferRepairExtension.htm)
[Tessa.Extensions.Platform.Server.Cards.Satellites.PersonalRoleSatelliteTransferRepairExtension](T_Tessa_Extensions_Platform_Server_Cards_Satellites_PersonalRoleSatelliteTransferRepairExtension.htm)
Подробнее __Less __
##  __Конструкторы
[CardSatelliteTransferRepairExtension](M_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension__ctor.htm)|
Инициализирует новый экземпляр класса CardSatelliteTransferRepairExtension  
---|---  
##  __Свойства
[IsTaskSatelite](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_IsTaskSatelite.htm)|
Определяет, относится ли данный тип сателлита к заданию или к карточке.  
---|---  
[MainCardIDColumnName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_MainCardIDColumnName.htm)|
Имя колонки с ссылкой на основную карточку, к которой относится сателлит.  
[SatelliteSectionName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_SatelliteSectionName.htm)|
Имя секции, где хранились ссылки на основную карточку и задание в карточке
сателлита.  
[StoreKey](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_StoreKey.htm)|
Имя ключа, по которому хранилась карточка сателлита или список карточек
сателлитов в card.Info основной карточки.  
[TaskRowIDColumnName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_TaskRowIDColumnName.htm)|
Имя колонки с ссылкой на задание, к которому относится сателлит.  
## __Методы
[AfterRequest](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequest.htm)|
Действие, выполняемое после исправления структуры карточки как при успешном,
так и при неудачном результате.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
---|---  
[AfterRequestFinally](M_Tessa_Cards_Extensions_CardRepairExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.  
(Унаследован от
[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm))  
[BeforeRequest](M_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_BeforeRequest.htm)|  
(Переопределяет
[CardRepairExtension.BeforeRequest(ICardRepairExtensionContext)](M_Tessa_Cards_Extensions_CardRepairExtension_BeforeRequest.htm))  
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
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
