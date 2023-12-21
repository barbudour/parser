# Tessa.Workflow - пространство имён
Серверное API и модели данных, общие на desktop-клиенте и сервере, для
конструктора бизнес-процессов.
##  __Классы
[ClientWorkflowService](T_Tessa_Workflow_ClientWorkflowService.htm)|  Сервис
для управления шаблонами, экземплярами и подписками Бизнес-процесса  
---|---  
[DiagWorkflowService](T_Tessa_Workflow_DiagWorkflowService.htm)|  Реализация
[IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm), которая выполняет
логирование времени выполнения методов  
[WorkflowEngineBindingContext](T_Tessa_Workflow_WorkflowEngineBindingContext.htm)|
Контекст привязки хеша к данным карточки, используемый в
[HashTreeBinder](T_Tessa_Workflow_Storage_HashTreeBinder.htm).  
[WorkflowEngineCache](T_Tessa_Workflow_WorkflowEngineCache.htm)|  Объект для
получения шаблонов процессов с кешированием их.  
[WorkflowEngineCardRequestExtender](T_Tessa_Workflow_WorkflowEngineCardRequestExtender.htm)|
Объект для расширения запросов на получение и сохранение карточки при
обработке в WorkflowEngine  
[WorkflowEngineCardsScope](T_Tessa_Workflow_WorkflowEngineCardsScope.htm)|
Scope для загрузки карточек в рамках обработки WorkflowEngine.  
[WorkflowEngineConsts](T_Tessa_Workflow_WorkflowEngineConsts.htm)|  
[WorkflowEngineContext](T_Tessa_Workflow_WorkflowEngineContext.htm)|  Контекст
обработки процесса в WorkflowEngine.  
[WorkflowEngineDatabaseLogger](T_Tessa_Workflow_WorkflowEngineDatabaseLogger.htm)|
Реализация логгера, которая пишет лог напрямую в базу. Создает свое
подключение к базе данных.  
[WorkflowEngineLockScope](T_Tessa_Workflow_WorkflowEngineLockScope.htm)|
Объект, отвечающий за блокировку экземпляра процесса.  
[WorkflowEngineManager](T_Tessa_Workflow_WorkflowEngineManager.htm)|
[WorkflowManager](T_Tessa_Cards_Workflow_WorkflowManager.htm) для обработчика
процессов WorkflowEngine  
[WorkflowEnginePermissionManager](T_Tessa_Workflow_WorkflowEnginePermissionManager.htm)|
Объект, осуществляющий проверку прав к шаблонам и экземплярам процессов  
[WorkflowEngineProcessorClient](T_Tessa_Workflow_WorkflowEngineProcessorClient.htm)|
Объект управляющий процессами WorkflowEngine с клиента.  
[WorkflowEngineProcessorExtensions](T_Tessa_Workflow_WorkflowEngineProcessorExtensions.htm)|  
[WorkflowEngineProcessorIterative](T_Tessa_Workflow_WorkflowEngineProcessorIterative.htm)|
Обработчик процессов WorkflowEngine на сервере.  
[WorkflowEngineProcessRequest](T_Tessa_Workflow_WorkflowEngineProcessRequest.htm)|
Запрос на обработку процесса WorkflowEngine.  
[WorkflowEngineProcessResult](T_Tessa_Workflow_WorkflowEngineProcessResult.htm)|
Результат обработки сигнала в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)  
[WorkflowEngineProcessSerializer](T_Tessa_Workflow_WorkflowEngineProcessSerializer.htm)|
Объект для сериализации и десериализации карточек процесса Workflow Engine  
[WorkflowEngineProcessStorageRequest](T_Tessa_Workflow_WorkflowEngineProcessStorageRequest.htm)|  
[WorkflowEngineTile](T_Tessa_Workflow_WorkflowEngineTile.htm)|  Информация о
настройках тайла бизнес-процесса.  
[WorkflowEngineTileCache](T_Tessa_Workflow_WorkflowEngineTileCache.htm)|
Объект для получения и кеширования информации о тайлах бизнес-процессов.  
[WorkflowEngineTileManager](T_Tessa_Workflow_WorkflowEngineTileManager.htm)|
Объект, который производит получение доступных кнопок процесса и производит
проверку доступа к ним  
[WorkflowEngineTileManagerExtensionRegistry](T_Tessa_Workflow_WorkflowEngineTileManagerExtensionRegistry.htm)|
Потокобезопасный реестр расширений прав доступа к тайлам WorkflowEngine
[IWorkflowEngineTileManagerExtension](T_Tessa_Workflow_IWorkflowEngineTileManagerExtension.htm).  
[WorkflowEngineTypes](T_Tessa_Workflow_WorkflowEngineTypes.htm)|  
[WorkflowEngineViewAliases](T_Tessa_Workflow_WorkflowEngineViewAliases.htm)|  
[WorkflowEngineWorker](T_Tessa_Workflow_WorkflowEngineWorker.htm)|
[IWorkflowWorker](T_Tessa_Cards_Workflow_IWorkflowWorker.htm) для обработки
процессов в WorkflowEngine  
[WorkflowExtensions](T_Tessa_Workflow_WorkflowExtensions.htm)|  
[WorkflowInstanceCardService](T_Tessa_Workflow_WorkflowInstanceCardService.htm)|
Реализация логгера и сервиса объектов экземпляра процесса, которая пишет в
карточку.  
[WorkflowRequestTypes](T_Tessa_Workflow_WorkflowRequestTypes.htm)|  Типы
запросов для [IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm).  
[WorkflowService](T_Tessa_Workflow_WorkflowService.htm)|  Сервис для
управления шаблонами, экземплярами и подписками Бизнес-процесса  
## __Интерфейсы
[IWorkflowEngineCache](T_Tessa_Workflow_IWorkflowEngineCache.htm)|  Объект для
получения шаблонов процессов с кешированием их.  
---|---  
[IWorkflowEngineCardRequestExtender](T_Tessa_Workflow_IWorkflowEngineCardRequestExtender.htm)|
Объект для расширения запросов на получение и сохранение карточки при
обработке в WorkflowEngine  
[IWorkflowEngineCardsScope](T_Tessa_Workflow_IWorkflowEngineCardsScope.htm)|
Scope для загрузки карточек в рамках обработки WorkflowEngine.  
[IWorkflowEngineContext](T_Tessa_Workflow_IWorkflowEngineContext.htm)|
Контекст обработки процесса в WorkflowEngine.  
[IWorkflowEngineLockScope](T_Tessa_Workflow_IWorkflowEngineLockScope.htm)|
Объект, отвечающий за блокировку экземпляра процесса.  
[IWorkflowEngineLogger](T_Tessa_Workflow_IWorkflowEngineLogger.htm)|  Логгер
процессов в Workflow Engine  
[IWorkflowEnginePermissionManager](T_Tessa_Workflow_IWorkflowEnginePermissionManager.htm)|
Объект, осуществляющий проверку прав к шаблонам и экземплярам процессов  
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)|
Обработчик процессов WorkflowEngine на сервере.  
[IWorkflowEngineProcessorClient](T_Tessa_Workflow_IWorkflowEngineProcessorClient.htm)|
Описание объекта для управления процессами WorkflowEngine с клиента  
[IWorkflowEngineProcessRequest](T_Tessa_Workflow_IWorkflowEngineProcessRequest.htm)|
Запрос на обработку процесса WorkflowEngine.  
[IWorkflowEngineProcessResult](T_Tessa_Workflow_IWorkflowEngineProcessResult.htm)|
Результат обработки сигнала в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)  
[IWorkflowEngineProcessSerializer](T_Tessa_Workflow_IWorkflowEngineProcessSerializer.htm)|
Объект для сериализации и десериализации карточек процесса Workflow Engine  
[IWorkflowEngineTileCache](T_Tessa_Workflow_IWorkflowEngineTileCache.htm)|
Объект для получения и кеширования информации о тайлах бизнес-процессов.  
[IWorkflowEngineTileManager](T_Tessa_Workflow_IWorkflowEngineTileManager.htm)|
Объект, который производит получение доступных кнопок процесса и производит
проверку доступа к ним  
[IWorkflowEngineTileManagerExtension](T_Tessa_Workflow_IWorkflowEngineTileManagerExtension.htm)|
Расширение прав доступа к тайлам WorkflowEngine, проверяемым в
[IWorkflowEngineTileManager](T_Tessa_Workflow_IWorkflowEngineTileManager.htm).
Регистрируются через
[IWorkflowEngineTileManagerExtensionRegistry](T_Tessa_Workflow_IWorkflowEngineTileManagerExtensionRegistry.htm).  
[IWorkflowEngineTileManagerExtensionRegistry](T_Tessa_Workflow_IWorkflowEngineTileManagerExtensionRegistry.htm)|
Описывает реестр типов расширений доступа к тайлам WorkflowEngine
[IWorkflowEngineTileManagerExtension](T_Tessa_Workflow_IWorkflowEngineTileManagerExtension.htm).  
[IWorkflowHashBinder](T_Tessa_Workflow_IWorkflowHashBinder.htm)|  Описывает
объект, осуществляющего связь значений хеша со значениями в секциях карточки.  
[IWorkflowInstanceService](T_Tessa_Workflow_IWorkflowInstanceService.htm)|
Сервис для управления экземплярами и подписками Бизнес-процесса  
[IWorkflowService](T_Tessa_Workflow_IWorkflowService.htm)|  Сервис для
управления шаблонами, экземплярами и подписками Бизнес-процесса  
## __Перечисления
[WorkflowEngineProcessFlags](T_Tessa_Workflow_WorkflowEngineProcessFlags.htm)|
Настройки обработки процесса в
[IWorkflowEngineProcessor](T_Tessa_Workflow_IWorkflowEngineProcessor.htm)  
---|---
