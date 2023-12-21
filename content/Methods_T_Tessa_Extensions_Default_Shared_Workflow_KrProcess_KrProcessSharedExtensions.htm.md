# KrProcessSharedExtensions - методы
##  __Методы
[AddKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AddKrProcessClientCommands.htm)|
Добавляет в указанное хранилище список клиентских команд.  
---|---  
[AreButtonsIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_AreButtonsIgnored.htm)|
Получает из заданного хранилища значение флага показывающего, что при загрузке
карточки не надо добавлять в ответ информацию по тайлам вторичных процессов.  
[ConsiderHiddenStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderHiddenStages.htm)|
Возвращает значение, показывающее, что в карточку должны быть загружены
скрытые этапы маршрута.  
[ConsiderSkippedStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_ConsiderSkippedStages.htm)|
Возвращает значение из заданного хранилища, показывающее, требуется ли
отображать пропущенные этапы.  
[DontHideSkippedStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideSkippedStages.htm)|
Устанавливает значение в заданном хранилище, показывающее, требуется ли
отображать пропущенные этапы.  
[DontHideStages(CardInfoStorageObject,
Boolean)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideStages_1.htm)|
Добавляет в указанное хранилище значение, показывающее, необходимо ли
загружать в карточку скрытые этапы маршрута или нет.  
[DontHideStages(IDictionary<String, Object>,
Boolean)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_DontHideStages.htm)|
Добавляет в указанный словарь значение, показывающее, необходимо ли загружать
в карточку скрытые этапы маршрута или нет.  
[GetActiveTasksSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetActiveTasksSection.htm)|
Возвращает секцию карточки содержащую активные задания.  
[GetApprovalInfoSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetApprovalInfoSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по процессу.  
[GetAsyncProcessCompletedSimultaniosly](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetAsyncProcessCompletedSimultaniosly.htm)|
Возвращает значение, показывающее, что асинхронный процесс был завершён.  
[GetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
[GetGlobalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetGlobalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
глобальных тайлах маршрутов.  
[GetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetHasRecalcChanges.htm)|
Возвращает значение, показывающее, что после пересчёта были изменения в
маршруте или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
[GetInfoAboutChanges(CardInfoStorageObject)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetInfoAboutChanges_1.htm)|
Возвращает режим вывода информации об изменениях в маршруте после пересчёта
или значение по умолчанию для типа, если хранилище его не содержало.  
[GetInfoAboutChanges(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetInfoAboutChanges.htm)|
Возвращает режим вывода информации об изменениях в маршруте после пересчёта
или значение по умолчанию для типа, если хранилище его не содержало.  
[GetKrApprovalHistorySection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrApprovalHistorySection.htm)|
Возвращает секцию карточки содержащую сопоставление истории заданий с историей
согласования (с учетом циклов согласования).  
[GetKrProcessClientCommands(CardInfoStorageObject)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessClientCommands_1.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
[GetKrProcessClientCommands(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessClientCommands.htm)|
Возвращает из указанной коллекции <ключ-значение> список клиентских команд или
значение по умолчанию для типа, если она их не содержала.  
[GetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
[GetKrProcessLaunchFullResult(CardResponse)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchFullResult.htm)|
Возвращает объект, содержащий результат запуска процесса, с заполненными
свойствами содержащими информацию по объекту его содержащему.  
[GetKrProcessLaunchFullResult(CardStoreResponse)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchFullResult_1.htm)|
Возвращает объект, содержащий результат запуска процесса, с заполненными
свойствами содержащими информацию по объекту его содержащему.  
[GetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetKrProcessLaunchResult.htm)|
Возвращает объект содержащий результат запуска процесса или значение по
умолчанию для типа, если указанный объект его не содержит.  
[GetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
[GetPerformersSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetPerformersSection.htm)|
Возвращает секцию карточки содержащей исполнителей этапов.  
[GetProcessInfoAtEnd](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetProcessInfoAtEnd.htm)|
Возвращает дополнительную информацию завершившегося асинхронного процесса.  
[GetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcChanges.htm)|
Возвращает информацию о различиях в маршруте до и после пересчёта.  
[GetRecalcFlag(CardInfoStorageObject)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcFlag_1.htm)|
Возвращает значение, показывающее, должен ли быть выполнен пересчёт маршрута
или нет.  
[GetRecalcFlag(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetRecalcFlag.htm)|
Возвращает значение, показывающее, должен ли быть выполнен пересчёт маршрута
или нет.  
[GetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStagePositions.htm)|
Возвращает информацию о позиции этапов.  
[GetStagesSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStagesSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по этапам процесса.  
[GetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
[GetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_GetStartingSecondaryProcess.htm)|
Возвращает из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса.  
[Has(InfoAboutChanges,
InfoAboutChanges)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_Has.htm)|  
[Has(KrComponents,
KrComponents)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_Has_1.htm)|  
[HasAny(InfoAboutChanges,
InfoAboutChanges)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasAny.htm)|  
[HasAny(KrComponents,
KrComponents)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasAny_1.htm)|  
[HasHiddenStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasHiddenStages.htm)|
Возвращает значение, показывающее, что в информации о позиции этапов
содержится информация о скрытых этапах.  
[HasNot(InfoAboutChanges,
InfoAboutChanges)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasNot.htm)|  
[HasNot(KrComponents,
KrComponents)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasNot_1.htm)|  
[HasSkipStages](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasSkipStages.htm)|
Возвращает значение, показывающее, наличие скрытых пропущенных этапов.  
[HasStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_HasStagePositions.htm)|
Возвращает значение, показывающее, что в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
содержится информация о позиции этапов.  
[IgnoreButtons](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreButtons.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
добавлять в ответ информацию по тайлам вторичных процессов.  
[IgnoreKrSatellite](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IgnoreKrSatellite.htm)|
Устанавливает значение, показывающее, что при загрузке карточки не надо
загружать и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
[IsKrSatelliteIgnored](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_IsKrSatelliteIgnored.htm)|
Возвращает значение, показывающее, что при загрузке карточки не надо загружать
и обрабатывать информацию содержащуюся в основном сателлите
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
карточки.  
[RemoveLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveLocalTiles.htm)|
Удаляет из заданного хранилища информацию по локальным тайлам маршрутов.  
[RemoveSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveSecondaryProcess.htm)|
Удаляет из объекта содержащего дополнительную информацию, информацию
необходимую для запуска процесса добавленную
[SetStartingSecondaryProcess(CardInfoStorageObject,
StartingSecondaryProcessInfo)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm).  
[RemoveStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_RemoveStagePositions.htm)|
Удаляет из
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
[SetAsyncProcessCompletedSimultaniosly](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetAsyncProcessCompletedSimultaniosly.htm)|
Устанавливает значение, показывающее, что асинхронный процесс был завершён.  
[SetGlobalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetGlobalTiles.htm)|
Сохраняет в указанном объекте коллекцию объектов содержащих информацию о
глобальных тайлах маршрутов.  
[SetHasRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetHasRecalcChanges.htm)|
Задаёт значение, показывающее, что после пересчёта были изменения в маршруте
или нет. Информация добавляется только при выставленном флаге
[HasChangesToInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrCompilers_InfoAboutChanges.htm).  
[SetIfDiffer<T>](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetIfDiffer__1.htm)|
Задаёт новое значение полю key в контейнере полей секции aci, если оно было
изменено.  
[SetInfoAboutChanges(CardInfoStorageObject,
InfoAboutChanges)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetInfoAboutChanges_1.htm)|
Устанавливает в хранилище информацию о режиме информирования об изменениях в
маршруте после пересчёта.  
[SetInfoAboutChanges(IDictionary<String, Object>,
InfoAboutChanges)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetInfoAboutChanges.htm)|
Устанавливает в хранилище информацию о режиме информирования об изменениях в
маршруте после пересчёта.  
[SetKrProcessInstance(CardInfoStorageObject,
KrProcessInstance)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessInstance_1.htm)|
Сохраняет в указанном объекте информация об экземпляре процесса.  
[SetKrProcessInstance(Dictionary<String, Object>,
KrProcessInstance)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessInstance.htm)|
Сохраняет в указанном объекте информация об экземпляре процесса.  
[SetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetKrProcessLaunchResult.htm)|
Сохраняет результаты запуска процесса в указанном хранилище.  
[SetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetLocalTiles.htm)|
Сохраняет в указанном объекте коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
[SetProcessInfoAtEnd](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetProcessInfoAtEnd.htm)|
Задаёт дополнительную информацию завершившегося асинхронного процесса в
указанном хранилище.  
[SetRecalcChanges](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcChanges.htm)|
Сохраняет в заданном хранилище информацию о различиях в маршруте до и после
пересчёта.  
[SetRecalcFlag(CardInfoStorageObject)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcFlag_1.htm)|
Задаёт значение, показывающее, что должен быть выполнен пересчёт маршрута.  
[SetRecalcFlag(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetRecalcFlag.htm)|
Задаёт значение, показывающее, что должен быть выполнен пересчёт маршрута.  
[SetStagePositions(Card,
List<Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStagePositions.htm)|
Задаёт в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
[SetStagePositions(Card,
List<KrStagePositionInfo>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStagePositions_1.htm)|
Задаёт в
[Card](T_Tessa_Cards_Card.htm).[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
информацию о позиции этапов.  
[SetStartingKrProcessParameters(CardInfoStorageObject, Dictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingKrProcessParameters_1.htm)|
Устанавливает параметры запускаемого процесса.  
[SetStartingKrProcessParameters(IDictionary<String, Object>,
Dictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingKrProcessParameters.htm)|
Устанавливает параметры запускаемого процесса.  
[SetStartingSecondaryProcess](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetStartingSecondaryProcess.htm)|
Устанавливает информацию о процессе, запускаемого посредством
[WorkflowStoreExtension](T_Tessa_Cards_Workflow_WorkflowStoreExtension.htm).  
[TryGetActiveTasksSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetActiveTasksSection.htm)|
Возвращает секцию карточки содержащую активные задания.  
[TryGetDocumentStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetDocumentStateNameAsync.htm)|
Возвращает название состояния в типовом решении по его идентификатору. Если
состояние не является стандартным, то значение запрашивается из метаданных
секции [!:KrDocState].  
[TryGetGlobalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetGlobalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
глобальных тайлах маршрутов.  
[TryGetKrApprovalCommonInfoSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrApprovalCommonInfoSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по процессу.  
[TryGetKrApprovalHistorySection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrApprovalHistorySection.htm)|
Возвращает секцию карточки содержащую сопоставление истории заданий с историей
согласования (с учетом циклов согласования).  
[TryGetKrProcessClientCommands](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessClientCommands.htm)|
Возвращает из указанного хранилища список клиентских команд или значение по
умолчанию для типа, если оно их не содержало.  
[TryGetKrProcessInstance](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessInstance.htm)|
Возвращает информацию об экземпляре процесса из указанного хранилища.  
[TryGetKrProcessLaunchResult](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetKrProcessLaunchResult.htm)|
Возвращает объект, содержащий результат запуска процесса.  
[TryGetLocalTiles](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetLocalTiles.htm)|
Получает из указанного объекта коллекцию объектов содержащих информацию о
локальных тайлах маршрутов.  
[TryGetPerformersSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetPerformersSection.htm)|
Возвращает секцию карточки содержащей исполнителей этапов.  
[TryGetStagePositions](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStagePositions.htm)|
Возвращает информацию о позиции этапов.  
[TryGetStagesSection](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStagesSection.htm)|
Возвращает секцию заданной карточки содержащую информацию по этапам процесса.  
[TryGetStageStateNameAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStageStateNameAsync.htm)|
Возвращает название состояния этапа. Если состояние не является стандартным,
то значение запрашивается из метаданных секции [!:KrConstants.KrStageState].  
[TryGetStartingKrProcessParameters(CardInfoStorageObject)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStartingKrProcessParameters_1.htm)|
Возвращает параметры запускаемого процесса.  
[TryGetStartingKrProcessParameters(IDictionary<String,
Object>)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_TryGetStartingKrProcessParameters.htm)|
Возвращает параметры запускаемого процесса.  
## __См. также
#### Ссылки
[KrProcessSharedExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
