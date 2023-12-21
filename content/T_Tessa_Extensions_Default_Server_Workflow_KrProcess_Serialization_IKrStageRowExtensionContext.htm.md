# IKrStageRowExtensionContext - интерфейс
Описывает контекст расширения на сериализацию этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageRowExtensionContext : IExtensionContext
VB __Копировать
     Public Interface IKrStageRowExtensionContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrStageRowExtensionContext : IExtensionContext
F# __Копировать
     type IKrStageRowExtensionContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[CardContext](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_CardContext.htm)|
Внешний контекст расширения. Может быть null.  
[CardToRepair](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_CardToRepair.htm)|
Карточка с настройками этапа, используемая для восстановления при загрузке.
Имеет значение null перед началом сериализации настроек этапов:
[BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm).  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_CardType.htm)|
Тип карточки. Перед сериализацией настроек этапов
([BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm))
возвращает тип
[InnerCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_InnerCard.htm),
после десериализации настроек этапов возвращает тип
[OuterCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_OuterCard.htm).  
[InnerCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_InnerCard.htm)|
"Входная" карточка.  
[OuterCard](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_OuterCard.htm)|
"Выходная" карточка.  
[RouteCardType](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_RouteCardType.htm)|
Тип карточки маршрута. Перед сериализацией настроек этапов
([BeforeSerialization(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm))
тип innerCard, после десериализации настроек этапов тип outerCard.  
[StageStorages](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtensionContext_StageStorages.htm)|
Коллекция ключ-значение, где ключ - идентификатор строки этапа, значение -
коллекция ключ-значение содержащая параметры этапа. Имеет значение null после
десериализации параметров этапов:
[DeserializationBeforeRepair(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationBeforeRepair.htm)
и
[DeserializationAfterRepair(IKrStageRowExtensionContext)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationAfterRepair.htm).  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)
