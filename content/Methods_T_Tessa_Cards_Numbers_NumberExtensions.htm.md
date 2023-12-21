# NumberExtensions - методы
##  __Методы
[AcquireNumberByTypeAsync](M_Tessa_Cards_Numbers_NumberExtensions_AcquireNumberByTypeAsync.htm)|
Выделяет и возвращает номер, тип которого указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращённое значение не равно null, но может быть пустым в случае ошибки.  
---|---  
[AcquireReservedNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_AcquireReservedNumberAsync.htm)|
Выделяет зарезервированный ранее номер, который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно выделен.  
[CreateContext](M_Tessa_Cards_Numbers_NumberExtensions_CreateContext.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданным номером
и другими параметрами. После создания контекста номер нельзя изменить.  
[CreateContextAsync(INumberDirector, INumberComposer, Card, CardType,
Dictionary<String, Object>, Object, NumberTransactionMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_CreateContextAsync.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, принимая тип номера равным
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm). Этот метод может
использоваться для создания контекста с базовым состоянием для последующей
донастройки номера.  
[CreateContextAsync(INumberDirector, INumberComposer, Card, CardType,
NumberTypeDescriptor, Dictionary<String, Object>, Object,
NumberTransactionMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_CreateContextAsync_1.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами. Этот метод может использоваться для создания контекста с базовым
состоянием для последующей донастройки номера.  
[CreateInitializedContextAsync(INumberDirector, INumberComposer, Card,
CardType, Dictionary<String, Object>, Object, NumberTransactionMode,
NumberEventType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_CreateInitializedContextAsync.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, принимая тип номера равным
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm), а затем инициализирует
контекст с указанием типа события eventType.  
[CreateInitializedContextAsync(INumberDirector, INumberComposer, Card,
CardType, NumberTypeDescriptor, Dictionary<String, Object>, Object,
NumberTransactionMode, NumberEventType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_CreateInitializedContextAsync_1.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, а затем инициализирует контекст с указанием типа события
eventType.  
[DereserveWhenTabIsClosedOrRefreshedAsync](M_Tessa_Cards_Numbers_NumberExtensions_DereserveWhenTabIsClosedOrRefreshedAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет
дерезервирование заданного номера number при закрытии вкладки карточки или при
её переоткрытии (например, в процессе сохранения).  
[EnsureAvailable](M_Tessa_Cards_Numbers_NumberExtensions_EnsureAvailable.htm)|
Гарантирует, что объект
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm) в
коллекции доступных типов событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.  
[ExecuteNumberActionAsync](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm)|
Выполняет ранее установленное действие с номером по заданному ключу. Если
действие не было установлено, то возвращает false.  
[GetNumberAsync(INumberLocation, INumberContext, NumberTypeDescriptor,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
[GetNumberAsync(INumberLocationManager, INumberContext, NumberTypeDescriptor,
NumberLocationType,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync_1.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
[GetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberQueue.htm)|
Возвращает очередь действий с номерами, отложенных для выполнения на сервере
для текущей карточки. Если очередь отсутствует, то создаётся и возвращается
пустая очередь для этой карточки.  
[HasNumberQueueToProcess](M_Tessa_Cards_Numbers_NumberExtensions_HasNumberQueueToProcess.htm)|
Возвращает признак того, что в карточке присутствует непустая очередь для
обработки.  
[Initialize](M_Tessa_Cards_Numbers_NumberExtensions_Initialize.htm)|
Выполняет инициализацию свойств для контекста действий с номером, если они не
были инициализированы:
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm),
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm) и
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm). Инициализация
вызывается автоматически для вызова расширяемых методов
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
[IsKnown(NumberEventType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown.htm)|
Возвращает признак того, что тип события, происходящего с номером, является
известным для стандартного API.  
[IsKnown(NumberLocationType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown_1.htm)|
Возвращает признак того, что тип местоположения номера является известным для
стандартного API.  
[IsKnown(NumberQueueActionType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown_2.htm)|
Возвращает признак того, что тип действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) является известным для
стандартного API.  
[IsKnown(NumberQueueEventType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown_3.htm)|
Возвращает признак того, что тип события по вызову действия с номером в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) является
известным для стандартного API.  
[IsKnown(NumberQueuePredicateType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown_4.htm)|
Возвращает признак того, что тип предиката, применимого к действиям с номерами
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm), является
известным для стандартного API.  
[IsKnown(NumberType)](M_Tessa_Cards_Numbers_NumberExtensions_IsKnown_5.htm)|
Возвращает признак того, что тип номера является известным для стандартного
API.  
[IsRegistered(NumberEventType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered.htm)|
Возвращает признак того, что тип события, происходящего с номером,
зарегистрирован в реестре типов, который используется в стандартном API.  
[IsRegistered(NumberLocationType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered_1.htm)|
Возвращает признак того, что тип местоположения номера зарегистрирован в
реестре типов, который используется в стандартном API.  
[IsRegistered(NumberQueueActionType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered_2.htm)|
Возвращает признак того, что тип действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) зарегистрирован в реестре
типов, который используется в стандартном API.  
[IsRegistered(NumberQueueEventType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered_3.htm)|
Возвращает признак того, что тип события по вызову действия с номером в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) зарегистрирован в
реестре типов, который используется в стандартном API.  
[IsRegistered(NumberQueuePredicateType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered_4.htm)|
Возвращает признак того, что тип предиката, применимого к действиям с номерами
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm), зарегистрирован
в реестре типов, который используется в стандартном API.  
[IsRegistered(NumberType)](M_Tessa_Cards_Numbers_NumberExtensions_IsRegistered_5.htm)|
Возвращает признак того, что тип номера зарегистрирован в реестре типов,
который используется в стандартном API.  
[RefreshFullNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_RefreshFullNumberAsync.htm)|
Обновляет поле с полным номером
[FullNumber](P_Tessa_Cards_Numbers_INumberObject_FullNumber.htm) для заданного
номера, если номер является номером последовательности, и возвращает объект
номера с такими же данными, но другим полным номером, или возвращает тот же
номер, если он не является номером последовательности.  
[RegisterNumbers](M_Tessa_Cards_Numbers_NumberExtensions_RegisterNumbers.htm)|
Выполняет регистрацию API работы с номерами. Метод автоматически вызывается
при регистрации серверного или клиентского API по работе с карточками.  
[ReleaseAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReleaseAndCommitAtServerAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет освобождение
заданного номера number при сохранении карточки. Вторым параметром возвращает
действие, выполняемое для отмены операции по освобождению номера, или null,
если отсутствуют действия для отмены.  
[RemoveNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_RemoveNumberQueue.htm)|
Удаляет очередь действий с номерами для текущей карточки. Возвращает признак
того, что такая очередь присутствовала в карточке перед удалением.  
[ReserveAcquiredNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAcquiredNumberAsync.htm)|
Резервирует номер, который ранее мог быть выделен и который указан в объекте
context.[NumberObject](P_Tessa_Cards_Numbers_INumberContext_NumberObject.htm).
Возвращает признак того, что номер успешно зарезервирован.  
[ReserveAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAndCommitAtServerAsync.htm)|
Резервирует номер заданного типа и добавляет запись в очередь действий с
номерами, которая вызовет выделение номера при сохранении карточки. Возвращает
зарезервированный номер или пустой номер, если зарезервировать номер не
удалось или в процессе выполнения произошли ошибки.  
[SetControl](M_Tessa_Cards_Numbers_NumberExtensions_SetControl.htm)|
Устанавливает в контексте элемент управления номерами, который инициировал
событие, происходящее с номером.  
[SetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_SetControlLocation.htm)|
Устанавливает в контексте информацию по местоположению номера в карточке для
элемента управления номерами, который инициировал событие, происходящее с
номером.  
[SetControlName](M_Tessa_Cards_Numbers_NumberExtensions_SetControlName.htm)|
Устанавливает в контексте имя элемента управления номерами, который
инициировал событие, происходящее с номером.  
[SetNumberAction](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberAction.htm)|
Устанавливает в контексте действие с номером, доступное по заданному ключу.
Значение null, переданное в параметр numberActionAsync, приводит к удалению
ранее заданного действия.  
[SetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberQueue.htm)|
Устанавливает очередь действий с номерами для текущей карточки.  
[SetPredicateItemID](M_Tessa_Cards_Numbers_NumberExtensions_SetPredicateItemID.htm)|
Устанавливает идентификатор записи в очереди действий
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm), который будет
использоваться для предиката в текущей записи.  
[StoreAsync(INumberObject, INumberContext, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_2.htm)|
Сохраняет объект с номером в заданном контексте.  
[StoreAsync(INumberObject, INumberContext, INumberLocation, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
[StoreAsync(INumberObject, INumberContext, NumberLocationType,
NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_StoreAsync_1.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
[StoreNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
[ToCardNumberLocation](M_Tessa_Cards_Numbers_NumberExtensions_ToCardNumberLocation.htm)|
Преобразует местоположение номера
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm) типа
[Card](F_Tessa_Cards_Numbers_NumberLocationTypes_Card.htm) в объект
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm). Может
вернуть null, если преобразование не удалось.  
[TryGetControl<T>](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControl__1.htm)|
Возвращает элемент управления номерами, который инициировал событие,
происходящее с номером, или null, если элемент управления неизвестен или если
его тип отличен от заданного.  
[TryGetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlLocation.htm)|
Возвращает информацию по местоположению номера в карточке для элемента
управления номерами, который инициировал событие, происходящее с номером, или
null, если местоположение неизвестно.  
[TryGetControlName](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlName.htm)|
Возвращает имя (алиас) элемента управления номерами, который инициировал
событие, происходящее с номером, или null, если элемент управления неизвестен
или если его тип отличен от заданного.  
[TryGetNumberQueue](M_Tessa_Cards_Numbers_NumberExtensions_TryGetNumberQueue.htm)|
Возвращает очередь действий с номерами, отложенных для выполнения на сервере
для текущей карточки, или null, если для текущей карточки очередь ещё не была
создана.  
[TryGetPredicateItemID](M_Tessa_Cards_Numbers_NumberExtensions_TryGetPredicateItemID.htm)|
Возвращает идентификатор записи в очереди действий
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm), который
используется для предиката в текущей записи, или null, если идентификатор не
был установлен или был установлен как null.  
## __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
