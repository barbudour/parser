# NumberContext - класс
Контекст события, происходящего с номером, о котором уведомляется объект
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NumberContext : INumberContext, 
    	INumberDependencies, ISealable
VB __Копировать
     Public NotInheritable Class NumberContext
    	Implements INumberContext, INumberDependencies, ISealable
C++ __Копировать
     public ref class NumberContext sealed : INumberContext, 
    	INumberDependencies, ISealable
F# __Копировать
     [<SealedAttribute>]
    type NumberContext = 
        class
            interface INumberContext
            interface INumberDependencies
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NumberContext
Implements
    [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm), [INumberDependencies](T_Tessa_Cards_Numbers_INumberDependencies.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[NumberContext](M_Tessa_Cards_Numbers_NumberContext__ctor.htm)|  Создаёт
экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[Builder](P_Tessa_Cards_Numbers_NumberContext_Builder.htm)|  Объект,
осуществляющий низкоуровневые действия с номерами, которые зависят от бизнес-
логики. Если объект недоступен или уже был установлен, то выбрасывается
исключение [System.InvalidOperationException].  
---|---  
[CanCancel](P_Tessa_Cards_Numbers_NumberContext_CanCancel.htm)|  Признак того,
что свойство [Tessa.Cards.Numbers.INumberContext.Cancel] содержит информацию
об отмене действия и его значение можно изменить.  
[Cancel](P_Tessa_Cards_Numbers_NumberContext_Cancel.htm)|  Признак того, что
действие должно быть отменено для
[Tessa.Cards.Numbers.INumberExtendable.NotifyBeforeEventAsync] или было
отменено для [Tessa.Cards.Numbers.INumberExtendable.NotifyAfterEventAsync]. По
умолчанию свойство равно false.  
[CanChangeNumber](P_Tessa_Cards_Numbers_NumberContext_CanChangeNumber.htm)|
Признак того, что значение свойства
[Tessa.Cards.Numbers.INumberContext.NumberObject] можно изменить.  
[CanHandle](P_Tessa_Cards_Numbers_NumberContext_CanHandle.htm)|  Признак того,
что свойство [Tessa.Cards.Numbers.INumberContext.Handled] содержит информацию
об успешной обработке действия и его значение можно изменить.  
[Card](P_Tessa_Cards_Numbers_NumberContext_Card.htm)|
Карточка, для которой производится работа с номером.
В методе [Tessa.Cards.Numbers.INumberDirectorBase.IsAvailableAsync] для
события [Tessa.Cards.Numbers.NumberEventTypes.DeletingCardWithoutBackup] может
отсутствовать любая информация по карточке для оптимизации загрузки секций
удаляемой карточки. Поэтому в этом случае, если в карточке нет секций,
рекомендуется не выполнять никаких проверок. Метод будет позже вызван ещё раз
для того же действия.
Во всех остальных случаях для того, чтобы гарантировать успешную обработку в
расширениях, в карточке должны присутствовать системная информация и все
секции, но могут отсутствовать файлы и задания.  
[CardType](P_Tessa_Cards_Numbers_NumberContext_CardType.htm)| Тип карточки,
для которой будет производиться работа с номером.  
[Composer](P_Tessa_Cards_Numbers_NumberContext_Composer.htm)|  Объект,
обрабатывающий логику выделения и изменения номеров карточек. Если объект
недоступен или уже был установлен, то выбрасывается исключение
[System.InvalidOperationException].  
[ContextInfo](P_Tessa_Cards_Numbers_NumberContext_ContextInfo.htm)|  Доступная
только для чтения информация из внешнего контекста, используемая при обработке
события, происходящего с номером. Обычно в расширениях UI это ICardModel.Info,
а в других расширениях, связанных с карточками, это Info запроса.  
[DbScope](P_Tessa_Cards_Numbers_NumberContext_DbScope.htm)|  Объект,
предоставляющий доступ к базе данных, или null, если выполнение происходит без
доступа к базе данных, например, со стороны клиента.  
[Director](P_Tessa_Cards_Numbers_NumberContext_Director.htm)|  Объект,
управляющий взаимодействием с номерами карточек. Если объект недоступен или
уже был установлен, то выбрасывается исключение
[System.InvalidOperationException].  
[EventType](P_Tessa_Cards_Numbers_NumberContext_EventType.htm)|  Тип события,
происходящего с номером. Если событие не было установлено, то возвращается
[Tessa.Cards.Numbers.NumberEventTypes.Unknown]. Установить значение можно
единственный раз, причём нельзя установить null или
[Tessa.Cards.Numbers.NumberEventTypes.Unknown].  
[ExternalContext](P_Tessa_Cards_Numbers_NumberContext_ExternalContext.htm)|
Объект внешнего контекста, используемый при обработке события, происходящего с
номером.  
[Handled](P_Tessa_Cards_Numbers_NumberContext_Handled.htm)|  Признак того, что
действие было успешно обработано, если свойство
[Tessa.Cards.Numbers.INumberContext.CanHandle] возвращает true. В противном
случае значене равно false, что следует трактовать как "информация о
выполнении неизвестна".  
[HasBuilder](P_Tessa_Cards_Numbers_NumberContext_HasBuilder.htm)|  Признак
того, что объект [Tessa.Cards.Numbers.INumberContext.Builder] был задан, и
обращение к свойству не приведёт к исключению.  
[HasComposer](P_Tessa_Cards_Numbers_NumberContext_HasComposer.htm)|  Признак
того, что объект [Tessa.Cards.Numbers.INumberContext.Composer] был задан, и
обращение к свойству не приведёт к исключению.  
[HasDirector](P_Tessa_Cards_Numbers_NumberContext_HasDirector.htm)|  Признак
того, что объект [Tessa.Cards.Numbers.INumberContext.Director] был задан, и
обращение к свойству не приведёт к исключению.  
[HasEventType](P_Tessa_Cards_Numbers_NumberContext_HasEventType.htm)|  Признак
того, что объект [Tessa.Cards.Numbers.INumberContext.EventType] был задан, и
обращение к свойству вернёт действительное значение.  
[Info](P_Tessa_Cards_Numbers_NumberContext_Info.htm)|  Произвольно
структурированная информация, используемая при обработке события,
происходящего с номером.  
[IsSealed](P_Tessa_Cards_Numbers_NumberContext_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
[NumberObject](P_Tessa_Cards_Numbers_NumberContext_NumberObject.htm)| Объект,
определяющий свойства номера и средства его хранения.  
[PlaceholderInfo](P_Tessa_Cards_Numbers_NumberContext_PlaceholderInfo.htm)|
Информация, передаваемая в свойство IPlaceholderContext.Info при замене
плейсхолдеров в формате номера, формате последовательности или в других
случаях, когда для API номеров требуется задействовать API плейсхолдеров.  
[PlaceholderManager](P_Tessa_Cards_Numbers_NumberContext_PlaceholderManager.htm)|
Объект, управляющий операциями с плейсхолдерами.  
[RequestRepository](P_Tessa_Cards_Numbers_NumberContext_RequestRepository.htm)|
Репозиторий, используемый для построения универсальных запросов к API номеров
на сервере.  
[SerializableInfo](P_Tessa_Cards_Numbers_NumberContext_SerializableInfo.htm)|
Сериализуемая информация, которая может быть передана при обмене данными между
клиентом и сервером. Обычно это информация из методов, связанных с элементом
управления номерами, которую можно получить из сервера в клиентском
NumberControlResponse.Info. Запрещено использовать это свойство для хранения
несериализуемых объектов, т.к. это приведёт к ошибке при сериализации данных.  
[Session](P_Tessa_Cards_Numbers_NumberContext_Session.htm)| Сессия текущего
пользователя.  
[TransactionMode](P_Tessa_Cards_Numbers_NumberContext_TransactionMode.htm)|
Получает или задаёт способ выполнения запросов, связанных с номерами.  
[UnityContainer](P_Tessa_Cards_Numbers_NumberContext_UnityContainer.htm)|
Контейнер Unity, который может использоваться для получения дополнительных
зависимостей.  
[ValidationResult](P_Tessa_Cards_Numbers_NumberContext_ValidationResult.htm)|
Информация по результату события, происходящего с номером.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_Numbers_NumberContext_Seal.htm)| Защищает объект от
изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[ExecuteNumberActionAsync](M_Tessa_Cards_Numbers_NumberExtensions_ExecuteNumberActionAsync.htm)|
Выполняет ранее установленное действие с номером по заданному ключу. Если
действие не было установлено, то возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Initialize](M_Tessa_Cards_Numbers_NumberExtensions_Initialize.htm)|
Выполняет инициализацию свойств для контекста действий с номером, если они не
были инициализированы:
[Director](P_Tessa_Cards_Numbers_INumberContext_Director.htm),
[Builder](P_Tessa_Cards_Numbers_INumberContext_Builder.htm) и
[EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm). Инициализация
вызывается автоматически для вызова расширяемых методов
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetControl](M_Tessa_Cards_Numbers_NumberExtensions_SetControl.htm)|
Устанавливает в контексте элемент управления номерами, который инициировал
событие, происходящее с номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_SetControlLocation.htm)|
Устанавливает в контексте информацию по местоположению номера в карточке для
элемента управления номерами, который инициировал событие, происходящее с
номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetControlName](M_Tessa_Cards_Numbers_NumberExtensions_SetControlName.htm)|
Устанавливает в контексте имя элемента управления номерами, который
инициировал событие, происходящее с номером.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[SetNumberAction](M_Tessa_Cards_Numbers_NumberExtensions_SetNumberAction.htm)|
Устанавливает в контексте действие с номером, доступное по заданному ключу.
Значение null, переданное в параметр numberActionAsync, приводит к удалению
ранее заданного действия.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControl<T>](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControl__1.htm)|
Возвращает элемент управления номерами, который инициировал событие,
происходящее с номером, или null, если элемент управления неизвестен или если
его тип отличен от заданного.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControlLocation](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlLocation.htm)|
Возвращает информацию по местоположению номера в карточке для элемента
управления номерами, который инициировал событие, происходящее с номером, или
null, если местоположение неизвестно.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[TryGetControlName](M_Tessa_Cards_Numbers_NumberExtensions_TryGetControlName.htm)|
Возвращает имя (алиас) элемента управления номерами, который инициировал
событие, происходящее с номером, или null, если элемент управления неизвестен
или если его тип отличен от заданного.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
