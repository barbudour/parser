# CardTableViewControlViewModel - поля
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
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
