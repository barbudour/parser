# Tessa.Cards.Numbers - пространство имён
API для организации нумерации карточек.
##  __Классы
[CardNumberLocation](T_Tessa_Cards_Numbers_CardNumberLocation.htm)|
Информация о местоположении полей с номерами в карточке, а именно о названиях
секций и полей, в которых расположены номера.  
---|---  
[DefaultNumberQueueProcessor](T_Tessa_Cards_Numbers_DefaultNumberQueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди с номерами.  
[NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm)|  Базовый класс для
объекта, осуществляющего низкоуровневые действия с номерами, которые зависят
от бизнес-логики.  
[NumberBuilderParameters](T_Tessa_Cards_Numbers_NumberBuilderParameters.htm)|
Известные платформе параметры, используемые для передачи в метод
[GetAsync<T>(INumberContext, Object,
CancellationToken)](M_Tessa_Cards_Numbers_INumberBuilder_GetAsync__1.htm) для
получения результатов.  
[NumberCardRequestTypes](T_Tessa_Cards_Numbers_NumberCardRequestTypes.htm)|
Типы стандартных запросов к сервису карточек через метод
[RequestAsync(CardRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_RequestAsync.htm),
используемый в API номеров.  
[NumberComposer](T_Tessa_Cards_Numbers_NumberComposer.htm)|  Объект,
обрабатывающий логику выделения и изменения номеров карточек, с реализацией по
умолчанию.  
[NumberComposerDependencies](T_Tessa_Cards_Numbers_NumberComposerDependencies.htm)|
Объект, содержащий зависимости стандартных классов, реализующих
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm). Классы-
наследники могут добавить дополнительные свойства, специфичные, например, для
типов карточек.  
[NumberContext](T_Tessa_Cards_Numbers_NumberContext.htm)|  Контекст события,
происходящего с номером, о котором уведомляется объект
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
[NumberContextActionKeys](T_Tessa_Cards_Numbers_NumberContextActionKeys.htm)|
Названия действий с номерами, устанавливаемых в контексте
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) посредством метода
[SetNumberAction(INumberContext, String, Func<INumberContext, INumberObject,
CancellationToken,
ValueTask>)](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberAction.htm) и
выполняемых посредством метода [ExecuteNumberActionAsync(INumberContext,
String, INumberObject,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm).
Обычно такие действия используются для обратной связи с элементом управления
номерами.  
[NumberContextEventArgs](T_Tessa_Cards_Numbers_NumberContextEventArgs.htm)|
Аргументы события, связанного с действием с номером.  
[NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)|
Запрос на выполнение действий через элемент управления "Нумератор".  
[NumberControlRequestExtension](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)|
Базовый класс для расширений, связанных с выполнением действия для контрола
"Нумератор".  
[NumberControlResponse](T_Tessa_Cards_Numbers_NumberControlResponse.htm)|
Ответ на запрос на выполнение действий через элемент управления "Нумератор".  
[NumberDependencies](T_Tessa_Cards_Numbers_NumberDependencies.htm)|  Объект,
содержащий внешние зависимости API номеров, которые обычно требуются для
построения таких объектов, как
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm) и
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm). Каждый экземпляр
создаваемого из Unity объекта должен получить свой экземпляр объекта с
зависимостями.  
[NumberDirector](T_Tessa_Cards_Numbers_NumberDirector.htm)|  Объект,
управляющий взаимодействием с номерами карточек, с реализацией по умолчанию.  
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)|  Базовый
объект, реализующий произвольное взаимодействие с номерами карточек.
Предназначен для реализации интерфейсов наподобие
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
[NumberDirectorContainer](T_Tessa_Cards_Numbers_NumberDirectorContainer.htm)|
Объект, выполняющий регистрацию и предоставляющий доступ к подсистеме номеров
для типов карточек, включая объекты
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).  
[NumberEventContainer<T>](T_Tessa_Cards_Numbers_NumberEventContainer_1.htm)|
Класс-контейнер, позволяющий получить результат ссылочного типа события,
происходящего с номером, которое передаётся в метод
[NotifyOnEventAsync(INumberContext, NumberEventType, Func<INumberContext,
CancellationToken, Task<Boolean>>, Func<INumberContext, CancellationToken,
Task<Boolean>>,
CancellationToken)](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventAsync.htm).  
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)|  Тип события,
происходящего с номером.  
[NumberEventTypeRegistry](T_Tessa_Cards_Numbers_NumberEventTypeRegistry.htm)|
Реестр типов действий с номерами
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm). Класс является
синглтоном.  
[NumberEventTypes](T_Tessa_Cards_Numbers_NumberEventTypes.htm)|  Стандартные
типы действий с номерами.  
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm)|  Базовый
объект, выполняющий расширяемые действия с номером.  
[NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm)|  Методы-
расширения для пространства имён Tessa.Cards.Numbers.  
[NumberHelper](T_Tessa_Cards_Numbers_NumberHelper.htm)|  Вспомогательные
методы для API управления номерами.  
[NumberLocation](T_Tessa_Cards_Numbers_NumberLocation.htm)|  Информация по
местоположению номера в карточке или в контексте события, происходящего с
номером.  
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm)|  Тип
местоположения номера (в карточке или в контексте события, происходящего с
номером).  
[NumberLocationTypeRegistry](T_Tessa_Cards_Numbers_NumberLocationTypeRegistry.htm)|
Реестр типов местоположений номеров
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm). Класс
является синглтоном.  
[NumberLocationTypes](T_Tessa_Cards_Numbers_NumberLocationTypes.htm)|
Стандартные типы местоположений номеров.  
[NumberObject](T_Tessa_Cards_Numbers_NumberObject.htm)|  Объект, определяющий
свойства номера и средства его хранения.  
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm)|  Очередь действий с
номерами, отложенных для выполнения на сервере.  
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm)|  Тип
события, происходящего с номером, в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueueActionTypeRegistry](T_Tessa_Cards_Numbers_NumberQueueActionTypeRegistry.htm)|
Реестр типов действий с номерами в очереди
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm).
Класс является синглтоном.  
[NumberQueueActionTypes](T_Tessa_Cards_Numbers_NumberQueueActionTypes.htm)|
Стандартные типы действий с номерами в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm)|  Тип
события по вызову действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueueEventTypeRegistry](T_Tessa_Cards_Numbers_NumberQueueEventTypeRegistry.htm)|
Реестр типов событий
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm) по
вызову действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm). Класс является
синглтоном.  
[NumberQueueEventTypes](T_Tessa_Cards_Numbers_NumberQueueEventTypes.htm)|
Стандартные типы событий по вызову действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)|  Действие с
номером в очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm)|
Тип предиката, применимого к действиям с номерами
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm). Предикат
эффективен для всех стандартных типов действий, а также для тех типов, в
которых явно прописана обработка предиката.  
[NumberQueuePredicateTypeRegistry](T_Tessa_Cards_Numbers_NumberQueuePredicateTypeRegistry.htm)|
Реестр типов предикатов
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm).
Класс является синглтоном.  
[NumberQueuePredicateTypes](T_Tessa_Cards_Numbers_NumberQueuePredicateTypes.htm)|
Стандартные типы предикатов, применимых к действиям с номерами
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm) в
очереди [NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[NumberQueueProcessor](T_Tessa_Cards_Numbers_NumberQueueProcessor.htm)|
Базовый класс для объекта, выполняющего обработку действий в очереди с
номерами.  
[NumberStorageLocation](T_Tessa_Cards_Numbers_NumberStorageLocation.htm)|
Объект, сохраняющий информацию по местоположению номера в карточке
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm).  
[NumberStorageObject](T_Tessa_Cards_Numbers_NumberStorageObject.htm)|  Объект,
сохраняющий информацию по номеру
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm).  
[NumberStorageTypeDescriptor](T_Tessa_Cards_Numbers_NumberStorageTypeDescriptor.htm)|
Объект, сохраняющий информацию по типу номера с дополнительной информацией
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm).  
[NumberType](T_Tessa_Cards_Numbers_NumberType.htm)|  Тип номера.  
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)|  Тип
номера и дополнительная информация по способу его использования. Наследники
класса могут определять такую информация в строго типизированных свойствах, в
остальных случаях она указывается в
[Info](P_Tessa_Cards_Numbers_NumberTypeDescriptor_Info.htm).  
[NumberTypeRegistry](T_Tessa_Cards_Numbers_NumberTypeRegistry.htm)|  Реестр
типов номеров [NumberType](T_Tessa_Cards_Numbers_NumberType.htm). Класс
является синглтоном.  
[NumberTypes](T_Tessa_Cards_Numbers_NumberTypes.htm)|  Стандартные типы
номеров.  
[NumberValidateThat](T_Tessa_Cards_Numbers_NumberValidateThat.htm)|  Предикаты
для валидации значений в объектах, связанных со стандартным API номеров.  
## __Интерфейсы
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm)|  Объект,
осуществляющий низкоуровневые действия с номерами, которые зависят от бизнес-
логики.  
---|---  
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm)|  Объект,
обрабатывающий логику выделения и изменения номеров карточек.  
[INumberComposerDependencies](T_Tessa_Cards_Numbers_INumberComposerDependencies.htm)|
Объект, содержащий зависимости стандартных классов, реализующих
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm).  
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)|  Контекст события,
происходящего с номером, о котором уведомляется объект
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
[INumberDependencies](T_Tessa_Cards_Numbers_INumberDependencies.htm)|  Объект,
содержащий внешние зависимости API номеров, которые обычно требуются для
построения таких объектов, как
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm) и
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm). Каждый экземпляр
создаваемого из Unity объекта должен получить свой экземпляр объекта с
зависимостями.  
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm)|  Объект,
управляющий взаимодействием с номерами карточек.  
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm)|  Базовый
интерфейс для объектов, реализующих произвольное взаимодействие с номерами
карточек.  
[INumberDirectorContainer](T_Tessa_Cards_Numbers_INumberDirectorContainer.htm)|
Объект, выполняющий регистрацию и предоставляющий доступ к подсистеме номеров
для типов карточек, включая объекты
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).  
[INumberDirectorProvider](T_Tessa_Cards_Numbers_INumberDirectorProvider.htm)|
Объект, предоставляющий доступ к подсистеме номеров для типов карточек,
включая объекты [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm),
[INumberComposer](T_Tessa_Cards_Numbers_INumberComposer.htm) и
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm).  
[INumberEventTypeRegistry](T_Tessa_Cards_Numbers_INumberEventTypeRegistry.htm)|
Реестр типов действий с номерами
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm).  
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm)|  Объект,
выполняющий расширяемые действия с номером.  
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)|  Информация по
местоположению номера в карточке или в контексте события, происходящего с
номером.  
[INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm)|
Объект, определяющий поведение объекта
[INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm).  
[INumberLocationTypeRegistry](T_Tessa_Cards_Numbers_INumberLocationTypeRegistry.htm)|
Реестр типов местоположений номеров
[NumberLocationType](T_Tessa_Cards_Numbers_NumberLocationType.htm).  
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)|  Объект,
определяющий свойства номера и средства его хранения.  
[INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm)|
Объект, определяющий поведение объекта
[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm).  
[INumberQueueActionTypeRegistry](T_Tessa_Cards_Numbers_INumberQueueActionTypeRegistry.htm)|
Реестр типов действий с номерами в очереди
[NumberQueueActionType](T_Tessa_Cards_Numbers_NumberQueueActionType.htm).  
[INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)|
Объект, предоставляющий доступ к очереди действий с номерами.  
[INumberQueueEventTypeRegistry](T_Tessa_Cards_Numbers_INumberQueueEventTypeRegistry.htm)|
Реестр типов событий
[NumberQueueEventType](T_Tessa_Cards_Numbers_NumberQueueEventType.htm) по
вызову действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm).  
[INumberQueuePredicateTypeRegistry](T_Tessa_Cards_Numbers_INumberQueuePredicateTypeRegistry.htm)|
Реестр типов предикатов
[NumberQueuePredicateType](T_Tessa_Cards_Numbers_NumberQueuePredicateType.htm).  
[INumberQueueProcessor](T_Tessa_Cards_Numbers_INumberQueueProcessor.htm)|
Объект, выполняющий обработку действий в очереди с номерами.  
[INumberTypeRegistry](T_Tessa_Cards_Numbers_INumberTypeRegistry.htm)|  Реестр
типов номеров [NumberType](T_Tessa_Cards_Numbers_NumberType.htm).  
## __Делегаты
[NumberQueuePredicateFuncAsync](T_Tessa_Cards_Numbers_NumberQueuePredicateFuncAsync.htm)|
Функция, возвращающая признак того, что обработка действия с номером в очереди
[NumberQueue](T_Tessa_Cards_Numbers_NumberQueue.htm) разрешена.  
---|---  
[NumberQueueProcessFuncAsync](T_Tessa_Cards_Numbers_NumberQueueProcessFuncAsync.htm)|
Функция, выполняющая обработку действия с номером и возвращающая признак того,
что обработка выполнена удачно.  
## __Перечисления
[NumberContextInitializationFlags](T_Tessa_Cards_Numbers_NumberContextInitializationFlags.htm)|
Флаги, определяющие результат инициализации контекста события, происходящего с
номером.  
---|---  
[NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)|  Способ
сохранения номера [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm) в
карточке.  
[NumberTransactionMode](T_Tessa_Cards_Numbers_NumberTransactionMode.htm)|
Способ выполнения запросов, связанных с номерами. Определяет наличие
транзакций в различных запросах. При использовании API номеров на клиенте эта
настройка игнорируется.
