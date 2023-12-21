# INumberDirector - методы
##  __Методы
[GetBuilder](M_Tessa_Cards_Numbers_INumberDirectorBase_GetBuilder.htm)|
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.  
(Унаследован от
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm))  
---|---  
[GetDigestAsync](M_Tessa_Cards_Numbers_INumberDirector_GetDigestAsync.htm)|
Возвращает Digest карточки по её номерам.  
[IsAvailableAsync](M_Tessa_Cards_Numbers_INumberDirectorBase_IsAvailableAsync.htm)|
Выполняет проверку доступности для типа события, происходящего с номером.  
(Унаследован от
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm))  
[NotifyAfterEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyAfterEventAsync.htm)|
Выполняет постобработку события, происходящего с номером. Это предоставляет
возможность изменить результат обработанного события или сохранить результат
во внешнем хранилище.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[NotifyBeforeEventAsync](M_Tessa_Cards_Numbers_INumberExtendable_NotifyBeforeEventAsync.htm)|
Выполняет предварительную обработку события, происходящего с номером. Это
предоставляет возможность полностью заместить или отменить стандартную
обработку.  
(Унаследован от
[INumberExtendable](T_Tessa_Cards_Numbers_INumberExtendable.htm))  
[NotifyOnClosingTabAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnClosingTabAsync.htm)|
Уведомляет о том, что на стороне клиента закрывается вкладка с карточкой. При
этом может потребоваться освободить номер, если он был зарезервирован и ещё не
был занят.  
[NotifyOnCreatingCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnCreatingCardAsync.htm)|
Уведомляет о том, что выполняется создание карточки (обычным способом или по
шаблону). При этом может потребоваться зарезервировать номер. Обычно
выполняется на этапе AfterRequest после создания карточки.  
[NotifyOnDeletingBackupCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnDeletingBackupCardAsync.htm)|
Уведомляет о том, что карточка окончательно удаляется, т.е. удаляется её
удалённая карточка [Tessa.Cards.CardHelper.DeletedTypeName]. При этом может
потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении удалённой карточки.  
[NotifyOnDeletingCardWithoutBackupAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnDeletingCardWithoutBackupAsync.htm)|
Уведомляет о том, что карточка удаляется без возможности восстановления. При
этом может потребоваться освободить занятый номер. Обычно выполняется на этапе
BeforeCommitTransaction при удалении карточки без возможности восстановления.  
[NotifyOnDeregisteringCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnDeregisteringCardAsync.htm)|
Уведомляет о том, что выполняется дерегистрация карточки. При этом может
потребоваться освободить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[NotifyOnEventAsync](M_Tessa_Cards_Numbers_INumberDirectorBase_NotifyOnEventAsync.htm)|
Выполняет заданное действие с номером.  
(Унаследован от
[INumberDirectorBase](T_Tessa_Cards_Numbers_INumberDirectorBase.htm))  
[NotifyOnImportingCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnImportingCardAsync.htm)|
Уведомляет о том, что карточка импортируется. При этом может потребоваться
занять номер, который был ранее занят. Обычно выполняется на этапе
BeforeCommitTransaction в транзакции на сохранение карточки.  
[NotifyOnPreparingTemplateAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnPreparingTemplateAsync.htm)|
Уведомляет о том, что карточка шаблона подготавливается к созданию по шаблону.
При этом может потребоваться очистить поля номеров, заданных в шаблоне. Обычно
выполняется на сервере на этапе AfterRequest после создания карточки, но перед
событием [Tessa.Cards.Numbers.NumberEventTypes.CreatingCard].  
[NotifyOnRegisteringCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnRegisteringCardAsync.htm)|
Уведомляет о том, что выполняется регистрация карточки. При этом может
потребоваться выделить регистрационный номер. Обычно выполняется на этапе
BeforeRequest перед сохранением карточки.  
[NotifyOnReleasingNumberFromControlAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnReleasingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется освобождение номера из элемента управления.  
[NotifyOnReservingNumberFromControlAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnReservingNumberFromControlAsync.htm)|
Уведомляет о том, что выполняется резервирование номера из элемента
управления.  
[NotifyOnSavingNewCardAsync](M_Tessa_Cards_Numbers_INumberDirector_NotifyOnSavingNewCardAsync.htm)|
Уведомляет о том, что карточка впервые сохраняется. При этом может
потребоваться выделить номер. Обычно выполняется на этапе BeforeRequest перед
сохранением карточки.  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
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
##  __См. также
#### Ссылки
[INumberDirector - ](T_Tessa_Cards_Numbers_INumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
