# WfHelper - методы
##  __Методы
[CanModifyTaskCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_CanModifyTaskCard.htm)|
Возвращает признак того, что пользователь может изменять карточку-сателлит
задания.  
---|---  
[GetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetData.htm)|
Возвращает неструктурированную информацию по бизнес-процессам, содержащуюся в
карточке-сателлите Workflow. Если такая информация отсутствует в карточке, то
создаётся и возвращается новый объект
[WfData](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfData.htm).  
[GetResolutionState](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetResolutionState.htm)|
Возвращает состояние резолюции, полученное по её параметрам.  
[GetUsedComponentsAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_GetUsedComponentsAsync.htm)|
Возвращает используемые компоненты типового решения, по которым можно
определить возможность использования резолюций и других бизнес-процессов
Workflow.  
[HasWorkflowInfo](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_HasWorkflowInfo.htm)|
Возвращает признак того, что заданная запись истории заданий содержит
информацию из расширенной истории заданий Workflow.  
[LoadHistoryWorkflowInfoAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_LoadHistoryWorkflowInfoAsync.htm)|
Загружает расширенную информацию по бизнес-процессам Workflow для записей в
истории заданий, которые относятся к бизнес-процессам. Возвращает признак
того, что хотя бы для одной записи была установлена расширенная информация.  
[SatelliteWasNotFound](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SatelliteWasNotFound.htm)|
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.  
[SetController](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetController.htm)|
Устанавливает информацию о роли, на которую возвращается задание с контролем
исполнения. Устанавливать и проверять информацию имеет смысл только для
добавляемого задания task.  
[SetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetData.htm)|
Устанавливает неструктурированную информацию по бизнес-процессам для карточки-
сателлита Workflow.  
[SetResponseCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetResponseCard.htm)|
Устанавливает заданную карточку в ответе на запрос. При этом выполняется
компрессия карточки.  
[SetSatellite](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatellite.htm)|
Сохраняет карточку-сателлит в пакете основной карточки.  
[SetSatelliteID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatelliteID.htm)|
Устанавливает идентификатор карточки-сателлита Workflow в контексте
[IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm). Установка
значения, равного null, удаляет информацию из контекста.  
[SetSatelliteMainCardID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetSatelliteMainCardID.htm)|
Устанавливает идентификатор основной карточки для карточки-сателлита резолюций
Workflow.  
[TaskTypeIsResolution](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolution.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции.  
[TaskTypeIsResolutionWithoutControl](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolutionWithoutControl.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции, который не требует контроля исполнения.  
[TaskTypeIsResolutionWithoutOverdue](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TaskTypeIsResolutionWithoutOverdue.htm)|
Возвращает признак того, что тип задания с заданным идентификатором является
одним из типов заданий резолюции, который не требует индикации просроченности.  
[TryCreateResolutionPerformerRoleAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryCreateResolutionPerformerRoleAsync.htm)|
Создаёт временную роль для исполнителей резолюции, объединяющую список ролей,
включая контекстные роли. Возвращает null, если создаваемая роль не содержит
пользователей. Метод имеет смысл использовать только в том случае, если
указано более одной роли исполнителей. Созданную роль необходимо сохранить
средствами [IRoleRepository](T_Tessa_Roles_IRoleRepository.htm), прежде чем
использовать.  
[TryGetController](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetController.htm)|
Возвращает информацию о роли, на которую возвращается задание с контролем
исполнения. Возвращает признак того, что контроль исполнения выполняется.  
[TryGetData](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetData.htm)|
Возвращает неструктурированную информацию по бизнес-процессам, содержащуюся в
карточке-сателлите Workflow, или null, если такая информация отсутствует в
карточке.  
[TryGetPerformers](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetPerformers.htm)|
Возвращает массив строк с ролями исполнителей, используемыми при отправке
резолюции, или null, если получить список невозможно или список пуст.
Возвращаемое значение не может быть пустым массивом.  
[TryGetResponseCard](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetResponseCard.htm)|
Возвращает карточку из ответа на запрос, установленную посредством метода
[SetResponseCard(CardResponseBase,
Card)](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_SetResponseCard.htm),
или null, если карточка не была установлена.  
[TryGetSatellite](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatellite.htm)|
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.  
[TryGetSatelliteID](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatelliteID.htm)|
Возвращает идентификатор карточки-сателлита Workflow, сохранённого в заданном
контексте [IWorkflowContext](T_Tessa_Cards_Workflow_IWorkflowContext.htm), или
null, если идентификатор не был установлен.  
[TryGetSatelliteIDAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TryGetSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для резолюций Workflow по
идентификатору основной карточки или null, если карточка-сателлит отсутствует.  
[TypeSupportsWorkflowAsync](M_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper_TypeSupportsWorkflowAsync.htm)|
Возвращает признак того, что тип поддерживает бизнес-процессы Workflow, на
основании настроек типового решения.  
## __См. также
#### Ссылки
[WfHelper - ](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
