# KrStageSerializer - класс
Объект, предоставляющий методы для сериализации параметров этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrStageSerializer : IKrStageSerializer
VB __Копировать
     Public NotInheritable Class KrStageSerializer
    	Implements IKrStageSerializer
C++ __Копировать
     public ref class KrStageSerializer sealed : IKrStageSerializer
F# __Копировать
     [<SealedAttribute>]
    type KrStageSerializer = 
        class
            interface IKrStageSerializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrStageSerializer
Implements
    [IKrStageSerializer](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer.htm)
##  __Конструкторы
[KrStageSerializer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer__ctor.htm)|
Инициализирует новый экземпляр класса KrStageSerializer  
---|---  
##  __Свойства
[OrderColumns](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_OrderColumns.htm)|
Список секций и столбцов, по которым выполняется сортировка.  
---|---  
[ReferencesToStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_ReferencesToStages.htm)|
Список прямых дочерних секций секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm).  
[SettingsFieldNames](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_SettingsFieldNames.htm)|
Список полей, содержащих параметры этапов.  
[SettingsSectionNames](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_SettingsSectionNames.htm)|
Список секций, содержащих параметры этапов.  
## __Методы
[Deserialize<T>](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_Deserialize__1.htm)|
Десериализовать объект из JSON.  
---|---  
[DeserializeSectionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_DeserializeSectionsAsync.htm)|
Десериализует параметры этапа в виртуальные секции.  
[DeserializeSettingsStorageAsync(CardRow, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_DeserializeSettingsStorageAsync_1.htm)|
Десериализует параметры этапа.  
[DeserializeSettingsStorageAsync(String, Guid, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_DeserializeSettingsStorageAsync.htm)|
Десериализует параметры этапа.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FillStageSettings](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_FillStageSettings.htm)|
Заполняет хранилище с параметрами этапа данными содержащимися в указанной
строке содержащей информацию об этапе.  
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
[MergeStageSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_MergeStageSettingsAsync.htm)|
Выполняет обновление параметров этапов в krStagesSection в соответствии с
updatedSections.  
[Serialize](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_Serialize.htm)|
Сериализовать объект в JSON.  
[SerializeSettingsStorage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_SerializeSettingsStorage.htm)|
Сериализует параметры этапа.  
[SetData](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_SetData.htm)|
Установить информацию по сериализуемым секциям и полям.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateStageSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_KrStageSerializer_UpdateStageSettingsAsync.htm)|
Обновляет сериализуемые параметры этапов в секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
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
