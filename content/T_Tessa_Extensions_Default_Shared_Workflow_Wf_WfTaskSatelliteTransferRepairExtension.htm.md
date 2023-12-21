# WfTaskSatelliteTransferRepairExtension - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WfTaskSatelliteTransferRepairExtension : CardSatelliteTransferRepairExtension
VB __Копировать
     Public NotInheritable Class WfTaskSatelliteTransferRepairExtension
    	Inherits CardSatelliteTransferRepairExtension
C++ __Копировать
     public ref class WfTaskSatelliteTransferRepairExtension sealed : public CardSatelliteTransferRepairExtension
F# __Копировать
     [<SealedAttribute>]
    type WfTaskSatelliteTransferRepairExtension = 
        class
            inherit CardSatelliteTransferRepairExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardRepairExtension](T_Tessa_Cards_Extensions_CardRepairExtension.htm) __[CardSatelliteTransferRepairExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension.htm) __ WfTaskSatelliteTransferRepairExtension
##  __Конструкторы
[WfTaskSatelliteTransferRepairExtension](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension__ctor.htm)|
Инициализирует новый экземпляр класса WfTaskSatelliteTransferRepairExtension  
---|---  
##  __Свойства
[IsTaskSatelite](P_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension_IsTaskSatelite.htm)|  
(Переопределяет
[CardSatelliteTransferRepairExtension.IsTaskSatelite](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_IsTaskSatelite.htm))  
---|---  
[MainCardIDColumnName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_MainCardIDColumnName.htm)|
Имя колонки с ссылкой на основную карточку, к которой относится сателлит.  
(Унаследован от
[CardSatelliteTransferRepairExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension.htm))  
[SatelliteSectionName](P_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension_SatelliteSectionName.htm)|  
(Переопределяет
[CardSatelliteTransferRepairExtension.SatelliteSectionName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_SatelliteSectionName.htm))  
[StoreKey](P_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension_StoreKey.htm)|  
(Переопределяет
[CardSatelliteTransferRepairExtension.StoreKey](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_StoreKey.htm))  
[TaskRowIDColumnName](P_Tessa_Extensions_Default_Shared_Workflow_Wf_WfTaskSatelliteTransferRepairExtension_TaskRowIDColumnName.htm)|  
(Переопределяет
[CardSatelliteTransferRepairExtension.TaskRowIDColumnName](P_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension_TaskRowIDColumnName.htm))  
##  __Методы
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
(Унаследован от
[CardSatelliteTransferRepairExtension](T_Tessa_Cards_Extensions_Templates_CardSatelliteTransferRepairExtension.htm))  
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
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
