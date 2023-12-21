# Tessa.UI.Cards - пространство имён
Автоматический UI для карточек и редактора типов карточек.
##  __Классы
[AdvancedCardDialogManager](T_Tessa_UI_Cards_AdvancedCardDialogManager.htm)|
Объект, предоставляющий методы для открытий карточки в модальном диалоге.  
---|---  
[AdvancedCardDialogManagerCreationCardContext](T_Tessa_UI_Cards_AdvancedCardDialogManagerCreationCardContext.htm)|  
[AnyDialogExtensionPolicy](T_Tessa_UI_Cards_AnyDialogExtensionPolicy.htm)|  
[BlockTypeResolver](T_Tessa_UI_Cards_BlockTypeResolver.htm)|  Объект,
используемый для получения типов блоков, используемых в автоматическом UI
карточки.  
[BorderedTextStyleViewModel](T_Tessa_UI_Cards_BorderedTextStyleViewModel.htm)|
Настройки стиля для текста, обрамлённого рамкой.  
[CardCommitChangesContext](T_Tessa_UI_Cards_CardCommitChangesContext.htm)|
Контекст операции по утверждению изменений в элементах управления
[CommitChangesAsync(ICardCommitChangesContext)](M_Tessa_UI_Cards_IControlViewModel_CommitChangesAsync.htm).  
[CardCreationInfo](T_Tessa_UI_Cards_CardCreationInfo.htm)|  Объект, содержащий
информацию по созданию карточки и её открытию в новой вкладке.  
[CardDialogManager](T_Tessa_UI_Cards_CardDialogManager.htm)|  Предоставляет
средства для вывода диалогов, используемых в карточках и типах карточек.  
[CardEditorTemplateSelector](T_Tessa_UI_Cards_CardEditorTemplateSelector.htm)|  
[CardIntegerOperation<TItem,
TContext>](T_Tessa_UI_Cards_CardIntegerOperation_2.htm)|  Базовый класс для
массовой операции с карточками. В качестве идентификатора карточки указывается
целое число [Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[CardIntegerOperationItem](T_Tessa_UI_Cards_CardIntegerOperationItem.htm)|
Элемент операции [CardIntegerOperation<TItem,
TContext>](T_Tessa_UI_Cards_CardIntegerOperation_2.htm), описывающий действие
с одной карточкой. В качестве идентификатора карточки указывается целое число
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[CardModel](T_Tessa_UI_Cards_CardModel.htm)|  Модель карточки, доступная в UI.  
[CardModelInitializingEventArgs](T_Tessa_UI_Cards_CardModelInitializingEventArgs.htm)|
Аргументы события по инициализации модели карточки.  
[CardModelSettingsManager](T_Tessa_UI_Cards_CardModelSettingsManager.htm)|
Объект, управляющий сохранением настроек
[ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm).  
[CardModelTableInfo](T_Tessa_UI_Cards_CardModelTableInfo.htm)|  Информация по
строке дочерней секции, открытой в модели карточки
[ICardModel](T_Tessa_UI_Cards_ICardModel.htm).  
[CardModelTypeFilterPolicy](T_Tessa_UI_Cards_CardModelTypeFilterPolicy.htm)|
Политика фильтрации расширений UI, использующая политику
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) для того,
чтобы не выполнять методы расширений, для которых в контексте
[ICardUIExtensionContext](T_Tessa_UI_Cards_ICardUIExtensionContext.htm) или
[IFormUIExtensionContext](T_Tessa_UI_IFormUIExtensionContext.htm) использован
тип карточки, запрещённый указанной политикой. Если политика
[ICardTypePolicy](T_Tessa_Cards_Extensions_ICardTypePolicy.htm) не
зарегистрирована, то метод расширения выполняется.  
[CardOperation<TItem, TContext>](T_Tessa_UI_Cards_CardOperation_2.htm)|
Базовый класс для массовой операции с карточками. В качестве идентификатора
карточки указывается
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[CardOperationBase<TIdentifier, TItem,
TContext>](T_Tessa_UI_Cards_CardOperationBase_3.htm)|  Базовый класс для
массовой операции с карточками.  
[CardOperationItem](T_Tessa_UI_Cards_CardOperationItem.htm)|  Элемент операции
[CardOperation<TItem, TContext>](T_Tessa_UI_Cards_CardOperation_2.htm),
описывающий действие с одной карточкой. В качестве идентификатора карточки
указывается целое число
[Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[CardOperationItemBase<TIdentifier>](T_Tessa_UI_Cards_CardOperationItemBase_1.htm)|
Базовый класс для элемента операции [CardOperationBase<TIdentifier, TItem,
TContext>](T_Tessa_UI_Cards_CardOperationBase_3.htm), описывающий действие с
одной карточкой.  
[CardSavingRequest](T_Tessa_UI_Cards_CardSavingRequest.htm)|  Запрос на
сохранение карточки, передаваемый в
[ICardModel](T_Tessa_UI_Cards_ICardModel.htm).  
[CardToolbarAction](T_Tessa_UI_Cards_CardToolbarAction.htm)|  
[CardToolbarActionGroup](T_Tessa_UI_Cards_CardToolbarActionGroup.htm)|  
[CardToolbarItem](T_Tessa_UI_Cards_CardToolbarItem.htm)|  
[CardToolbarItemCollection](T_Tessa_UI_Cards_CardToolbarItemCollection.htm)|  
[CardToolbarItemDelegateCommand<T>](T_Tessa_UI_Cards_CardToolbarItemDelegateCommand_1.htm)|  
[CardToolbarViewModel](T_Tessa_UI_Cards_CardToolbarViewModel.htm)|  
[CardTypeRepairVisitor](T_Tessa_UI_Cards_CardTypeRepairVisitor.htm)|  Объект,
выполняющий посещение объектов типа карточки с целью их восстановления в
соответствии со схемой и типами форм, блоков, элементов управления и
валидаторов.  
[CardUIException](T_Tessa_UI_Cards_CardUIException.htm)|  Исключение в
процессе построения автоматического UI карточки или редакторов такого UI.  
[CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm)|  Расширения для
модели представления карточки.  
[CardUIExtensionContext](T_Tessa_UI_Cards_CardUIExtensionContext.htm)|
Контекст расширений для модели представления карточки.  
[CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm)|  Методы-расширения
для пространства имён Tessa.UI.Cards.  
[CardUIHelper](T_Tessa_UI_Cards_CardUIHelper.htm)|  Вспомогательные методы для
взаимодействия с UI карточки.  
[CardUIManager](T_Tessa_UI_Cards_CardUIManager.htm)|  Объект, предоставляющий
пользовательский интерфейс для операций с карточками.  
[CardUIMetadataBinder](T_Tessa_UI_Cards_CardUIMetadataBinder.htm)|  Объект,
осуществляющий действия с карточкой [Card](T_Tessa_Cards_Card.htm), требующие
наличие метаинформации [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm), в
потоке UI. Это такие операции, как удаление строк коллекционных секций с
учётом всех дочерних строк.  
[CardUIResolver](T_Tessa_UI_Cards_CardUIResolver.htm)|  Объект, используемый
для получения объектов, используемых в автоматическом UI карточки.  
[CardUISettings](T_Tessa_UI_Cards_CardUISettings.htm)|  Настройки элементов
управления и блоков, которые используются для редактирования значений
определённого типа.  
[CloseSessionOperation](T_Tessa_UI_Cards_CloseSessionOperation.htm)|  Операция
по закрытию сессий.  
[ControlTypeResolver](T_Tessa_UI_Cards_ControlTypeResolver.htm)|  Объект,
используемый для получения типов элементов управления, используемых в
автоматическом UI карточки.  
[DeleteCardIntegerOperationItem](T_Tessa_UI_Cards_DeleteCardIntegerOperationItem.htm)|
Элемент операции, описывающий удаляемую карточку для операции
[DeleteCardOperation](T_Tessa_UI_Cards_DeleteCardOperation.htm). В качестве
идентификатора карточки указывается целое число
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[DeleteCardOperation](T_Tessa_UI_Cards_DeleteCardOperation.htm)|  Операция по
удалению карточек.  
[DeleteCardOperationItem](T_Tessa_UI_Cards_DeleteCardOperationItem.htm)|
Элемент операции, описывающий удаляемую карточку для операции
[DeleteCardOperation](T_Tessa_UI_Cards_DeleteCardOperation.htm).  
[DeleteIntegerCardOperation](T_Tessa_UI_Cards_DeleteIntegerCardOperation.htm)|
Операция по удалению карточек. В качестве идентификатора карточки указывается
целое число [Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[DeleteNotificationSubscriptionOperation](T_Tessa_UI_Cards_DeleteNotificationSubscriptionOperation.htm)|
Операция по удалению подписок на уведомления карточки.  
[DialogExtensionPolicy](T_Tessa_UI_Cards_DialogExtensionPolicy.htm)|  
[DialogFilterPolicy](T_Tessa_UI_Cards_DialogFilterPolicy.htm)|  
[DialogFormInvoker](T_Tessa_UI_Cards_DialogFormInvoker.htm)|  Объект,
предоставляющий стандартную реализацию [TryCreateDialogFormAsync(String,
String, FormCreationOptions, Func<CardNewResponse, CancellationToken,
ValueTask>, Func<ICardModel, CancellationToken, ValueTask>,
Func<IReadOnlyList<CardType>, String, IEnumerable<CardType>>,
CancellationToken)](M_Tessa_UI_Cards_DialogFormInvoker_TryCreateDialogFormAsync.htm)
для делегата
[CreateDialogFormFuncAsync](T_Tessa_UI_Cards_CreateDialogFormFuncAsync.htm).  
[EditorViewModelBase](T_Tessa_UI_Cards_EditorViewModelBase.htm)|  Базовый
класс для модели представления, выполняющей редактирование метаинформации о
форме, блоке или элементе управления.  
[ExportAllCardOperation](T_Tessa_UI_Cards_ExportAllCardOperation.htm)|
Операция по экспорту всех карточек из представления.  
[ExportCardOperation](T_Tessa_UI_Cards_ExportCardOperation.htm)|  Операция по
экспорту карточек.  
[ExportCardOperationItem](T_Tessa_UI_Cards_ExportCardOperationItem.htm)|
Элемент операции, описывающий экспортируемую карточку для операции
[ExportCardOperation](T_Tessa_UI_Cards_ExportCardOperation.htm).  
[FakeAdvancedCardDialogManager](T_Tessa_UI_Cards_FakeAdvancedCardDialogManager.htm)|
Реализация интерфейса
[IAdvancedCardDialogManager](T_Tessa_UI_Cards_IAdvancedCardDialogManager.htm),
не выполняющая работы и выбрасывающая исключения
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception).
Используется в приложении TessaAdmin.  
[FormCreationContext](T_Tessa_UI_Cards_FormCreationContext.htm)|  Контекст
операции по созданию формы.  
[FormTypeResolver](T_Tessa_UI_Cards_FormTypeResolver.htm)|  Объект,
используемый для получения типов форм, используемых в автоматическом UI
карточки.  
[FormViewModelCollection](T_Tessa_UI_Cards_FormViewModelCollection.htm)|
Коллекция форм карточки.  
[ForumChangeParticipants](T_Tessa_UI_Cards_ForumChangeParticipants.htm)|  
[ForumOperation](T_Tessa_UI_Cards_ForumOperation.htm)|  
[ForumOperationContext](T_Tessa_UI_Cards_ForumOperationContext.htm)|  
[ForumOperationItem](T_Tessa_UI_Cards_ForumOperationItem.htm)|  
[ForumRemoveParticipants](T_Tessa_UI_Cards_ForumRemoveParticipants.htm)|  
[MySettingsDialogManager](T_Tessa_UI_Cards_MySettingsDialogManager.htm)|
Объект, управляющий отображением диалогов "Мои настройки".  
[MySettingsExtension](T_Tessa_UI_Cards_MySettingsExtension.htm)|  Базовый
класс для расширения для диалога "Мои настройки".  
[MySettingsExtensionContext](T_Tessa_UI_Cards_MySettingsExtensionContext.htm)|
Контекст расширений для диалога "Мои настройки". Используется в расширениях
[IMySettingsExtension](T_Tessa_UI_Cards_IMySettingsExtension.htm).  
[PermissionHelper](T_Tessa_UI_Cards_PermissionHelper.htm)|  
[RemoveOperationOperation](T_Tessa_UI_Cards_RemoveOperationOperation.htm)|
Операция по удалению операций из "Активных операций".  
[RepairCardOperation<TItem,
TContext>](T_Tessa_UI_Cards_RepairCardOperation_2.htm)|  Базовый класс для
операций по исправлению карточек, сериализованных в других карточках
(например, в карточках шаблонов или в удалённых карточках).  
[RepairCardOperationItem](T_Tessa_UI_Cards_RepairCardOperationItem.htm)|
Элемент операции, описывающий исправляемую карточку для соответствующих
операций. Наследники класса могут определять дополнительные свойства.  
[RepairDeletedOperation](T_Tessa_UI_Cards_RepairDeletedOperation.htm)|
Операция по исправлению удалённых карточек.  
[RepairTemplateOperation](T_Tessa_UI_Cards_RepairTemplateOperation.htm)|
Операция по исправлению карточек в шаблонах.  
[RestoreCardOperation](T_Tessa_UI_Cards_RestoreCardOperation.htm)|  Операция
по восстановлению удалённых карточек.  
[RestoreCardOperationItem](T_Tessa_UI_Cards_RestoreCardOperationItem.htm)|
Элемент операции, описывающий восстанавливаемую карточку для операции
[RestoreCardOperation](T_Tessa_UI_Cards_RestoreCardOperation.htm).  
[RowContext](T_Tessa_UI_Cards_RowContext.htm)|  Контекст для диалога
редактирования строки в карточке.  
[SupportSelectAllControlViewModelBase](T_Tessa_UI_Cards_SupportSelectAllControlViewModelBase.htm)|
Базовый класс для моделей представления элементов управления в автоматическом
UI карточки, которые также поддерживают интерфейс
[ISupportSelectAll](T_Tessa_UI_Cards_ISupportSelectAll.htm).  
[TabSelectedEventArgs](T_Tessa_UI_Cards_TabSelectedEventArgs.htm)|  Контекст
метода по уведомлению форм, блоков и контролов при переключении вкладок.  
[TextStyleViewModel](T_Tessa_UI_Cards_TextStyleViewModel.htm)|  Настройки
стиля для текста.  
[TypeExtensionTypeResolver](T_Tessa_UI_Cards_TypeExtensionTypeResolver.htm)|
Объект, используемый для получения типов расширений для типов карточек,
используемых в автоматическом UI карточки.  
[ValidatorTypeResolver](T_Tessa_UI_Cards_ValidatorTypeResolver.htm)|  Объект,
используемый для получения типов валидаторов, используемых в автоматическом UI
карточки.  
[ViewModelBag<T>](T_Tessa_UI_Cards_ViewModelBag_1.htm)|  Объект, содержащий
неупорядоченный список всех элементов управления в карточке. При этом элементы
управления карточки, её заданий и файлов размещаются в одном и том же объекте.  
## __Интерфейсы
[IAdvancedCardDialogManager](T_Tessa_UI_Cards_IAdvancedCardDialogManager.htm)|
Объект, предоставляющий методы для открытий карточки в модальном диалоге.  
---|---  
[IBlockState](T_Tessa_UI_Cards_IBlockState.htm)|  Объект, описывающий
состояние элемента управления
[IBlockViewModel](T_Tessa_UI_Cards_IBlockViewModel.htm).  
[IBlockType](T_Tessa_UI_Cards_IBlockType.htm)|  Тип блока, используемого в
автоматическом UI карточки.  
[IBlockTypeResolver](T_Tessa_UI_Cards_IBlockTypeResolver.htm)|  Объект,
используемый для получения типов блоков, используемых в автоматическом UI
карточки.  
[IBlockViewModel](T_Tessa_UI_Cards_IBlockViewModel.htm)|  Модель представления
блока в автоматическом UI карточки.  
[IBorderedTextStyleViewModel](T_Tessa_UI_Cards_IBorderedTextStyleViewModel.htm)|
Настройки стиля для текста, обрамлённого рамкой.  
[ICardCommitChangesContext](T_Tessa_UI_Cards_ICardCommitChangesContext.htm)|
Контекст операции по утверждению изменений в элементах управления
[CommitChangesAsync(ICardCommitChangesContext)](M_Tessa_UI_Cards_IControlViewModel_CommitChangesAsync.htm).  
[ICardDialogManager](T_Tessa_UI_Cards_ICardDialogManager.htm)|  Предоставляет
средства для вывода диалогов, используемых в карточках и типах карточек.  
[ICardEditorCreationContext](T_Tessa_UI_Cards_ICardEditorCreationContext.htm)|
Контекст, содержащий информацию по созданной карточке.  
[ICardEditorData](T_Tessa_UI_Cards_ICardEditorData.htm)|  Информация по
последним запросам, выполненным для объекта
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm).  
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)|  Редактируемое
представление карточки на клиенте.  
[ICardEditorModelContext](T_Tessa_UI_Cards_ICardEditorModelContext.htm)|
Объект, содержащий контекст редактора карточек
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm).  
[ICardEditorOpeningContext](T_Tessa_UI_Cards_ICardEditorOpeningContext.htm)|
Контекст, содержащий информацию по открытой карточке.  
[ICardEditorOperationContext<TRequest,
TResponse>](T_Tessa_UI_Cards_ICardEditorOperationContext_2.htm)|  Контекст,
содержащий информацию по карточке, которая относится к операции в
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm).  
[ICardModel](T_Tessa_UI_Cards_ICardModel.htm)|  Модель карточки, доступная в
UI.  
[ICardModelSettingsManager](T_Tessa_UI_Cards_ICardModelSettingsManager.htm)|
Объект, управляющий сохранением настроек
[ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm).  
[ICardSavingRequest](T_Tessa_UI_Cards_ICardSavingRequest.htm)|  Запрос на
сохранение карточки, передаваемый в
[ICardModel](T_Tessa_UI_Cards_ICardModel.htm).  
[ICardToolbarItem](T_Tessa_UI_Cards_ICardToolbarItem.htm)|  
[ICardToolbarItemCollection](T_Tessa_UI_Cards_ICardToolbarItemCollection.htm)|  
[ICardToolbarItemGroup](T_Tessa_UI_Cards_ICardToolbarItemGroup.htm)|  
[ICardToolbarViewModel](T_Tessa_UI_Cards_ICardToolbarViewModel.htm)|  
[ICardUIExtension](T_Tessa_UI_Cards_ICardUIExtension.htm)|  Расширения для
модели представления карточки.  
[ICardUIExtensionContext](T_Tessa_UI_Cards_ICardUIExtensionContext.htm)|
Контекст расширений для модели представления карточки.  
[ICardUIManager](T_Tessa_UI_Cards_ICardUIManager.htm)|  Объект,
предоставляющий пользовательский интерфейс для операций с карточками.  
[ICardUIResolver](T_Tessa_UI_Cards_ICardUIResolver.htm)|  Объект, используемый
для получения объектов, используемых в автоматическом UI карточки.  
[IControlState](T_Tessa_UI_Cards_IControlState.htm)|  Объект, описывающий
состояние элемента управления
[IControlViewModel](T_Tessa_UI_Cards_IControlViewModel.htm).  
[IControlType](T_Tessa_UI_Cards_IControlType.htm)|  Тип элемента управления,
используемого в автоматическом UI карточки.  
[IControlTypeResolver](T_Tessa_UI_Cards_IControlTypeResolver.htm)|  Объект,
используемый для получения типов элементов управления, используемых в
автоматическом UI карточки.  
[IControlViewModel](T_Tessa_UI_Cards_IControlViewModel.htm)|  Модель
представления элемента управления в автоматическом UI карточки.  
[IDialogExtensionPolicy](T_Tessa_UI_Cards_IDialogExtensionPolicy.htm)|  
[IEditorViewModel](T_Tessa_UI_Cards_IEditorViewModel.htm)|  Модель
представления для редактирования метаинформации о форме, блоке или элементе
управления.  
[IFormCreationContext](T_Tessa_UI_Cards_IFormCreationContext.htm)|  Контекст
операции по созданию формы.  
[IFormState](T_Tessa_UI_Cards_IFormState.htm)|  Объект, описывающий состояние
формы [IFormViewModel](T_Tessa_UI_Cards_IFormViewModel.htm).  
[IFormType](T_Tessa_UI_Cards_IFormType.htm)|  Тип формы, используемой в
автоматическом UI карточки.  
[IFormTypeResolver](T_Tessa_UI_Cards_IFormTypeResolver.htm)|  Объект,
используемый для получения типов форм, используемых в автоматическом UI
карточки.  
[IFormViewModel](T_Tessa_UI_Cards_IFormViewModel.htm)|  Модель представления
формы в автоматическом UI карточки.  
[IForumOperationContext](T_Tessa_UI_Cards_IForumOperationContext.htm)|  
[IMainFormViewModel](T_Tessa_UI_Cards_IMainFormViewModel.htm)|  Модель
представления основной формы в автоматическом UI карточки. Поддерживает
управление вкладками. Обычно соответствует основной форме карточки в свойстве
[MainForm](P_Tessa_UI_Cards_ICardModel_MainForm.htm).  
[IMySettingsDialogManager](T_Tessa_UI_Cards_IMySettingsDialogManager.htm)|
Объект, управляющий отображением диалогов "Мои настройки".  
[IMySettingsExtension](T_Tessa_UI_Cards_IMySettingsExtension.htm)|  Расширения
для диалога "Мои настройки".  
[IMySettingsExtensionContext](T_Tessa_UI_Cards_IMySettingsExtensionContext.htm)|
Контекст расширений для диалога "Мои настройки". Используется в расширениях
[IMySettingsExtension](T_Tessa_UI_Cards_IMySettingsExtension.htm).  
[IRowContext](T_Tessa_UI_Cards_IRowContext.htm)|  Контекст для диалога
редактирования строки в карточке.  
[ISupportSelectAll](T_Tessa_UI_Cards_ISupportSelectAll.htm)|  Элемент
управления, поддерживающий выбор всего текста.  
[ISupportTabNotifications](T_Tessa_UI_Cards_ISupportTabNotifications.htm)|
Признак того, что объект поддерживает уведомления о переключении вкладки.  
[ITabbedFormViewModel](T_Tessa_UI_Cards_ITabbedFormViewModel.htm)|  Модель
представления формы, содержащей вкладки, в автоматическом UI карточки. Обычно
соответствует основной форме карточки в свойстве
[MainForm](P_Tessa_UI_Cards_ICardModel_MainForm.htm).  
[ITabSelectedContext](T_Tessa_UI_Cards_ITabSelectedContext.htm)|  Контекст
метода по уведомлению форм, блоков и контролов при переключении вкладок.  
[ITextStyleViewModel](T_Tessa_UI_Cards_ITextStyleViewModel.htm)|  Настройки
стиля для текста.  
[ITypeExtensionType](T_Tessa_UI_Cards_ITypeExtensionType.htm)|  Тип расширения
для типов карточек, используемый в автоматическом UI карточки.  
[ITypeExtensionTypeResolver](T_Tessa_UI_Cards_ITypeExtensionTypeResolver.htm)|
Объект, используемый для получения типов расширений для типов карточек,
используемых в автоматическом UI карточки.  
[IValidatorType](T_Tessa_UI_Cards_IValidatorType.htm)|  Тип валидатора,
используемого в автоматическом UI карточки.  
[IValidatorTypeResolver](T_Tessa_UI_Cards_IValidatorTypeResolver.htm)|
Объект, используемый для получения типов валидаторов, используемых в
автоматическом UI карточки.  
[IViewModelBag<T>](T_Tessa_UI_Cards_IViewModelBag_1.htm)|  Объект, содержащий
неупорядоченный список всех элементов управления в карточке. При этом элементы
управления карточки, её заданий и файлов размещаются в одном и том же объекте.  
## __Делегаты
[CardControlCreationOverrideAsync](T_Tessa_UI_Cards_CardControlCreationOverrideAsync.htm)|
Функция, подменяющая создание элемента управления и возвращающая созданный
элемент управления или null, если создание элемента управления не было
переопределено.  
---|---  
[CardControlValidationFunc](T_Tessa_UI_Cards_CardControlValidationFunc.htm)|
Функция, возвращающая строку с сообщением об ошибке валидации, если такая
ошибка возникла, или null или пустую строку, если ошибок нет.  
[CardEditorCreationActionAsync](T_Tessa_UI_Cards_CardEditorCreationActionAsync.htm)|
Действие, выполняемое для созданной карточки.  
[CardEditorOpeningActionAsync](T_Tessa_UI_Cards_CardEditorOpeningActionAsync.htm)|
Действие, выполняемое для открытой карточки.  
[CardModelSavingFuncAsync](T_Tessa_UI_Cards_CardModelSavingFuncAsync.htm)|
Функция сохранения карточки [ICardModel](T_Tessa_UI_Cards_ICardModel.htm),
принимающая запрос на сохранение карточки и возвращающая объект, позволяющий
отслеживать операцию сохранения и получить её результат. Функцию можно
установить посредством вызова метода
[SetSavingFunc(CardModelSavingFuncAsync)](M_Tessa_UI_Cards_ICardModel_SetSavingFunc.htm).  
[CreateCardFormFuncAsync](T_Tessa_UI_Cards_CreateCardFormFuncAsync.htm)|
Функция, которая создаёт модель представления для используемой по умолчанию
формы по заданной модели карточки.  
[CreateCardModelFuncAsync](T_Tessa_UI_Cards_CreateCardModelFuncAsync.htm)|
Функция, которая создаёт модель карточки по заданным параметрам.  
[CreateCardModelWithMetadataFuncAsync](T_Tessa_UI_Cards_CreateCardModelWithMetadataFuncAsync.htm)|
Функция, которая создаёт модель карточки по заданным параметрам.  
[CreateDialogFormFuncAsync](T_Tessa_UI_Cards_CreateDialogFormFuncAsync.htm)|
Функция, которая создает модель представления формы для заданной вкладки типа
диалога.  
[CreateFileSourceForCardModelFuncAsync](T_Tessa_UI_Cards_CreateFileSourceForCardModelFuncAsync.htm)|
Создаёт источник файлов для карточки по заданной модели.  
[ShowCardGridEditorActionAsync](T_Tessa_UI_Cards_ShowCardGridEditorActionAsync.htm)|
Метод, выполняющий открытие окна редактирования формы в режиме сетки для
заданных формы и типа карточки.  
[ShowCardPreviewActionAsync](T_Tessa_UI_Cards_ShowCardPreviewActionAsync.htm)|
Метод, выполняющий открытие окна предварительного просмотра для заданных формы
и типа карточки.  
[ShowCardRowActionAsync](T_Tessa_UI_Cards_ShowCardRowActionAsync.htm)|  Метод,
отображающий форму для строки карточки, которая определяется через заданный
контекст.  
## __Перечисления
[CardCreationMode](T_Tessa_UI_Cards_CardCreationMode.htm)|  Способ создания
карточки.  
---|---  
[CardEditorOperationType](T_Tessa_UI_Cards_CardEditorOperationType.htm)|  Тип
операции, выполняемой для редактируемого представления карточки на клиенте
[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm).  
[CardModelFlags](T_Tessa_UI_Cards_CardModelFlags.htm)|  Флаги, которые
указываются для [ICardModel](T_Tessa_UI_Cards_ICardModel.htm) и описывают
особенности отображения карточки в UI.  
[CardPreviewMode](T_Tessa_UI_Cards_CardPreviewMode.htm)|  Способ
предварительного просмотра типа карточки.  
[CardSavingMode](T_Tessa_UI_Cards_CardSavingMode.htm)|  Способ сохранения
карточки в редакторе.  
[CardUIFinalizationType](T_Tessa_UI_Cards_CardUIFinalizationType.htm)|  Тип
финализации карточки в расширениях
[ICardUIExtension](T_Tessa_UI_Cards_ICardUIExtension.htm).  
[CardUIInitializationType](T_Tessa_UI_Cards_CardUIInitializationType.htm)|
Тип инициализации карточки в расширениях
[ICardUIExtension](T_Tessa_UI_Cards_ICardUIExtension.htm).  
[RepairResult](T_Tessa_UI_Cards_RepairResult.htm)|  Результат восстановления
объекта типа карточек к работоспособному состоянию в соответствии со схемой.  
[RowEditingType](T_Tessa_UI_Cards_RowEditingType.htm)|  Способ редактирования
строки в карточке.
