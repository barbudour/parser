# IKrStageRowExtension - интерфейс
Описывает расширение на сериализацию этапов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrStageRowExtension : IExtension
VB __Копировать
     Public Interface IKrStageRowExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IKrStageRowExtension : IExtension
F# __Копировать
     type IKrStageRowExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[BeforeSerialization](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_BeforeSerialization.htm)|
Выполняется перед началом сериализации настроек этапов.  
---|---  
[DeserializationAfterRepair](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationAfterRepair.htm)|
Выполняется после десериализации и после восстановления строки этапов.  
[DeserializationBeforeRepair](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization_IKrStageRowExtension_DeserializationBeforeRepair.htm)|
Выполняется после десериализации, но перед восстановлением строк этапов. В
карточке на восстановление доступны строки с полями, перенесенными из
[Name](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Name.htm),
даже если в
[Virtual](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_Virtual.htm)
они отсутствуют.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Serialization -
пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Serialization.htm)
