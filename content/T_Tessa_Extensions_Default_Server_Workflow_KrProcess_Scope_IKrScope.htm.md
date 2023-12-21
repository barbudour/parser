# IKrScope - интерфейс
Объект, предоставляющий методы для работы с текущим контекстом подсистемы
маршрутов, содержащим разделяемые карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrScope
VB __Копировать
     Public Interface IKrScope
C++ __Копировать
     public interface class IKrScope
F# __Копировать
     type IKrScope = interface end
##  __Свойства
[CurrentLevel](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_CurrentLevel.htm)|
Текущий уровень контекста IKrScope или значение null, если код вызван вне
контекста.  
---|---  
[Depth](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_Depth.htm)|
Количество уровней в текущем контексте IKrScope.  
[Exists](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_Exists.htm)|
Значение, показывающее, что текущий код выполняется внутри операции с
контекстом IKrScope.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_Info.htm)|
Хранилище произвольных данных с областью видимости на текущий и вложенные
запросы.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_ValidationResult.htm)|
Результат валидации операций, производимых в текущем контексте IKrScope. Извне
писать в это свойство не рекомендуется.  
## __Методы
[AddCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_AddCard.htm)|
Добавляет указанную карточку в контекст IKrScope.  
---|---  
[AddCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_AddCardFileContainer.htm)|
Добавляет указанный контейнер
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm) в контекст
IKrScope.  
[AddDisposableObject(IAsyncDisposable)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_AddDisposableObject.htm)|
Добавляет объект, освобождение ресурсов которого будет выполнено при
выполнении
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) этого объекта.  
[AddDisposableObject(IDisposable)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_AddDisposableObject_1.htm)|
Добавляет объект, освобождение ресурсов которого будет выполнено при
выполнении
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) этого объекта.  
[AddProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_AddProcessHolder.htm)|
Добавляет
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
в текущий контекст IKrScope.  
[CardIsLoaded](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_CardIsLoaded.htm)|
Проверяет, загружена ли карточка с заданным идентификатором или нет.  
[CreateSecondaryKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_CreateSecondaryKrSatelliteAsync.htm)|
Создаёт и сохраняет сателлит вторичного процесса.  
[EnsureMainCardHasTaskHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_EnsureMainCardHasTaskHistoryAsync.htm)|
Загружает историю заданий для карточки с указанным идентификатором загруженной
в IKrScope. По умолчанию история заданий не загружается.  
[EnterNewLevel](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_EnterNewLevel.htm)|
Создаёт новый уровень контекста IKrScope.  
[ForceIncrementMainCardVersion](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_ForceIncrementMainCardVersion.htm)|
Планирует увеличение версии карточки с заданным идентификатором.  
[GetCurrentHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetCurrentHistoryGroupAsync.htm)|
Возвращает текущую группу истории заданий для указанной карточки, чей
контекстуальный сателлит находится в текущем IKrScope.  
[GetForceIncrementCardVersion](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetForceIncrementCardVersion.htm)|
Возвращает признак, показывающий, нужно ли увеличить версию карточки с
заданным идентификатором.  
[GetForceIncrementCardVersionIdentifiers](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetForceIncrementCardVersionIdentifiers.htm)|
Возвращает список идентификаторов карточек, для которых должна быть
принудительно увеличена версия.  
[GetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetKrSatelliteAsync.htm)|
Возвращает основной сателлит процесса
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
для заданной карточки. При наличии изменений сателлит будет сохранен в
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).  
Если контекста IKrScope не существует, то сателлит будет загружен явно,
дальнейшее отслеживание производиться не будет.  
Если сателлит не существует, то создаёт его.  
[GetLoadedCards](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetLoadedCards.htm)|
Возвращает список загруженных карточек.  
[GetLockedCardIDs](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetLockedCardIDs.htm)|
Возвращает идентификаторы заблокированных карточек.  
[GetMainCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetMainCardAsync.htm)|
Возвращает карточку с указанным идентификатором. При загрузке карточки
исключается следующая информация:
[RestrictTasks](T_Tessa_Cards_CardGetRestrictionFlags.htm) и
[RestrictTaskHistory](T_Tessa_Cards_CardGetRestrictionFlags.htm).  
[GetMainCardFileContainerAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetMainCardFileContainerAsync.htm)|
Возвращает файловый контейнер для карточки.  
[GetProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetProcessHolder.htm)|
Возвращает
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
из текущего контекста IKrScope.  
[GetSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetSatelliteAsync.htm)|
Возвращает карточку сателлита.  
[GetSecondaryKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_GetSecondaryKrSatelliteAsync.htm)|
Возвращает существующий сателлит вторичного процесса.  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_InvalidateAsync.htm)|
Сбрасывает все загруженные объекты.  
[IsCardLocked](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_IsCardLocked.htm)|
Возвращает признак, показывающий, что карточка с указанным идентификатором
заблокирована для сохранения.  
[LockCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_LockCard.htm)|
Блокирует карточку для сохранения. Если карточка заблокирована, то при выходе
с уровня сохранение произведено не будет.  
[PopCurrentLevel](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_PopCurrentLevel.htm)|
Удаляет и возвращает текущий уровень контекста IKrScope.  
[ReleaseCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_ReleaseCard.htm)|
Снимает блокировку с карточки на сохранение.  
[RemoveProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_RemoveProcessHolder.htm)|
Удаляет
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
из текущего контекста IKrScope.  
[SetCurrentHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_SetCurrentHistoryGroupAsync.htm)|
Устанавливает новую группу истории заданий для указанной карточки, чей
контекстуальный сателлит находится в текущем KrScope.  
[StoreSatelliteExplicitlyAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_StoreSatelliteExplicitlyAsync.htm)|
Выполняет явное сохранение сателлита. В общем случае является избыточным и не
рекомендуется.  
[TryGetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_TryGetKrSatelliteAsync.htm)|
Возвращает основной сателлит процесса
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
для заданной карточки. При наличии изменений сателлит будет сохранен в
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).  
Если контекста IKrScope не существует, то сателлит будет загружен явно,
дальнейшее отслеживание производится не будет.  
[TryGetLoadedCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_TryGetLoadedCard.htm)|
Возвращает карточку, загруженную в контекст IKrScope.  
[TryGetLoadedCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_TryGetLoadedCardFileContainer.htm)|
Возвращает [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm),
загруженный в контекст IKrScope.  
[TryGetLoadedSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_TryGetLoadedSatellite.htm)|
Возвращает карточку сателлита, загруженную в контекст IKrScope.  
[TryGetSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope_TryGetSatelliteAsync.htm)|
Возвращает карточку сателлита.  
## __Методы расширения
[AddLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_AddLaunchedRunner.htm)|
Добавляет информацию о том, что для указанного процесса запущен обработчик.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
---|---  
[AddToLaunchedLevels](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_AddToLaunchedLevels.htm)|
Добавляет информацию о запуске процесса в рамках запроса.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[DisableMultirunForRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_DisableMultirunForRequest.htm)|
Запрещает повторное выполнение процесса за запрос.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[FirstLaunchPerRequest](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_FirstLaunchPerRequest.htm)|
Возвращает значение, показывающее, что процесс с указанным идентификатором
запускается первый раз за запрос.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[GetKrProcessClientCommands](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetKrProcessClientCommands.htm)|
Возвращает список клиентских команд.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[GetKrProcessRunnerTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_GetKrProcessRunnerTrace.htm)|
Возвращает список, содержащий информацию по истории выполнения.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[GetRunnerState](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions_GetRunnerState.htm)|  
(Определяется
[KrProcessStateMachineExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions.htm))  
[HasLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_HasLaunchedRunner.htm)|
Возвращает значение, показывающее, запущен ли для указанного процесса раннер
или нет.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[IsDefaultProcessState](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions_IsDefaultProcessState.htm)|  
(Определяется
[KrProcessStateMachineExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions.htm))  
[MultirunEnabled](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_MultirunEnabled.htm)|
Возвращает значение, показывающее разрешено ли запускать процесс повторно за
запрос.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[RemoveLaunchedRunner](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_RemoveLaunchedRunner.htm)|
Удаляет информацию о том, что для указанного процесса запущен раннер.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[SetDefaultState](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions_SetDefaultState.htm)|  
(Определяется
[KrProcessStateMachineExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions.htm))  
[SetRunnerState](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions_SetRunnerState.htm)|  
(Определяется
[KrProcessStateMachineExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_StateMachine_KrProcessStateMachineExtensions.htm))  
[TryAddClientCommand](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryAddClientCommand.htm)|
Добавляет клиентскую команду, если список команд доступен.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[TryAddToTrace](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryAddToTrace.htm)|
Добавляет новую запись в историю выполнения процесса.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
[TryGetKrProcessClientCommands](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions_TryGetKrProcessClientCommands.htm)|
Возвращает список клиентских команд.  
(Определяется
[KrProcessExtensions](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Workflow_KrProcessExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)
