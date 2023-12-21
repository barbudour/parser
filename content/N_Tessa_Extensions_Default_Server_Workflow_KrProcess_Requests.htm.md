# Tessa.Extensions.Default.Server.Workflow.KrProcess.Requests - пространство
имён
Расширения типового решения на сервере, связанные с выполнением процессов
маршрутов по части обработки запросов.
##  __Классы
[KrCardGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCardGetExtension.htm)|
Расширение на загрузку карточки, имеющей основной сателлит
[KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm).
Переносит информацию из сателлита в соответствующие виртуальные секции.  
---|---  
[KrCardNewExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCardNewExtension.htm)|  
[KrCardStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCardStoreExtension.htm)|  
[KrCheckGroupBoundariesInSatelliteStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCheckGroupBoundariesInSatelliteStoreExtension.htm)|
Расширение на сохранение карточки основного сателлита.
Проверяет правильность расположения этапов маршрута в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm)).  
[KrCheckGroupBoundariesStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCheckGroupBoundariesStoreExtension.htm)|
Расширение на сохранение карточки, для которой включены маршруты документов.
Проверяет правильность расположения этапов маршрута в сохраняемой карточке.  
[KrCheckStageRowModifiedStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrCheckStageRowModifiedStoreExtension.htm)|
Расширение проверяет, изменилась ли строка с этапом согласования в карточке.
Если изменилась, делает соответствующую отметку в поле
[RowChanged](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_RowChanged.htm)
и
[OrderChanged](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStages_OrderChanged.htm).  
[KrInfoForInitiatorGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrInfoForInitiatorGetExtension.htm)|  
[KrLaunchProcessCustomExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrLaunchProcessCustomExtension.htm)|
Расширение обрабатывающее запрос
[LaunchProcessRequestType](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_LaunchProcessRequestType.htm)
выполняющий запуск процесса в соответствии с объектом типа
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
содержащемся в запросе.  
[KrLaunchProcessStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrLaunchProcessStoreExtension.htm)|
Расширение на сохранение карточки выполняющее запуск процесса в соответствии с
объектом типа
[KrProcessInstance](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessInstance.htm)
содержащемся в запросе на сохранение.  
[KrLocalTilesNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrLocalTilesNewGetExtension.htm)|
Расширение на создание и загрузку карточки. Загружает информацию о тайлах
вторичных процессов.  
[KrProcessWorkflowStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrProcessWorkflowStoreExtension.htm)|  
[KrStagePermissionsNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrStagePermissionsNewGetExtension.htm)|
Устанавливает права доступа на строки этапов.  
[KrStartProcessSignalInterceptorStoreExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrStartProcessSignalInterceptorStoreExtension.htm)|
Расширение на сохранение карточки обрабатывающее сигналы типа
[KrStartProcessSignal](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStartProcessSignal.htm)
и
[KrStartProcessUnlessStartedGlobalSignal](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrStartProcessUnlessStartedGlobalSignal.htm),
расположенные в очереди действий Workflow, осуществляя планирование запуска
основного процесса
[KrProcessName](F_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrConstants_KrProcessName.htm).  
[KrTaskKindGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTaskKindGetExtension.htm)|
Расширение, проставляющее информацию о виде задания из TaskCommonInfo.Kind в
task.Info. Это нужно для того, чтобы платформенное расширение
[TaskKindGetExtension](T_Tessa_Extensions_Platform_Server_Cards_TaskKindGetExtension.htm)
по этому Info проставило заголовок задания. По умолчанию заголовок ставится по
таск хистори, но если задание не пишется в историю, то это расширение
позволяет выставить заголовок.  
[KrTileNewGetExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrTileNewGetExtension.htm)|
Вычисляем видимость плиток типового решения на сервере при создании карточек,
добавленных в типовое решение.  
[KrUpdateParentTaskExtension](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_KrUpdateParentTaskExtension.htm)|  
[Registrator](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Requests_Registrator.htm)|