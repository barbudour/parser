# NumberDirector - класс
Объект, управляющий взаимодействием с номерами карточек, с реализацией по
умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class NumberDirector : NumberDirectorBase, 
    	INumberDirector, INumberDirectorBase, INumberExtendable, ISealable
VB __Копировать
     Public Class NumberDirector
    	Inherits NumberDirectorBase
    	Implements INumberDirector, INumberDirectorBase, INumberExtendable, ISealable
C++ __Копировать
     public ref class NumberDirector : public NumberDirectorBase, 
    	INumberDirector, INumberDirectorBase, INumberExtendable, ISealable
F# __Копировать
     type NumberDirector = 
        class
            inherit NumberDirectorBase
            interface INumberDirector
            interface INumberDirectorBase
            interface INumberExtendable
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NumberExtendable](T_Tessa_Cards_Numbers_NumberExtendable.htm) __[NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm) __[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm) __ NumberDirector
Derived
[Tessa.Extensions.Default.Shared.Numbers.DocumentNumberDirector](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
Implements
    [INumberDirector](T_Tessa_Cards_Numbers_INumberDirector.htm), [INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm), [INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[NumberDirector](M_Tessa_Cards_Numbers_NumberDirector__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[AvailableEventTypes](P_Tessa_Cards_Numbers_NumberDirectorBase_AvailableEventTypes.htm)|
Доступные типы событий, происходящие с номерами. Изменение этой коллекции
позволяет отключить обработку некоторых событий для всех карточек, к которым
применим текущий объект.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
---|---  
[Dependencies](P_Tessa_Cards_Numbers_NumberBuilder_Dependencies.htm)| Объект,
содержащий внешние зависимости API номеров.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[IsSealed](P_Tessa_Cards_Numbers_NumberDirectorBase_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[PrimaryLocation](P_Tessa_Cards_Numbers_NumberDirector_PrimaryLocation.htm)|
Основное местоположение для номера в карточке.  
[PrimaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_PrimaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Primary](F_Tessa_Cards_Numbers_NumberLocationTypes_Primary.htm) для текущего
объекта.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[SecondaryLocation](P_Tessa_Cards_Numbers_NumberDirector_SecondaryLocation.htm)|
Дополнительное местоположение для номера в карточке.  
[SecondaryTypeLocation](P_Tessa_Cards_Numbers_NumberBuilder_SecondaryTypeLocation.htm)|
Местоположение номера, всегда соответствующее типу
[Secondary](F_Tessa_Cards_Numbers_NumberLocationTypes_Secondary.htm) для
текущего объекта.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[UnavailableCardTypes](P_Tessa_Cards_Numbers_NumberDirectorBase_UnavailableCardTypes.htm)|
Идентификаторы типов карточек, система нумерации для которых принудительно
отключена.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
##  __Методы
[BeforeClosingTabAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeClosingTabAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.ClosingTab].  
---|---  
[BeforeCreatingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeCreatingCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.CreatingCard].  
[BeforeDeletingBackupCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeDeletingBackupCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.DeletingBackupCard].  
[BeforeDeletingCardWithoutBackupAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeDeletingCardWithoutBackupAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.DeletingCardWithoutBackup].  
[BeforeDeregisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeDeregisteringCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.DeregisteringCard].  
[BeforeGettingDigestAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeGettingDigestAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.GettingDigest].  
[BeforeImportingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeImportingCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.ImportingCard].  
[BeforePreparingTemplateAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforePreparingTemplateAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.PreparingTemplate].  
[BeforeRegisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeRegisteringCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.RegisteringCard].  
[BeforeReleasingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeReleasingNumberFromControlAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.ReleasingNumberFromControl].  
[BeforeReservingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeReservingNumberFromControlAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.ReservingNumberFromControl].  
[BeforeSavingNewCardAsync](M_Tessa_Cards_Numbers_NumberDirector_BeforeSavingNewCardAsync.htm)|
Предикат, проверяющий предусловия и заполняющий контекст перед обработкой
события [NumberEventTypes.SavingNewCard].  
[CreateEmptyNumberAsync](M_Tessa_Cards_Numbers_NumberBuilder_CreateEmptyNumberAsync.htm)|
Создаёт объект, описывающий пустой номер заданного типа. Возвращённое значение
не может быть равно null.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
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
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[GetBuilderCore](M_Tessa_Cards_Numbers_NumberDirectorBase_GetBuilderCore.htm)|
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[GetCoreAsync<T>](M_Tessa_Cards_Numbers_NumberBuilder_GetCoreAsync__1.htm)|
Возвращает типизированные данные для контекста события, происходящего с
номером.  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[GetDigestAsync](M_Tessa_Cards_Numbers_NumberDirector_GetDigestAsync.htm)|
Возвращает Digest карточки по её номерам.  
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
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[IsAvailableCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_IsAvailableCoreAsync.htm)|
Выполняет проверку доступности для типа события, происходящего с номером.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
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
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
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
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[NotifyOnClosingTabAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnClosingTabAsync.htm)|
Уведомляет о том, что на стороне клиента закрывается вкладка с карточкой. При
этом может потребоваться освободить номер, если он был зарезервирован и ещё не
был занят.  
[NotifyOnCreatingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnCreatingCardAsync.htm)|
Уведомляет о том, что выполняется создание карточки (обычным способом или по
шаблону). При этом может потребоваться зарезервировать номер. Обычно
выполняется на этапе AfterRequest после создания карточки.  
[NotifyOnDeletingBackupCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnDeletingBackupCardAsync.htm)|
Уведомляет о том, что карточка окончательно удаляется, т.е. удаляется её
удалённая карточка [Tessa.Cards.CardHelper.DeletedTypeName]. При этом может
потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении удалённой карточки.  
[NotifyOnDeletingCardWithoutBackupAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnDeletingCardWithoutBackupAsync.htm)|
Уведомляет о том, что карточка удаляется без возможности восстановления. При
этом может потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении карточки без возможности восстановления.  
[NotifyOnDeregisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnDeregisteringCardAsync.htm)|
Уведомляет о том, что выполняется дерегистрация карточки. При этом может
потребоваться освободить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[NotifyOnEventAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventAsync.htm)|
Выполняет заданное действие с номером.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[NotifyOnEventCoreAsync](M_Tessa_Cards_Numbers_NumberDirectorBase_NotifyOnEventCoreAsync.htm)|
Выполняет заданное действие с номером.  
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[NotifyOnImportingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnImportingCardAsync.htm)|
Уведомляет о том, что карточка импортируется. При этом может потребоваться
занять номер, который был ранее занят. Обычно выполняется на этапе
BeforeCommitTransaction в транзакции на сохранение карточки.  
[NotifyOnPreparingTemplateAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnPreparingTemplateAsync.htm)|
Уведомляет о том, что карточка шаблона подготавливается к созданию по шаблону.
При этом может потребоваться очистить поля номеров, заданных в шаблоне. Обычно
выполняется на сервере на этапе AfterRequest после создания карточки, но перед
событием [Tessa.Cards.Numbers.NumberEventTypes.CreatingCard].  
[NotifyOnRegisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnRegisteringCardAsync.htm)|
Уведомляет о том, что выполняется регистрация карточки. При этом может
потребоваться выделить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[NotifyOnReleasingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnReleasingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется освобождение номера из элемента управления.  
[NotifyOnReservingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnReservingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется резервирование номера из элемента
управления.  
[NotifyOnSavingNewCardAsync](M_Tessa_Cards_Numbers_NumberDirector_NotifyOnSavingNewCardAsync.htm)|
Уведомляет о том, что карточка впервые сохраняется. При этом может
потребоваться выделить номер. Обычно выполняется на этапе BeforeRequest перед
сохранением карточки.  
[OnClosingTabAsync](M_Tessa_Cards_Numbers_NumberDirector_OnClosingTabAsync.htm)|
Уведомляет о том, что на стороне клиента закрывается вкладка с карточкой. При
этом может потребоваться освободить номер, если он был зарезервирован и ещё не
был занят.  
[OnCreatingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnCreatingCardAsync.htm)|
Уведомляет о том, что выполняется создание карточки (обычным способом или по
шаблону). При этом может потребоваться зарезервировать номер. Обычно
выполняется на этапе AfterRequest после создания карточки.  
[OnDeletingBackupCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnDeletingBackupCardAsync.htm)|
Уведомляет о том, что карточка окончательно удаляется, т.е. удаляется её
удалённая карточка [Tessa.Cards.CardHelper.DeletedTypeName]. При этом может
потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении удалённой карточки.  
[OnDeletingCardWithoutBackupAsync](M_Tessa_Cards_Numbers_NumberDirector_OnDeletingCardWithoutBackupAsync.htm)|
Уведомляет о том, что карточка удаляется без возможности восстановления. При
этом может потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении карточки без возможности восстановления.  
[OnDeregisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnDeregisteringCardAsync.htm)|
Уведомляет о том, что выполняется дерегистрация карточки. При этом может
потребоваться освободить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[OnGettingDigestAsync](M_Tessa_Cards_Numbers_NumberDirector_OnGettingDigestAsync.htm)|
Возвращает Digest карточки по её номерам.  
[OnImportingCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnImportingCardAsync.htm)|
Уведомляет о том, что карточка импортируется. При этом может потребоваться
занять номер, который был ранее занят. Обычно выполняется на этапе
BeforeCommitTransaction в транзакции на сохранение карточки.  
[OnPreparingTemplateAsync](M_Tessa_Cards_Numbers_NumberDirector_OnPreparingTemplateAsync.htm)|
Уведомляет о том, что карточка шаблона подготавливается к созданию по шаблону.
При этом может потребоваться очистить поля номеров, заданных в шаблоне. Обычно
выполняется на сервере на этапе AfterRequest после создания карточки, но перед
событием [Tessa.Cards.Numbers.NumberEventTypes.CreatingCard].  
[OnRegisteringCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnRegisteringCardAsync.htm)|
Уведомляет о том, что выполняется регистрация карточки. При этом может
потребоваться выделить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[OnReleasingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_OnReleasingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется освобождение номера из элемента управления.  
[OnReservingNumberFromControlAsync](M_Tessa_Cards_Numbers_NumberDirector_OnReservingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется резервирование номера из элемента
управления.  
[OnSavingNewCardAsync](M_Tessa_Cards_Numbers_NumberDirector_OnSavingNewCardAsync.htm)|
Уведомляет о том, что карточка впервые сохраняется. При этом может
потребоваться выделить номер. Обычно выполняется на этапе BeforeRequest перед
сохранением карточки.  
[ProcessControlRequestAsync](M_Tessa_Cards_Numbers_NumberDirector_ProcessControlRequestAsync.htm)|
Выполняет обработку запроса к API номеров на сервере, который связан с
элементом управления.  
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
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
[SealInternal](M_Tessa_Cards_Numbers_NumberDirectorBase_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[NumberDirectorBase](T_Tessa_Cards_Numbers_NumberDirectorBase.htm))  
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
[TryCreateControlRequestAsync](M_Tessa_Cards_Numbers_NumberDirector_TryCreateControlRequestAsync.htm)|
Создаёт и возвращает объект запроса к API номеров на сервере, который связан с
элементом управления. Возвращает null, если запрос не должен быть выполнен.  
[TryGetControlResponseAsync](M_Tessa_Cards_Numbers_NumberDirector_TryGetControlResponseAsync.htm)|
Возвращает объект ответа на запрос к элементу управления по ответу на запрос к
API номеров на сервере. Возвращает null, если объект отсутствует в ответе на
запрос.  
[TryGetNumberEffectiveLocationAsync](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
(Унаследован от [NumberBuilder](T_Tessa_Cards_Numbers_NumberBuilder.htm))  
[TryGetNumberEffectiveLocationCoreAsync](M_Tessa_Cards_Numbers_NumberDirector_TryGetNumberEffectiveLocationCoreAsync.htm)|
Возвращает эффективное местоположение номера по его заданному местоположению
или null, если эффективное местоположение недоступно и следует использовать
заданное местоположение location. Например, местоположение
[Tessa.Cards.Numbers.NumberLocationTypes.Primary] может соответствовать
определённым полям в карточке, задаваемым эффективным местоположением типа
[Tessa.Cards.Numbers.CardNumberLocation].  
(Переопределяет
[NumberBuilder.TryGetNumberEffectiveLocationCoreAsync(INumberContext,
NumberTypeDescriptor, INumberLocation,
CancellationToken)](M_Tessa_Cards_Numbers_NumberBuilder_TryGetNumberEffectiveLocationCoreAsync.htm))  
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
##  __Методы расширения
[CreateContextAsync](M_Tessa_Cards_Numbers_NumberExtensions_CreateContextAsync.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, принимая тип номера равным
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm). Этот метод может
использоваться для создания контекста с базовым состоянием для последующей
донастройки номера.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
---|---  
[CreateContextAsync](M_Tessa_Cards_Numbers_NumberExtensions_CreateContextAsync_1.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами. Этот метод может использоваться для создания контекста с базовым
состоянием для последующей донастройки номера.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[CreateInitializedContextAsync](M_Tessa_Cards_Numbers_NumberExtensions_CreateInitializedContextAsync.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, принимая тип номера равным
[Custom](F_Tessa_Cards_Numbers_NumberTypes_Custom.htm), а затем инициализирует
контекст с указанием типа события eventType.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[CreateInitializedContextAsync](M_Tessa_Cards_Numbers_NumberExtensions_CreateInitializedContextAsync_1.htm)|
Создаёт контекст операции с номером для объекта
[INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm) с заданными
параметрами, а затем инициализирует контекст с указанием типа события
eventType.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
[EnsureAvailable](M_Tessa_Cards_Numbers_NumberExtensions_EnsureAvailable.htm)|
Гарантирует, что объект
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm) в
коллекции доступных типов событий
[AvailableEventTypes](P_Tessa_Cards_Numbers_INumberDirectorBase_AvailableEventTypes.htm)
будет содержать тип действия eventType. Если коллекция защищена от изменений и
тип события в ней отсутствовал, то метод возвращает false.  
(Определяется [NumberExtensions](T_Tessa_Cards_Numbers_NumberExtensions.htm))  
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
