# Tessa.Extensions.Default.Server.Workflow.Wf - пространство имён
Расширения типового решения на сервере, связанные с отправкой типовых задач.
##  __Классы
[Registrator](T_Tessa_Extensions_Default_Server_Workflow_Wf_Registrator.htm)|  
---|---  
[WfGetResolutionVisualizationDataRequestExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfGetResolutionVisualizationDataRequestExtension.htm)|
Возвращает сжатую карточку для визуализации резолюций Workflow. Карточка
содержит все задания резолюций с их секциями (без календаря), а также все
записи в истории заданий, относящиеся к заданиям резолюций. Не содержит секций
карточки, файлов и прочих заданий.  
[WfResolutionCheckSafeLimitStoreTaskExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfResolutionCheckSafeLimitStoreTaskExtension.htm)|  
[WfResolutionStoreTaskExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfResolutionStoreTaskExtension.htm)|
При завершении дочерней резолюции с её удалением добавляется запись в
родительскую резолюцию о том, что дочерняя резолюция завершена (если
родительская резолюция ещё существует). При создании любой резолюции добавляет
запись в карточку-сателлит с информацией для истории заданий.  
[WfSatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfSatelliteHandler.htm)|  
[WfTaskSatelliteHandler](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfTaskSatelliteHandler.htm)|  
[WfTasksPermissionsExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfTasksPermissionsExtension.htm)|  
[WfTasksServerGetExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfTasksServerGetExtension.htm)|
Загрузка карточки с заполнением виртуальных секций в её заданиях. Метод
выполняется при загрузке для всех карточек во всех режимах CardGetMethod,
кроме Storage, но действительную работу выполняет только для заданий Workflow,
у которых загружены секции.  
[WfWorkflowManager](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowManager.htm)|
Объект, предоставляющий возможности для управления бизнес-процессами Workflow.  
[WfWorkflowStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowStoreExtension.htm)|
Расширение, выполняющее взаимодействие с бизнес-процессом Workflow при
сохранении карточки.  
[WfWorkflowWorker](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker.htm)|
Класс, реализующий логику бизнес-процессов Workflow.  
[WfWorkflowWorker.ResolutionParameters](T_Tessa_Extensions_Default_Server_Workflow_Wf_WfWorkflowWorker_ResolutionParameters.htm)|
Параметры резолюции, содержащие информацию по номерам переходов в подпроцессе.
