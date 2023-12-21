# IKrStageSerializer - интерфейс
Объект, предоставляющий методы для сериализации параметров этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageSerializer
VB __Копировать
     Public Interface IKrStageSerializer
C++ __Копировать
     public interface class IKrStageSerializer
F# __Копировать
     type IKrStageSerializer = interface end
##  __Свойства
[OrderColumns](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_OrderColumns.htm)|
Список секций и столбцов, по которым выполняется сортировка.  
---|---  
[ReferencesToStages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_ReferencesToStages.htm)|
Список прямых дочерних секций секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm).  
[SettingsFieldNames](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_SettingsFieldNames.htm)|
Список полей, содержащих параметры этапов.  
[SettingsSectionNames](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_SettingsSectionNames.htm)|
Список секций, содержащих параметры этапов.  
## __Методы
[Deserialize<T>](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_Deserialize__1.htm)|
Десериализовать объект из JSON.  
---|---  
[DeserializeSectionsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_DeserializeSectionsAsync.htm)|
Десериализует параметры этапа в виртуальные секции.  
[DeserializeSettingsStorageAsync(CardRow, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_DeserializeSettingsStorageAsync_1.htm)|
Десериализует параметры этапа.  
[DeserializeSettingsStorageAsync(String, Guid, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_DeserializeSettingsStorageAsync.htm)|
Десериализует параметры этапа.  
[FillStageSettings](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_FillStageSettings.htm)|
Заполняет хранилище с параметрами этапа данными содержащимися в указанной
строке содержащей информацию об этапе.  
[MergeStageSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_MergeStageSettingsAsync.htm)|
Выполняет обновление параметров этапов в krStagesSection в соответствии с
updatedSections.  
[Serialize](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_Serialize.htm)|
Сериализовать объект в JSON.  
[SerializeSettingsStorage](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_SerializeSettingsStorage.htm)|
Сериализует параметры этапа.  
[SetData](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_SetData.htm)|
Установить информацию по сериализуемым секциям и полям.  
[UpdateStageSettingsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageSerializer_UpdateStageSettingsAsync.htm)|
Обновляет сериализуемые параметры этапов в секции
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm)  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)
