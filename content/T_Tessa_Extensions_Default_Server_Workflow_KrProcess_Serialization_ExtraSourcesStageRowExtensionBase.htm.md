# ExtraSourcesStageRowExtensionBase - класс
Базовый абстрактный класс расширения на сериализацию параметров этапов
предоставляющий методы для получения и сохранения информации о дополнительных
методах этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ExtraSourcesStageRowExtensionBase : KrStageRowExtension
VB __Копировать
     Public MustInherit Class ExtraSourcesStageRowExtensionBase
    	Inherits KrStageRowExtension
C++ __Копировать
     public ref class ExtraSourcesStageRowExtensionBase abstract : public KrStageRowExtension
F# __Копировать
     [<AbstractClassAttribute>]
    type ExtraSourcesStageRowExtensionBase = 
        class
            inherit KrStageRowExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrStageRowExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension.htm) __ ExtraSourcesStageRowExtensionBase
Derived
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization.ExtraSourcesStageRowExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtension.htm)
##  __Конструкторы
[ExtraSourcesStageRowExtensionBase](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase__ctor.htm)|
Инициализирует новый экземпляр класса ExtraSourcesStageRowExtensionBase.  
---|---  
## __Свойства
[ExtraSourceSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_ExtraSourceSerializer.htm)|
Возвращает сериализатор объектов содержащих информацию о дополнительных
методах.  
---|---  
## __Методы
[BeforeSerialization](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension_BeforeSerialization.htm)|
Выполняется перед началом сериализации настроек этапов.  
(Унаследован от
[KrStageRowExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension.htm))  
---|---  
[DeserializationAfterRepair](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension_DeserializationAfterRepair.htm)|
Выполняется после десериализации и после восстановления строки этапов.  
(Унаследован от
[KrStageRowExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension.htm))  
[DeserializationBeforeRepair](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension_DeserializationBeforeRepair.htm)|
Выполняется после десериализации, но перед восстановлением строк этапов. В
карточке на восстановление доступны строки с полями, перенесенными из
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm),
даже если в
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm)
они отсутствуют.  
(Унаследован от
[KrStageRowExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageRowExtension.htm))  
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
[GetExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_GetExtraSources.htm)|
Возвращает коллекцию содержащую информацию о дополнительных скриптах этапа из
поля
[ExtraSources](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_ExtraSources.htm).  
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
[MoveSourceFromExtraSourcesToStageSettings](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_MoveSourceFromExtraSourcesToStageSettings.htm)|
Переносит информацию о сценарии этапа, текст тела которого расположен в поле
[ExtraSources](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_ExtraSources.htm),
в параметры этапа по ключу scriptField.  
[MoveSourceFromStageSettingsToExtraSources(IList<IExtraSource>,
IKrStageRowExtensionContext, CardRow,
KrExtraSourceDescriptor)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_MoveSourceFromStageSettingsToExtraSources_1.htm)|
Переносит информацию о сценарии этапа, текст тела которого расположен в поле
scriptField, в коллекцию содержащую информацию о дополнительных скриптах
этапа.  
[MoveSourceFromStageSettingsToExtraSources(IList<IExtraSource>,
IKrStageRowExtensionContext, CardRow, String, String, String, String, String,
String)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_MoveSourceFromStageSettingsToExtraSources.htm)|
Переносит информацию о сценарии этапа, текст тела которого расположен в поле
scriptField, в коллекцию содержащую информацию о дополнительных скриптах
этапа.  
[SetExtraSources](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_SetExtraSources.htm)|
Сохраняет заданную коллекцию содержащую информацию о дополнительных скриптах
этапа в поле
[ExtraSources](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_ExtraSources.htm).  
[SourceChanged](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_ExtraSourcesStageRowExtensionBase_SourceChanged.htm)|  
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
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)
