# KrScope - класс
Объект, предоставляющий методы для работы с текущим контекстом подсистемы
маршрутов, содержащим разделяемые карточки.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrProcess.Scope](N_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrScope : IKrScope
VB __Копировать
     Public NotInheritable Class KrScope
    	Implements IKrScope
C++ __Копировать
     public ref class KrScope sealed : IKrScope
F# __Копировать
     [<SealedAttribute>]
    type KrScope = 
        class
            interface IKrScope
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrScope
Implements
    [IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm)
##  __Конструкторы
[KrScope](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope__ctor.htm)|
Инициализирует новый экземпляр класса KrScope  
---|---  
##  __Свойства
[CurrentLevel](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_CurrentLevel.htm)|
Текущий уровень контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm)
или значение null, если код вызван вне контекста.  
---|---  
[Depth](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_Depth.htm)|
Количество уровней в текущем контексте
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[Exists](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_Exists.htm)|
Значение, показывающее, что текущий код выполняется внутри операции с
контекстом
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_Info.htm)|
Хранилище произвольных данных с областью видимости на текущий и вложенные
запросы.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_ValidationResult.htm)|
Результат валидации операций, производимых в текущем контексте
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).
Извне писать в это свойство не рекомендуется.  
## __Методы
[AddCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_AddCard.htm)|
Добавляет указанную карточку в контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
---|---  
[AddCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_AddCardFileContainer.htm)|
Добавляет указанный контейнер
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm) в контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[AddDisposableObject(IAsyncDisposable)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_AddDisposableObject.htm)|
Добавляет объект, освобождение ресурсов которого будет выполнено при
выполнении
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) этого объекта.  
[AddDisposableObject(IDisposable)](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_AddDisposableObject_1.htm)|
Добавляет объект, освобождение ресурсов которого будет выполнено при
выполнении
[DisposeAsync()](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync) этого объекта.  
[AddProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_AddProcessHolder.htm)|
Добавляет
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
в текущий контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[CardIsLoaded](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_CardIsLoaded.htm)|
Проверяет, загружена ли карточка с заданным идентификатором или нет.  
[CreateSecondaryKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_CreateSecondaryKrSatelliteAsync.htm)|
Создаёт и сохраняет сателлит вторичного процесса.  
[EnsureMainCardHasTaskHistoryAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_EnsureMainCardHasTaskHistoryAsync.htm)|
Загружает историю заданий для карточки с указанным идентификатором загруженной
в
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).
По умолчанию история заданий не загружается.  
[EnterNewLevel](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_EnterNewLevel.htm)|
Создаёт новый уровень контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ForceIncrementMainCardVersion](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_ForceIncrementMainCardVersion.htm)|
Планирует увеличение версии карточки с заданным идентификатором.  
[GetCurrentHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetCurrentHistoryGroupAsync.htm)|
Возвращает текущую группу истории заданий для указанной карточки, чей
контекстуальный сателлит находится в текущем
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[GetForceIncrementCardVersion](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetForceIncrementCardVersion.htm)|
Возвращает признак, показывающий, нужно ли увеличить версию карточки с
заданным идентификатором.  
[GetForceIncrementCardVersionIdentifiers](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetForceIncrementCardVersionIdentifiers.htm)|
Возвращает список идентификаторов карточек, для которых должна быть
принудительно увеличена версия.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetKrSatelliteAsync.htm)|
Возвращает основной сателлит процесса
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
для заданной карточки. При наличии изменений сателлит будет сохранен в
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).  
Если контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm)
не существует, то сателлит будет загружен явно, дальнейшее отслеживание
производиться не будет.  
Если сателлит не существует, то создаёт его.  
[GetLoadedCards](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetLoadedCards.htm)|
Возвращает список загруженных карточек.  
[GetLockedCardIDs](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetLockedCardIDs.htm)|
Возвращает идентификаторы заблокированных карточек.  
[GetMainCardAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetMainCardAsync.htm)|
Возвращает карточку с указанным идентификатором. При загрузке карточки
исключается следующая информация:
[RestrictTasks](T_Tessa_Cards_CardGetRestrictionFlags.htm) и
[RestrictTaskHistory](T_Tessa_Cards_CardGetRestrictionFlags.htm).  
[GetMainCardFileContainerAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetMainCardFileContainerAsync.htm)|
Возвращает файловый контейнер для карточки.  
[GetProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetProcessHolder.htm)|
Возвращает
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
из текущего контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[GetSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetSatelliteAsync.htm)|
Возвращает карточку сателлита.  
[GetSecondaryKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_GetSecondaryKrSatelliteAsync.htm)|
Возвращает существующий сателлит вторичного процесса.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_InvalidateAsync.htm)|
Сбрасывает все загруженные объекты.  
[IsCardLocked](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_IsCardLocked.htm)|
Возвращает признак, показывающий, что карточка с указанным идентификатором
заблокирована для сохранения.  
[LockCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_LockCard.htm)|
Блокирует карточку для сохранения. Если карточка заблокирована, то при выходе
с уровня сохранение произведено не будет.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[PopCurrentLevel](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_PopCurrentLevel.htm)|
Удаляет и возвращает текущий уровень контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[ReleaseCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_ReleaseCard.htm)|
Снимает блокировку с карточки на сохранение.  
[RemoveProcessHolder](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_RemoveProcessHolder.htm)|
Удаляет
[ProcessHolder](T_Tessa_Extensions_Default_Server_Workflow_KrObjectModel_ProcessHolder.htm)
из текущего контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[SetCurrentHistoryGroupAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_SetCurrentHistoryGroupAsync.htm)|
Устанавливает новую группу истории заданий для указанной карточки, чей
контекстуальный сателлит находится в текущем KrScope.  
[StoreSatelliteExplicitlyAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_StoreSatelliteExplicitlyAsync.htm)|
Выполняет явное сохранение сателлита. В общем случае является избыточным и не
рекомендуется.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetKrSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_TryGetKrSatelliteAsync.htm)|
Возвращает основной сателлит процесса
([KrSatelliteTypeID](F_Tessa_Extensions_Default_Shared_DefaultCardTypes_KrSatelliteTypeID.htm))
для заданной карточки. При наличии изменений сателлит будет сохранен в
[BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm).  
Если контекста
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm)
не существует, то сателлит будет загружен явно, дальнейшее отслеживание
производится не будет.  
[TryGetLoadedCard](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_TryGetLoadedCard.htm)|
Возвращает карточку, загруженную в контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[TryGetLoadedCardFileContainer](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_TryGetLoadedCardFileContainer.htm)|
Возвращает [ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm),
загруженный в контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[TryGetLoadedSatellite](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_TryGetLoadedSatellite.htm)|
Возвращает карточку сателлита, загруженную в контекст
[IKrScope](T_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_IKrScope.htm).  
[TryGetSatelliteAsync](M_Tessa_Extensions_Default_Server_Workflow_KrProcess_Scope_KrScope_TryGetSatelliteAsync.htm)|
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
