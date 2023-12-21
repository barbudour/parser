# NumberBuilder - класс
Базовый класс для объекта, осуществляющего низкоуровневые действия с номерами,
которые зависят от бизнес-логики.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class NumberBuilder : NumberExtendable, 
    	INumberBuilder, INumberObjectManager, INumberLocationManager, INumberQueueContainer
VB __Копировать
     Public MustInherit Class NumberBuilder
    	Inherits NumberExtendable
    	Implements INumberBuilder, INumberObjectManager, INumberLocationManager, INumberQueueContainer
C++ __Копировать
     public ref class NumberBuilder abstract : public NumberExtendable, 
    	INumberBuilder, INumberObjectManager, INumberLocationManager, INumberQueueContainer
F# __Копировать
     [<AbstractClassAttribute>]
    type NumberBuilder = 
        class
            inherit NumberExtendable
            interface INumberBuilder
            interface INumberObjectManager
            interface INumberLocationManager
            interface INumberQueueContainer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm) __ NumberBuilder
Derived
[Tessa.Cards.Numbers.NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
Implements
    [INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm), [INumberLocationManager](T_Tessa_Cards_Numbers_INumberLocationManager.htm), [INumberObjectManager](T_Tessa_Cards_Numbers_INumberObjectManager.htm), [INumberQueueContainer](T_Tessa_Cards_Numbers_INumberQueueContainer.htm)
##  __Конструкторы
[NumberBuilder](M_Tessa_Cards_Numbers_NumberBuilder__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[Dependencies](P_Tessa_Cards_Numbers_NumberBuilder_Dependencies.htm)| Объект,
содержащий внешние зависимости API номеров.  
---|---  
[PrimaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_PrimaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Primary](F_Tessa_Cards_Numbers_NumberLocationTypes_Primary.htm) для текущего
объекта.  
[SecondaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_SecondaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Secondary](F_Tessa_Cards_Numbers_NumberLocationTypes_Secondary.htm) для
текущего объекта.  
## __Методы
[CreateEmptyNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateEmptyNumberAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
---|---  
[CreateEmptyNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateEmptyNumberCoreAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
[CreateNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateNumberAsync.htm)|
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.  
[CreateNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateNumberCoreAsync.htm)|
Создаёт объект, описывающий номер с заданными параметрами. Номер может быть
пустым или не пустым в зависимости от параметров. Возвращённое значение не
может быть равно null.  
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
[FormatSequenceNameAsync](M_Tessa_Cards_Numbers_NumberBuilder_FormatSequenceNameAsync.htm)|
Форматирует имя последовательности по заданной строке форматирования.  
[Get<T>](M_Tessa_Cards_Numbers_NumberBuilder_Get__1.htm)|  Возвращает значение
поля в строковой секции карточки. Поле обязано присутствовать в секции.  
[GetAsync<T>](M_Tessa_Cards_Numbers_NumberBuilder_GetAsync__1.htm)| Возвращает
типизированные данные для контекста события, происходящего с номером.  
[GetCoreAsync<T>](M_Tessa_Cards_Numbers_NumberBuilder_GetCoreAsync__1.htm)|
Возвращает типизированные данные для контекста события, происходящего с
номером.  
[GetDefaultSequenceName](M_Tessa_Cards_Numbers_NumberBuilder_GetDefaultSequenceName.htm)|
Возвращает имя последовательности, рекомендуемое для организации номеров
карточек.  
[GetFullNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetFullNumberAsync.htm)|
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.  
[GetFullNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetFullNumberCoreAsync.htm)|
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
[GetNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberCoreAsync.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
[GetNumberFromCardLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetNumberFromCardLocationAsync.htm)|
Возвращает номер, расположенный в карточке в месте, указанном в параметре
cardLocation, или пустой номер, если номер пуст или его не удалось получить.
Метод не возвращает null.  
[GetPaddedNumber](M_Tessa_Cards_Numbers_NumberBuilder_GetPaddedNumber.htm)|
Возвращает строку, дополненную спереди нулями до заданного размера.  
[GetPlaceholderDateTimeUtc](M_Tessa_Cards_Numbers_NumberBuilder_GetPlaceholderDateTimeUtc.htm)|
Возвращает дату и время в формате UTC, используемую для подстановки в строке
для форматирования номера или имени последовательности. По умолчанию
возвращает текущую дату.  
[GetPlaceholderInfoAsync](M_Tessa_Cards_Numbers_NumberBuilder_GetPlaceholderInfoAsync.htm)|
Создаёт или возвращает объект с дополнительной информацией, необходимой при
обращении к API плейсхолдеров. Созданный объект кэшируется в контексте
context, чтобы для той же операции он мог повторно использоваться. Например,
если в операции форматируются и имя последовательности, и строковое
представление номера, то обе операции по форматированию получат один и тот же
объект с дополнительной информацией.  
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
[NotifyAfterEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyAfterEventCoreAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[NotifyBeforeEventCoreAsync](M_Tessa_Cards_Numbers_NumberExtendable_NotifyBeforeEventCoreAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm))  
[RemoveNumberQueueAsync](M_Tessa_Cards_Numbers_NumberBuilder_RemoveNumberQueueAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
[RemoveNumberQueueCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_RemoveNumberQueueCoreAsync.htm)|
Удаляет очередь действий с номерами для заданного контекста. Возвращает
признак того, что очередь была найдена и удалена. Возвращает false, если
очередь не была найдена.  
[ReplacePlaceholder](M_Tessa_Cards_Numbers_NumberBuilder_ReplacePlaceholder.htm)|
Заменяет плейсхолдеры в строке для форматирования номера или имени
последовательности и возвращает строку, содержащую заменённый плейсхолдер или
null, если плейсхолдер заменить не удалось. Неизвестные плейсхолдеры не
изменяются в результирующей строке номера.  
[StoreNumberAsync(INumberContext, INumberObject, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberAsync_1.htm)|
Сохраняет объект с номером в контексте и по местоположению, определяемому его
типом.  
[StoreNumberAsync(INumberContext, INumberObject, INumberLocation,
NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
[StoreNumberCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberCoreAsync.htm)|
Сохраняет объект с номером в заданном местоположении и контексте.  
[StoreNumberToCardLocation](M_Tessa_Cards_Numbers_NumberBuilder_StoreNumberToCardLocation.htm)|
Сохраняет номер в карточку в место, указанное в параметре cardLocation.
Возвращает false, если сохранить номер не удалось.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet<T>](M_Tessa_Cards_Numbers_NumberBuilder_TryGet__1.htm)|  Возвращает
значение поля в строковой секции карточки или значение по умолчанию для типа
T, если поле или секция отсутствуют.  
[TryGetNumberEffectiveLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
[TryGetNumberEffectiveLocationCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationCoreAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
[TryGetNumberLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberLocationAsync.htm)|
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.  
[TryGetNumberLocationCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberLocationCoreAsync.htm)|
Возвращает местоположение номера для заданного типа или null, если
местоположение не определено и действие с номером следует отменить.  
[TryGetNumberQueueAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberQueueAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
[TryGetNumberQueueCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberQueueCoreAsync.htm)|
Возвращает очередь действий с номерами для заданного контекста или null, если
очередь недоступна.  
[TryGetSequenceNameAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetSequenceNameAsync.htm)|
Возвращает имя последовательности, подходящее для заданного события,
происходящего с номером, или null, если последовательность недоступна и
операция будет считаться невыполненной.  
[TryGetSequenceNameCoreAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetSequenceNameCoreAsync.htm)|
Возвращает имя последовательности, подходящее для заданного события,
происходящего с номером, или null, если последовательность недоступна и
операция будет считаться невыполненной.  
## __События
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
##  __Методы расширения
[DereserveWhenTabIsClosedOrRefreshedAsync](M_Tessa_Cards_Numbers_NumberExtensions_DereserveWhenTabIsClosedOrRefreshedAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет
дерезервирование заданного номера number при закрытии вкладки карточки или при
её переоткрытии (например, в процессе сохранения).  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[GetNumberAsync](M_Tessa_Cards_Numbers_NumberExtensions_GetNumberAsync_1.htm)|
Возвращает номер, расположенный в заданных местоположении и контексте или
пустой номер, если он не был найден. Метод не возвращает null.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ReleaseAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReleaseAndCommitAtServerAsync.htm)|
Добавляет запись в очередь действий с номерами, которая вызовет освобождение
заданного номера number при сохранении карточки. Вторым параметром возвращает
действие, выполняемое для отмены операции по освобождению номера, или null,
если отсутствуют действия для отмены.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[ReserveAndCommitAtServerAsync](M_Tessa_Cards_Numbers_NumberExtensions_ReserveAndCommitAtServerAsync.htm)|
Резервирует номер заданного типа и добавляет запись в очередь действий с
номерами, которая вызовет выделение номера при сохранении карточки. Возвращает
зарезервированный номер или пустой номер, если зарезервировать номер не
удалось или в процессе выполнения произошли ошибки.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
