# CardTableViewControlViewModel - класс
Модель-представление для элемента управления отображающего таблицу в
представление в карточках.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TableViewExtension](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardTableViewControlViewModel : CardViewControlViewModel
VB __Копировать
     Public Class CardTableViewControlViewModel
    	Inherits CardViewControlViewModel
C++ __Копировать
     public ref class CardTableViewControlViewModel : public CardViewControlViewModel
F# __Копировать
     type CardTableViewControlViewModel = 
        class
            inherit CardViewControlViewModel
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[SupportUnloadingViewModel](T_Tessa_UI_SupportUnloadingViewModel.htm) __[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm) __[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm) __ CardTableViewControlViewModel
##  __Конструкторы
[CardTableViewControlViewModel](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel__ctor.htm)|
Инициализирует новый экземпляр класса CardTableViewControlViewModel  
---|---  
##  __Свойства
[ActualMargin](P_Tessa_UI_Cards_Controls_ControlViewModelBase_ActualMargin.htm)|
Предпочитаемый отступ элемента управления относительно других элементов
управления, расчитываемый блоком и используемый при отображении. Не
рекомендуется вручную изменять это значение.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
---|---  
[AddRowButton](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_AddRowButton.htm)|
Кнопка добавления строки. Нельзя присвоить значение null. Видимость кнопки
устанавливается автоматически, не рекомендуется его изменять без
необходимости.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Alias](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Alias.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[AllowDrop](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_AllowDrop.htm)|
Признак возможности обработки операций Drag-n-Drop  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Block](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Block.htm)| Блок, в
котором размещён текущий элемент управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[BottomItems](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_BottomItems.htm)|
Дополнительные кнопки под таблицей внизу.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Caption](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Caption.htm)|
Заголовок элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CaptionStyle](P_Tessa_UI_Cards_Controls_ControlViewModelBase_CaptionStyle.htm)|
Стиль текста для заголовка контрола.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CaptionVisibility](P_Tessa_UI_Cards_Controls_ControlViewModelBase_CaptionVisibility.htm)|
Видимость заголовка элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CardIDParam](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_CardIDParam.htm)|
Параметр представления, в которые пробрасывается ID карточки.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[CardModel](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_CardModel.htm)|
Модель карточки  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[CardTypeControl](P_Tessa_UI_Cards_Controls_ControlViewModelBase_CardTypeControl.htm)|
Информация о типе отображаемого элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ClientQuickSearchText](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ClientQuickSearchText.htm)|
Текст клиентского быстрого поиска  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ColumnSpan](P_Tessa_UI_Cards_Controls_ControlViewModelBase_ColumnSpan.htm)|
Количество колонок, которые занимает контрол по горизонтали. Неактуально для
контролов, растягиваемых по ширине всей строки. По умолчанию значение равно 1
и не может быть меньше. Если заданное количество колонок больше, чем общее
количество колонок в блоке, то контрол растягивается на ширину строки.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[Content](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Content.htm)|
Отображаемое содержимое  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ContentMaxHeight](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ContentMaxHeight.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ContentVisible](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ContentVisible.htm)|
Признак отображения основной области отображения
[Content](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Content.htm)  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ContextMenuGenerators](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ContextMenuGenerators.htm)|
Gets Список генераторов контекстного меню  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ControlVisibility](P_Tessa_UI_Cards_Controls_ControlViewModelBase_ControlVisibility.htm)|
Видимость элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CreateRowFunc](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_CreateRowFunc.htm)|
Функция для перегрузки создания строки  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[CurrentPage](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_CurrentPage.htm)|
Текущая страница  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[CurrentRefreshTask](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_CurrentRefreshTask.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DataProvider](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_DataProvider.htm)|
Источник данных  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DelayedViewRefresh](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_DelayedViewRefresh.htm)|
Отложенное обновление представления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DeleteRowsButton](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_DeleteRowsButton.htm)|
Кнопка удаления выделенных строк. Нельзя присвоить значение null. Видимость
кнопки устанавливается автоматически, не рекомендуется его изменять без
необходимости.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DoubleClickCommand](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_DoubleClickCommand.htm)|
Команда обрабатывающая двойной щелчок мышью  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DragDrop](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_DragDrop.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[EditRowCommand](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_EditRowCommand.htm)|
Команда, выполняемая при открытии окна редактирования строки (например, по
двойному клику). Команду нельзя изменить в расширениях, используйте событие
[RowInvoked](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInvoked.htm).  
[EmptyColumnsToTheLeft](P_Tessa_UI_Cards_Controls_ControlViewModelBase_EmptyColumnsToTheLeft.htm)|
Количество пустых колонок, которые отображаются слева от контрола. Неактуально
для контролов, растягиваемых по ширине всей строки. По умолчанию значение
равно 0 и не может быть меньше. Если заданное количество колонок больше, чем
количество колонок в блоке минус количество колонок, занимаемых контролом, то
отрисовывается столько пустых колонок, сколько умещается в строке. Если
контрол рисуется не с начала строки, и он не умещается вместе с заданным
отступом, то он переносится на следующую строку.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[EnableMouseScrolling](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_EnableMouseScrolling.htm)|
true, если прокрутка колесом мыши прокручивает таблицу; false, если прокрутка
колесом мыши прокручивает карточку, а для прокрутки таблицы требуется зажать
Ctrl.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Error](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Error.htm)|  Сообщение
об ошибке, связанное с текущим объектом, или null, если ошибки нет.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[FirstRowSelection](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_FirstRowSelection.htm)|
Автоматически выбирать первую строку после обновления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Focusable](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Focusable.htm)|
Признак того, что элемент управления может иметь логический фокус.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[FocusPending](P_Tessa_UI_Cards_Controls_ControlViewModelBase_FocusPending.htm)|
Признак того, что элемент управления получит логический фокус, как только
элемент управления станет доступен, т.е. его свойство
[Tessa.UI.Cards.IControlViewModel.IsEnabled] будет равно true.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[HasActiveValidation](P_Tessa_UI_Cards_Controls_ControlViewModelBase_HasActiveValidation.htm)|
Признак того, что в элементе управления следует включить активную валидацию.
При этом если для элемента управления введено некорректное значение, то он
будет уведомлять об этом рамкой валидации. Значение устанавливливается равным
true обычно после неудачного сохранения карточки. По умолчанию значение равно
false.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[HasNextPage](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_HasNextPage.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[HorizontalAlignment](P_Tessa_UI_Cards_Controls_ControlViewModelBase_HorizontalAlignment.htm)|
Выравнивание контрола по горизонтали. По умолчанию контрол выравнивается по
ширине Stretch.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[Initialized](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Initialized.htm)|
Признак того, что форма уже инициализирована вызовом
[InitializeAsync(CancellationToken)](M_Tessa_Platform_IAsyncInitializable_InitializeAsync.htm),
поэтому повторные вызовы метода будут игнорироваться.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[InitializedStrategy](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializedStrategy.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InitialRefreshIsCompleted](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitialRefreshIsCompleted.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[IsChildViewControl](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_IsChildViewControl.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[IsDataLoading](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_IsDataLoading.htm)|
Признак загрузки данных  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[IsEmpty](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsEmpty.htm)| Признак
того, что элемент управления не содержит отображаемых данных.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsEnabled](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsEnabled.htm)|
Признак того, что элемент управления доступен для взаимодействия. Только
доступный элемент может получить логический фокус. Свойство следует
использовать только для чтения, т.е. можно проверить его значение и
подписаться на его изменение в PropertyChanged, но установленное в свойстве
значение будет проигнорировано.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsFocused](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsFocused.htm)|
Признак того, что элемент управления имеет логический фокус. Проверка и
установка значения свойства имеет смысл только в случае, если элемент
управления может получить логический фокус, т.е. значение свойства
[Tessa.UI.Cards.IControlViewModel.Focusable] равно true.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsGroupsExpanded](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_IsGroupsExpanded.htm)|
Признак свернутости\развернутости групп в представлении  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[IsReadOnly](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsReadOnly.htm)|
Признак того, что элемент управления доступен только для чтения или не
содержит редактируемых данных. Для контрола "Кнопка" разрешает или запрещает
нажатие по кнопке.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsRequired](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsRequired.htm)|
Признак того, что элемент управления отмечен, как обязательный для заполнения.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsSpanned](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsSpanned.htm)|
Признак того, что элемент управления должен быть растянут на ширину колонки
при выводе в несколько колонок.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsUnloaded](P_Tessa_UI_SupportUnloadingViewModel_IsUnloaded.htm)|  Признак
того, что объект был выгружен и уже не может использоваться в UI. Например,
если объект является контролом карточки, то он становится выгруженным после
закрытия формы редактирования строки или пре рефреше карточки.  
(Унаследован от
[SupportUnloadingViewModel](T_Tessa_UI_SupportUnloadingViewModel.htm))  
[IsVisibilityRearranged](P_Tessa_UI_Cards_Controls_ControlViewModelBase_IsVisibilityRearranged.htm)|
Признак того, что видимость элемента управления была изменена в процессе
перерисовки содержимого. Поле используется системой и сбрасывается в false при
ручном изменении видимости.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[Item](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Item.htm)|  Сообщение об
ошибке, связанное со свойством текущего объекта, или null, если ошибки нет.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[KeyDownHandlers](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_KeyDownHandlers.htm)|
Список методов, выполняющихся при обработке нажатия клавиши.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[LeftButtonClickCommand](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_LeftButtonClickCommand.htm)|
Команда обрабатывающая нажатие правой кнопки мыши на элемент таблицы  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[LeftItems](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_LeftItems.htm)|
Дополнительные элементы отображаемые слева от основного содержимого.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Margin](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Margin.htm)|  Заданный
в настройках отступ элемента управления относительно других элементов
управления. По умолчанию отступ отсутствует. Если по одному из направлений
(слева, сверху и пр.) задано отрицательное значение, то по этому направлению
отступ не отображается (т.е. равен 0).  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[MasterContext](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MasterContext.htm)|
Контекст мастер-представления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MasterControl](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MasterControl.htm)|
Мастер-контрол предствлаения  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MaxResultsCount](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MaxResultsCount.htm)|
Gets or sets the max results count.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MaxWidth](P_Tessa_UI_Cards_Controls_ControlViewModelBase_MaxWidth.htm)|
Максимальная ширина контрола. По умолчанию значение равно
double.PositiveInfinity. Значение не может быть меньше 0. При установке
значения 0 в действительности устанавливается double.PositiveInfinity, т.к. в
настройках контрола 0 эквивалентно отсутствию ограничения на контрол.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[MenuActionGenerator](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MenuContext](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MenuContext.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MiddleClickCommand](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MiddleClickCommand.htm)|
Gets or sets the middle click command.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MinRowHeight](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_MinRowHeight.htm)|
Минимальная высота создаваемой строки. По умолчанию равна 0.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MinWidth](P_Tessa_UI_Cards_Controls_ControlViewModelBase_MinWidth.htm)|
Минимальная ширина контрола. По умолчанию значение равно 0 и не может быть
меньше.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ModifyRowActions](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ModifyRowActions.htm)|
Список модификацией, которые будут применены к каждой строке сразу после ее
инициализации  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Name](P_Tessa_UI_Cards_Controls_ControlViewModelBase_Name.htm)|  Имя элемента
управления, по которому он доступен в коллекции, или null, если у элемента
управления не задано имя.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[OptionalPagingStatus](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_OptionalPagingStatus.htm)|
Gets or sets a value indicating whether Статус режима опционального пейджинга  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[PageCount](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_PageCount.htm)|
Gets Количество страниц в источнике данных.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[PageCountStatus](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_PageCountStatus.htm)|
Gets a value indicating whether Признак отображения количества страниц  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[PagingMode](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_PagingMode.htm)|
Gets Возвращает поддерживаемый режим пейджинга  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Parameters](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Parameters.htm)|
Список параметров  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ParametersActions](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ParametersActions.htm)|
Действия над коллекцией параметров  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ParametersSetName](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ParametersSetName.htm)|
Gets Имя набора параметров  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[RefreshDelay](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_RefreshDelay.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[RequiredText](P_Tessa_UI_Cards_Controls_ControlViewModelBase_RequiredText.htm)|
Текст валидации обязательного для заполнения элемента.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[RightButtonClickCommand](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_RightButtonClickCommand.htm)|
Команда обрабатывающая нажатие правой кнопки мыши на элемент таблицы  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[RightItems](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_RightItems.htm)|
Дополнительные элементы отображаемые справа от основного содержимого.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[RowContextMenuGenerators](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_RowContextMenuGenerators.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Rows](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Rows.htm)|  Список
строк  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedCell](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedCell.htm)|
Выбранная ячейка  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedColumn](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedColumn.htm)|
Выбранный столбец  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedColumnName](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedColumnName.htm)|
Имя выбранного столбца  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedRow](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedRow.htm)|
Выбранная строка  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedRowData](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedRowData.htm)|
Выбранная строка в мастер-представлении или null  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SelectedRows](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedRows.htm)|
Список выбранных строк  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Sorting](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Sorting.htm)|
Текущая сортировка  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[StartAtNewLine](P_Tessa_UI_Cards_Controls_ControlViewModelBase_StartAtNewLine.htm)|
Признак того, что текущий контрол в блоке всегда начинается с новой строки.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[Table](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_Table.htm)|  Модель
таблицы данных  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ToolTip](P_Tessa_UI_Cards_Controls_ControlViewModelBase_ToolTip.htm)|
Всплывающая подсказка для элемента управления или null, если подсказка
отсутствует. Пустая строка или строка, состоящая из пробелов, присваивается
как null.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[TopContent](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_TopContent.htm)|
Отображаемое содержимое над основным содержимым  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[TopContentVisible](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_TopContentVisible.htm)|
Признак отображения верхнего содержимого  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[TopItems](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_TopItems.htm)|
Дополнительные элементы над таблицей  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[UIContextExecutorAsync](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_UIContextExecutorAsync.htm)|
Делегат, выполняющий заданное действие в контексте [Tessa.UI.IUIContext].  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[UILockNotifier](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_UILockNotifier.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ValidationFunc](P_Tessa_UI_Cards_Controls_ControlViewModelBase_ValidationFunc.htm)|
Функция валидации, проверяющая элемент управления на корректность его
значения, или null, если дополнительные проверки значения отсутствуют.
Проверка на незаполненное значение всё равно выполняется, если элемент
управления был отмечен как обязательный для заполнения (в т.ч. посредством
валидатора). Для использования функции на элементе управления должна быть
включена валидация [Tessa.UI.Cards.IControlViewModel.HasActiveValidation].  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[VerticalAlignment](P_Tessa_UI_Cards_Controls_ControlViewModelBase_VerticalAlignment.htm)|
Выравнивание контрола по вертикали. По умолчанию контрол выравнивается по
высоте Stretch.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ViewControlIsInitialized](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ViewControlIsInitialized.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ViewMapping](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ViewMapping.htm)|
Настройки маппинга.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ViewMetadata](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_ViewMetadata.htm)|
Метаданные представления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
##  __Методы
[ApplyClientQuickSearch](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_ApplyClientQuickSearch.htm)|
Перегузка дефолтного клиентского поиска. Так как клиентский поиск должен
работать с пейджингом, филтрация происходит в
[InternalRefreshAsync(IDisposable)](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_InternalRefreshAsync.htm),
а не в фильтре [TreeCollectionView](T_Tessa_UI_Data_TreeCollectionView.htm).  
(Переопределяет
[CardViewControlViewModel.ApplyClientQuickSearch(String)](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_ApplyClientQuickSearch.htm))  
---|---  
[CommitChangesAsync](M_Tessa_UI_Cards_Controls_ControlViewModelBase_CommitChangesAsync.htm)|
Подтверждает изменения для текущего элемента управления. Метод обычно
вызывается перед сохранением карточки для того, чтобы элементы управления, у
которых состояние ввода зависит от фокуса и других параметров, могли
подтвердить введённое значение перед тем, как карточка будет сохранена. Если
при выполнении этого метода возникнет исключение, то оно будет зафиксировано в
результате.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CreateParametersSettings](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_CreateParametersSettings.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[DeleteRowsAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_DeleteRowsAsync.htm)|
Удаляет заданные строки с учётом визуальных изменений в контроле. При этом
выполняются обработчики события
[RowInvoked](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInvoked.htm),
которые могут запретить удаление некоторых строк или вывести на экран окна с
ошибками. Укажите
[SelectedRows](P_Tessa_UI_Cards_Controls_CardViewControlViewModel_SelectedRows.htm),
чтобы удалить выбранные строки (аналогично соответствующей кнопке в контроле).  
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
[Focus](M_Tessa_UI_Cards_Controls_ControlViewModelBase_Focus.htm)|
Устанавливает логический фокус на текущий элемент управления, если он
поддерживает логический фокус, т.е. значение свойства
[Tessa.UI.Cards.IControlViewModel.Focusable] равно true. Если элемент
управления недоступен или не поддерживает логический фокус, то метод
возвращает значение false.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[GetContextMenuAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_GetContextMenuAsync.htm)|
Возвращает контекстное меню, доступное для текущей модели представления. Если
возвращается null, пустая коллекция или коллекция из скрытых элементов, то
меню при этом не отображается.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetState](M_Tessa_UI_Cards_Controls_ControlViewModelBase_GetState.htm)|
Возвращает текущее состояние элемента управления. Может вернуть null, если
элемент управления не имеет состояния.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasEmptyValue](M_Tessa_UI_Cards_Controls_ControlViewModelBase_HasEmptyValue.htm)|
Возвращает признак того, что элемент управления имеет пустое значение.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[InitializeAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_InitializeAsync.htm)|  
(Переопределяет
[CardViewControlViewModel.InitializeAsync(IUILockNotifier)](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeAsync.htm))  
[InitializeCoreAsync](M_Tessa_UI_Cards_Controls_ControlViewModelBase_InitializeCoreAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[InitializeEventsSubscriptions](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeEventsSubscriptions.htm)|
Осуществляет инициализацию подписки на события  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InitializeMasterLinks](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeMasterLinks.htm)|
The initialize master links.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InitializeOnTabAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeOnTabAsync.htm)|
Отображает элементы графического интерфейса на вкладке. Используется, когда
представления программное и иниициализация стратегии произошла после
инициализации на вкладке стандартными средствами.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InitializeOtherViewControlsAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeOtherViewControlsAsync.htm)|
Осуществляет вызов инициализации элементов отображения представлений в
карточке. По принципу кто первый встал тот и тапки греет. Необходимо для
корректной инициализации ссылок на мастер представления. Т.к. мастер
представление может быть не доступно на момент создания элемента отображения
представления использующего его.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InitializeStrategyAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InitializeStrategyAsync.htm)|
Инициализирует стратегию создания ViewModelи представления. DataProvider можно
установить через свойство CardViewControlViewModel.DataProvider.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InPagingMode](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InPagingMode.htm)|  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[InternalRefreshAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_InternalRefreshAsync.htm)|
Новый рефреш представления с учетом того, что это теперь таблица.  
(Переопределяет
[CardViewControlViewModel.InternalRefreshAsync(IDisposable)](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InternalRefreshAsync.htm))  
[InvalidateAutoSize](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_InvalidateAutoSize.htm)|
Перерассчитывает ширину колонок если включена автоширина.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[NotifyTabDeselectedAsync](M_Tessa_UI_Cards_Controls_ControlViewModelBase_NotifyTabDeselectedAsync.htm)|
Уведомляет текущий объект и все его дочерние объекты о том, что он
располагался на выбранной вкладке, после чего выбрали другую вкладку.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[NotifyTabSelectedAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_NotifyTabSelectedAsync.htm)|  
(Переопределяет
[CardViewControlViewModel.NotifyTabSelectedAsync(ITabSelectedContext,
CancellationToken)](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_NotifyTabSelectedAsync.htm))  
[NotifyUpdateValidation](M_Tessa_UI_Cards_Controls_ControlViewModelBase_NotifyUpdateValidation.htm)|
Уведомляет об изменении всех свойств, связанных с валидацией в элементе
управления, даже если эти свойства не были изменены.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_OnPropertyChanged.htm)|  
(Переопределяет
[NotificationObject.OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_UI_NotificationUIObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnRefreshCompletedAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_OnRefreshCompletedAsync.htm)|
Метод, вызываемый после обновления представления вместе с объектами UI
(колонками и строками). Реализация по умолчанию вызывает обработчики события
[Refreshed](E_Tessa_UI_Cards_Controls_CardViewControlViewModel_Refreshed.htm).  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[OnUnloadingAsync](M_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_OnUnloadingAsync.htm)|
Отписываемся от всех событий  
(Переопределяет
[SupportUnloadingViewModel.OnUnloadingAsync(IValidationResultBuilder)](M_Tessa_UI_SupportUnloadingViewModel_OnUnloadingAsync.htm))  
[Rearrange](M_Tessa_UI_Cards_Controls_ControlViewModelBase_Rearrange.htm)|
Выполняет перерисовку содержимого в зависимости от состояния объекта с учётом
дочерних объектов, в т.ч. от видимости дочерних вложенных форм при их наличии.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[RearrangeChildren](M_Tessa_UI_Cards_Controls_ControlViewModelBase_RearrangeChildren.htm)|
Выполняет перерисовку содержимого в зависимости от состояния дочерних
объектов, в т.ч. от видимости дочерних вложенных форм при их наличии.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[RearrangeSelf](M_Tessa_UI_Cards_Controls_ControlViewModelBase_RearrangeSelf.htm)|
Выполняет перерисовку содержимого в зависимости от состояния объекта без учёта
дочерних объектов.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[RefreshAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_RefreshAsync.htm)|
Вызывает обновление данных из представления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[SetBlock](M_Tessa_UI_Cards_Controls_ControlViewModelBase_SetBlock.htm)|
Устанавливает блок, в котором размещён элемент управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[SetStateAsync](M_Tessa_UI_Cards_Controls_ControlViewModelBase_SetStateAsync.htm)|
Устанавливает заданное состояние элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[SortColumnAsync](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_SortColumnAsync.htm)|
Вызывается при сортировке по указанному столбцу  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnloadAsync](M_Tessa_UI_SupportUnloadingViewModel_UnloadAsync.htm)|
Выполняет выгрузку объекта. Если объект уже был выгружен, то повторная
выгрузка не выполняется.  
(Унаследован от
[SupportUnloadingViewModel](T_Tessa_UI_SupportUnloadingViewModel.htm))  
[UpdatePageCount](M_Tessa_UI_Cards_Controls_CardViewControlViewModel_UpdatePageCount.htm)|
Обновляет количество страниц  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
[Refreshed](E_Tessa_UI_Cards_Controls_CardViewControlViewModel_Refreshed.htm)|
Событие, вызываемое после обновления представления. В нём можно изменять
модели представлений строк и колонок.  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[Refreshing](E_Tessa_UI_Cards_Controls_CardViewControlViewModel_Refreshing.htm)|
Событие обновления  
(Унаследован от
[CardViewControlViewModel](T_Tessa_UI_Cards_Controls_CardViewControlViewModel.htm))  
[RowAdding](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowAdding.htm)|
Событие, возникающее перед вставкой новой строки в таблицу.  
[RowChanged](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowChanged.htm)|
Событие, возникающее при изменении строки секции, от которой зависят строки
таблицы.  
[RowEditorClosed](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowEditorClosed.htm)|
Событие, происходящее при закрытии редактора для строки таблицы, который может
быть открыт при создании строки или при открытии существующей строки. Событие
вызывается как при закрытии с сохранением строки, так и при отмене. Обработчик
события обычно удаляет подписки, добавленные в
[RowInitializing](E_Tessa_UI_Cards_Controls_GridViewModel_RowInitializing.htm).
Через аргументы этого события нельзя отменить закрытие строки, для этого
используйте событие
[RowEditorClosing](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowEditorClosing.htm).  
[RowEditorClosing](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowEditorClosing.htm)|
Событие, происходящее при закрытии редактора для строки таблицы, который может
быть открыт при создании строки или при открытии существующей строки. При
создании строки событие вызывается только при сохранении строки (но не при
отмене), причём проверка строки валидаторами вызываются после срабатывания
события. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) установлено равным true, то закрытие не
будет выполнено.  
[RowInitializing](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInitializing.htm)|
Событие, происходящее при инициализации окна для строки таблицы, а именно при
создании строки или при открытии существующей строки. Событие вызывается
непосредственно перед тем, как окно будет открыто. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) установлено равным true, то открытие
окна будет отменено.  
[RowInvoked](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowInvoked.htm)|
Событие, происходящее при выполнении действий со строкой таблицы, а именно при
создании строки, открытии существующей строки и удалении строки. Если свойство
[Cancel](https://learn.microsoft.com/dotnet/api/system.componentmodel.canceleventargs.cancel#system-
componentmodel-canceleventargs-cancel) установлено равным true, то действие
будет отменено.  
[RowValidating](E_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel_RowValidating.htm)|
Событие, происходящее при валидации строки перед сохранением или закрытием её
окна редактирования. Если хотя бы один обработчик выбросит исключение, то оно
будет считаться ошибкой валидации.  
[TabDeselected](E_Tessa_UI_Cards_Controls_ControlViewModelBase_TabDeselected.htm)|
Событие, происходящее для объекта, который располагался на выбранной вкладке,
после чего выбрали другую вкладку.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[TabSelected](E_Tessa_UI_Cards_Controls_ControlViewModelBase_TabSelected.htm)|
Событие, происходящее при переходе объекта на выбранную вкладку. Событие для
выбранной вкладки вызывается после того, как было вызвано событие
TabDeselected для вкладки, которая перестала быть выбранной.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[Unloaded](E_Tessa_UI_SupportUnloadingViewModel_Unloaded.htm)|  Событие,
возникающее после того, как объект был выгружен и уже не может использоваться
в UI. Если на некоторые свойства объекта, связанные с UI, выполнялась
подписка, то в обработчике события можно выполнить отписку, а также удалить
сам обработчик.  
(Унаследован от
[SupportUnloadingViewModel](T_Tessa_UI_SupportUnloadingViewModel.htm))  
##  __Поля
[ActualMarginInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_ActualMarginInternal.htm)|
Предпочитаемый отступ элемента управления относительно других элементов
управления, расчитываемый блоком и используемый при отображении. Не
рекомендуется вручную изменять это значение.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
---|---  
[BlockInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_BlockInternal.htm)|
Блок, в котором размещён текущий элемент управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CaptionInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_CaptionInternal.htm)|
Заголовок элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[CaptionVisibilityInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_CaptionVisibilityInternal.htm)|
Видимость заголовка элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ColumnSpanInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_ColumnSpanInternal.htm)|
Количество колонок, которые занимает контрол по горизонтали. Неактуально для
контролов, растягиваемых по ширине всей строки. По умолчанию значение равно 1
и не может быть меньше. Если заданное количество колонок больше, чем общее
количество колонок в блоке, то контрол растягивается на ширину строки.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ControlVisibilityInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_ControlVisibilityInternal.htm)|
Видимость элемента управления.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[EmptyColumnsToTheLeftInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_EmptyColumnsToTheLeftInternal.htm)|
Количество пустых колонок, которые отображаются слева от контрола. Неактуально
для контролов, растягиваемых по ширине всей строки. По умолчанию значение
равно 0 и не может быть меньше. Если заданное количество колонок больше, чем
количество колонок в блоке минус количество колонок, занимаемых контролом, то
отрисовывается столько пустых колонок, сколько умещается в строке. Если
контрол рисуется не с начала строки, и он не умещается вместе с заданным
отступом, то он переносится на следующую строку.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[HasActiveValidationInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_HasActiveValidationInternal.htm)|
Признак того, что в элементе управления следует включить активную валидацию.
При этом если для элемента управления введено некорректное значение, то он
будет уведомлять об этом рамкой валидации. Значение устанавливливается равным
true обычно после неудачного сохранения карточки. По умолчанию значение равно
false.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[HorizontalAlignmentInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_HorizontalAlignmentInternal.htm)|
Выравнивание контрола по горизонтали. По умолчанию контрол выравнивается по
ширине Stretch.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsReadOnlyInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_IsReadOnlyInternal.htm)|
Признак того, что элемент управления доступен только для чтения или не
содержит редактируемых данных. Для контрола "Кнопка" разрешает или запрещает
нажатие по кнопке.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsRequiredInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_IsRequiredInternal.htm)|
Признак того, что элемент управления отмечен, как обязательный для заполнения.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[IsSpannedInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_IsSpannedInternal.htm)|
Признак того, что элемент управления должен быть растянут на ширину колонки
при выводе в несколько колонок.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[MarginInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_MarginInternal.htm)|
Заданный в настройках отступ элемента управления относительно других элементов
управления. По умолчанию отступ отсутствует. Если по одному из направлений
(слева, сверху и пр.) задано отрицательное значение, то по этому направлению
отступ не отображается (т.е. равен 0).  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[MaxWidthInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_MaxWidthInternal.htm)|
Максимальная ширина контрола. По умолчанию значение равно
double.PositiveInfinity. Значение не может быть меньше 0. При установке
значения 0 в действительности устанавливается double.PositiveInfinity, т.к. в
настройках контрола 0 эквивалентно отсутствию ограничения на контрол.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[MinWidthInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_MinWidthInternal.htm)|
Минимальная ширина контрола. По умолчанию значение равно 0 и не может быть
меньше.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[StartAtNewLineInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_StartAtNewLineInternal.htm)|
Признак того, что текущий контрол в блоке всегда начинается с новой строки.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ToolTipInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_ToolTipInternal.htm)|
Всплывающая подсказка для элемента управления или null, если подсказка
отсутствует. Пустая строка или строка, состоящая из пробелов, присваивается
как null.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[ValidationFuncInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_ValidationFuncInternal.htm)|
Признак того, что в элементе управления следует включить активную валидацию.
При этом если для элемента управления введено некорректное значение, то он
будет уведомлять об этом рамкой валидации. Значение устанавливливается равным
true обычно после неудачного сохранения карточки. По умолчанию значение равно
false.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
[VerticalAlignmentInternal](F_Tessa_UI_Cards_Controls_ControlViewModelBase_VerticalAlignmentInternal.htm)|
Выравнивание контрола по вертикали. По умолчанию контрол выравнивается по
высоте Stretch.  
(Унаследован от
[ControlViewModelBase](T_Tessa_UI_Cards_Controls_ControlViewModelBase.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
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
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
