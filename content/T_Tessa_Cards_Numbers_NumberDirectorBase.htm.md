# NumberDirectorBase - класс
Базовый объект, реализующий произвольное взаимодействие с номерами карточек.
Предназначен для реализации интерфейсов наподобие
[INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NumberDirectorBase : NumberBuilder, 
    	INumberDirectorBase, INumberExtendable, ISealable
VB __Копировать
     Public MustInherit Class NumberDirectorBase
    	Inherits NumberBuilder
    	Implements INumberDirectorBase, INumberExtendable, ISealable
C++ __Копировать
     public ref class NumberDirectorBase abstract : public NumberBuilder, 
    	INumberDirectorBase, INumberExtendable, ISealable
F# __Копировать
     [<AbstractClassAttribute>]
    type NumberDirectorBase = 
        class
            inherit NumberBuilder
            interface INumberDirectorBase
            interface INumberExtendable
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm) __[NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm) __ NumberDirectorBase
Derived
[Tessa.Cards.Numbers.NumberDirector](T_Tessa_Cards_Numbers_NumberDirector.htm)
Implements
    [INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm), [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[NumberDirectorBase](M_Tessa_Cards_Numbers_NumberDirectorBase__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[AvailableEventTypes](P_Tessa_Cards_Numbers_NumberDirectorBase_AvailableEventTypes.htm)|
Доступные типы событий, происходящие с номерами. Изменение этой коллекции
позволяет отключить обработку некоторых событий для всех карточек, к которым
применим текущий объект.  
---|---  
[Dependencies](P_Tessa_Cards_Numbers_NumberBuilder_Dependencies.htm)| Объект,
содержащий внешние зависимости API номеров.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[IsSealed](P_Tessa_Cards_Numbers_NumberDirectorBase_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[PrimaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_PrimaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Primary](F_Tessa_Cards_Numbers_NumberLocationTypes_Primary.htm) для текущего
объекта.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[SecondaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_SecondaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Secondary](F_Tessa_Cards_Numbers_NumberLocationTypes_Secondary.htm) для
текущего объекта.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[UnavailableCardTypes](P_Tessa_Cards_Numbers_NumberDirectorBase_UnavailableCardTypes.htm)|
Идентификаторы типов карточек, система нумерации для которых принудительно
отключена.  
## __Методы
[CreateEmptyNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateEmptyNumberAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
---|---  
[CreateEmptyNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateEmptyNumberCoreAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[CreateNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateNumberAsync.htm)|
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[CreateNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateNumberCoreAsync.htm)|
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
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
[FormatNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_FormatNumberAsync.htm)|
Форматирует текстовое представление номера по заданной строке форматирования.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[FormatSequenceNameAsync](M_Tessa_Cards_Numbers_NumberBuilder_FormatSequenceNameAsync.htm)|
Форматирует имя последовательности по заданной строке форматирования.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetAsync<T>](M_Tessa_Cards_Numbers_NumberBuilder_GetAsync__1.htm)| Возвращает
типизированные данные для контекста события, происходящего с номером.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetBuilder](M_Tessa_Cards_Numbers_NumberDirectorBase_GetBuilder.htm)|
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.  
[GetBuilderCore](M_Tessa_Cards_Numbers_NumberDirectorBase_GetBuilderCore.htm)|
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.  
[GetCoreAsync<T>](M_Tessa_Cards_Numbers_NumberBuilder_GetCoreAsync__1.htm)|
Возвращает типизированные данные для контекста события, происходящего с
номером.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetFullNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetFullNumberAsync.htm)|
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetFullNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetFullNumberCoreAsync.htm)|
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberCoreAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetNumberFromCardLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberFromCardLocationAsync.htm)|
Возвращает номер, расположенный в карточке в месте, указанном в параметре
cardLocation, или пустой номер, если номер пуст или его не удалось получить.
Метод не возвращает null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetPlaceholderDateTimeUtc](M_Tessa_Cards_Numbers_NumberBuilder_GetPlaceholderDateTimeUtc.htm)|
Возвращает дату и время в формате UTC, используемую для подстановки в строке
для форматирования номера или имени последовательности. По умолчанию
возвращает текущую дату.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetPlaceholderInfoAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetPlaceholderInfoAsync.htm)|
Создаёт или возвращает объект с дополнительной информацией, необходимой при
обращении к API плейсхолдеров. Созданный объект кэшируется в контексте
context, чтобы для той же операции он мог повторно использоваться. Например,
если в операции форматируются и имя последовательности, и строковое
представление номера, то обе операции по форматированию получат один и тот же
объект с дополнительной информацией.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsAvailableAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_IsAvailableAsync.htm)|
Выполняет проверку доступности для типа события, происходящего с номером.  
[IsAvailableCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_IsAvailableCoreAsync.htm)|
Выполняет проверку доступности для типа события, происходящего с номером.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MethodReturnedNull](M_Tessa_Cards_Numbers_NumberExtendable_MethodReturnedNull.htm)|
Создаёт и возвращает исключение, которое вызывается в случае, когда
перегруженный виртуальный метод вернул null, хотя он не должен был возвращать
null.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyAfterEventCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyAfterEventCoreAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Переопределяет [NumberExtendable.NotifyAfterEventCoreAsync(INumberContext,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventCoreAsync.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyBeforeEventCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyBeforeEventCoreAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Переопределяет [NumberExtendable.NotifyBeforeEventCoreAsync(INumberContext,
CancellationToken)](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventCoreAsync.htm))  
[NotifyOnEventAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventAsync.htm)|
Выполняет заданное действие с номером.  
[NotifyOnEventCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventCoreAsync.htm)|
Выполняет заданное действие с номером.  
[RemoveNumberQueueAsync](M_Tessa_Cards_Numbers_NumberBuilder_RemoveNumberQueueAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[RemoveNumberQueueCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_RemoveNumberQueueCoreAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[ReplacePlaceholder](M_Tessa_Cards_Numbers_NumberBuilder_ReplacePlaceholder.htm)|
Заменяет плейсхолдеры в строке для форматирования номера или имени
последовательности и возвращает строку, содержащую заменённый плейсхолдер или
null, если плейсхолдер заменить не удалось. Неизвестные плейсхолдеры не
изменяются в результирующей строке номера.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[Seal](M_Tessa_Cards_Numbers_NumberDirectorBase_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Cards_Numbers_NumberDirectorBase_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[StoreNumberAsync(INumberContext, INumberObject, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberAsync_1.htm)|
Сохраняет объект с номером в контексте и по местоположению, определяемому его
типом.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[StoreNumberAsync(INumberContext, INumberObject, INumberLocation,
NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[StoreNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberCoreAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[StoreNumberToCardLocation](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberToCardLocation.htm)|
Сохраняет номер в карточку в место, указанное в параметре cardLocation.
Возвращает false, если сохранить номер не удалось.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetNumberEffectiveLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberEffectiveLocationCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationCoreAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberLocationAsync.htm)|
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberLocationCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberLocationCoreAsync.htm)|
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberQueueAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberQueueAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberQueueCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberQueueCoreAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetSequenceNameAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetSequenceNameAsync.htm)|
Возвращает имя последовательности, подходящее для заданного события,
происходящего с номером, или null, если последовательность недоступна и
операция будет считаться невыполненной.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetSequenceNameCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetSequenceNameCoreAsync.htm)|
Возвращает имя последовательности, подходящее для заданного события,
происходящего с номером, или null, если последовательность недоступна и
операция будет считаться невыполненной.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
##  __События
[AfterEvent](E_Tessa_Cards_Numbers_NumberExtendable_AfterEvent.htm)|  Событие,
выполняемое в процессе постобработки события, происходящего с номером. Это
предоставляет возможность изменить результат обработанного события или
сохранить результат во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
---|---  
[BeforeEvent](E_Tessa_Cards_Numbers_NumberExtendable_BeforeEvent.htm)|
Событие, выполняемое в процессе предварительной обработки события,
происходящего с номером. Это предоставляет возможность полностью заместить или
отменить стандартную обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
##  __Поля
[UnavailableCardTypesStatic](F_Tessa_Cards_Numbers_NumberDirectorBase_UnavailableCardTypesStatic.htm)|
Идентификаторы типов карточек, система нумерации для которых принудительно
отключена. Используется по умолчанию в переопределяемом свойстве
[UnavailableCardTypes](P_Tessa_Cards_Numbers_NumberDirectorBase_UnavailableCardTypes.htm).  
---|---  
## __Методы расширения
[EnsureAvailable](M_Tessa_Cards_Numbers_NumberExtensions_EnsureAvailable.htm)|
Гарантирует, что объект
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm) в
коллекции доступных типов событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
