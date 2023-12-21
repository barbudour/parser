# KrProcessHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrProcessHelper
VB __Копировать
     Public NotInheritable Class KrProcessHelper
C++ __Копировать
     public ref class KrProcessHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type KrProcessHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrProcessHelper
##  __Свойства
[WorkflowProcessSerializer](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_WorkflowProcessSerializer.htm)|
Объект, выполняющий сериализацию
[WorkflowProcess](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_WorkflowProcess.htm)
с использованием конвертера
[TypedJsonConverter](T_Tessa_Platform_Json_TypedJsonConverter.htm).  
---|---  
## __Методы
[CardExistsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_CardExistsAsync.htm)|
Асинхронно проверяет, существует ли карточка по записи в Instances.  
---|---  
[CardSupportsRoutesAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_CardSupportsRoutesAsync.htm)|
Возвращает значение, показывающее, поддерживает ли карточка маршруты.  
[CreateSatelliteInfo](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_CreateSatelliteInfo.htm)|
Создать информацию о сателлите.  
[CreateScriptInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_CreateScriptInstanceAsync.htm)|
Создаёт новый пустой экземпляр класса сценария маршрута.  
[DeserializeWorkflowProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_DeserializeWorkflowProcess.htm)|
Десериализует объектную модель процесса.  
[GetKrSatelliteIDAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_GetKrSatelliteIDAsync.htm)|
Возвращает идентификатор основного сателлита
[KrProcessName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrProcessName.htm)
процесса согласования.  
[GetSecondarySatellitesIDsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_GetSecondarySatellitesIDsAsync.htm)|
Возвращает список идентификаторов сателлитов вторичных процессов.  
[GetTemplateCardTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_GetTemplateCardTypeAsync.htm)|
Возвращает идентификатор типа карточки шаблона.  
[GetTemplateDocTypeAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_GetTemplateDocTypeAsync.htm)|
Асинхронно возвращает тип документа или тип карточки (если тип документа
отсутствует) из карточки шаблона.  
[IsTransactionOpened](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_IsTransactionOpened.htm)|
Возвращает значение, показывающее, открыта ли транзакция в текущем соединении.  
[SatelliteExistsAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_SatelliteExistsAsync.htm)|
Проверяет, существует ли основной сателлит
[KrProcessName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrProcessName.htm)
процесса согласования.  
[SerializeWorkflowProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_SerializeWorkflowProcess.htm)|
Сериализует объектную модель процесса.  
[SetInactiveStateToStages](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_SetInactiveStateToStages.htm)|
Устанавливает состояние
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)
для всех этапов маршрута.  
[SetStageDefaultValues](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_SetStageDefaultValues.htm)|
Устанавливает состояние
[Inactive](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrStageState_Inactive.htm)
для всех этапов маршрута.  
[SignWorkflowProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_SignWorkflowProcess.htm)|
Возвращает электронную цифровую подпись для объектной модели процесса.  
[TryCreateScriptInstanceAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_TryCreateScriptInstanceAsync.htm)|
Создаёт новый пустой экземпляр класса сценария маршрута. Не создаёт
исключений, если не удалось найти тип создаваемого экземпляра класса.
Информация об ошибке записывается в лог сервера приложений.  
[TryGetSecondarySatelliteInfoListAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_TryGetSecondarySatelliteInfoListAsync.htm)|
Возвращает список с информацией о сателлитах вторичных процессов.  
[VerifyWorkflowProcess](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessHelper_VerifyWorkflowProcess.htm)|
Проверяет валидность сериализованной объектной модели процесса.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Workflow - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow.htm)
