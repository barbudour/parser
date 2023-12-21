# Tessa.UI.Behaviors - пространство имён
API для использования поведений в элементах управления WPF и стандартные
поведения, применяемые в приложениях TESSA.
##  __Классы
[Behavior](T_Tessa_UI_Behaviors_Behavior.htm)|  
---|---  
[Behavior<T>](T_Tessa_UI_Behaviors_Behavior_1.htm)|  
[BehaviorCollection](T_Tessa_UI_Behaviors_BehaviorCollection.htm)|  
[BorderlessWindowBehavior](T_Tessa_UI_Behaviors_BorderlessWindowBehavior.htm)|
With this class we can make custom window styles.  
[ChangeExpandedOnMiddleMouseDown](T_Tessa_UI_Behaviors_ChangeExpandedOnMiddleMouseDown.htm)|
При нажатии средней кнопкой мыши сворачивает/разворачивает узел дерева, по
которому был выполнен клик.  
[ChangeFocusOnDisabling](T_Tessa_UI_Behaviors_ChangeFocusOnDisabling.htm)|
Поведение, выполняющее переключение активного фокуса с текущего элемента на
элемент
[FocusElement](P_Tessa_UI_Behaviors_ChangeFocusOnDisabling_FocusElement.htm)
или первый его элемент, доступный для фокуса, в ситуации, когда текущий
элемент перестаёт быть доступным.  
[CollectionBinding](T_Tessa_UI_Behaviors_CollectionBinding.htm)|  
[ColumnCommand](T_Tessa_UI_Behaviors_ColumnCommand.htm)|  
[ColumnCommandCollection](T_Tessa_UI_Behaviors_ColumnCommandCollection.htm)|  
[CommandOnContainerCellEvent](T_Tessa_UI_Behaviors_CommandOnContainerCellEvent.htm)|  
[CommandOnContainerEvent](T_Tessa_UI_Behaviors_CommandOnContainerEvent.htm)|  
[CommandOnEvent](T_Tessa_UI_Behaviors_CommandOnEvent.htm)|  
[CommandOnEventBehaviorBase](T_Tessa_UI_Behaviors_CommandOnEventBehaviorBase.htm)|  
[ContextMenu](T_Tessa_UI_Behaviors_ContextMenu.htm)|  Поведение, отображающее
контекстное меню по правой клавише мыши, если по логическому дереву элементов,
в котором произошёл клик, в свойстве DataContext можно найти объект,
реализующий интерфейс
[IContextMenuProvider](T_Tessa_UI_Menu_IContextMenuProvider.htm).  
[DelegatedCommandBinding](T_Tessa_UI_Behaviors_DelegatedCommandBinding.htm)|  
[DisableOnValidationErrors](T_Tessa_UI_Behaviors_DisableOnValidationErrors.htm)|  
[ExpandGroupsOnMouseButtonDown](T_Tessa_UI_Behaviors_ExpandGroupsOnMouseButtonDown.htm)|  
[Focusable](T_Tessa_UI_Behaviors_Focusable.htm)|  
[HorizontalScrollRatio](T_Tessa_UI_Behaviors_HorizontalScrollRatio.htm)|  
[HorizontalWheelScroll](T_Tessa_UI_Behaviors_HorizontalWheelScroll.htm)|  
[IgnoreMouseWheel](T_Tessa_UI_Behaviors_IgnoreMouseWheel.htm)|  
[Interaction](T_Tessa_UI_Behaviors_Interaction.htm)|  
[LanguageBinding](T_Tessa_UI_Behaviors_LanguageBinding.htm)|  Поведение,
добавляющее возможность создавать привязку для свойства
[Language](https://learn.microsoft.com/dotnet/api/system.windows.frameworkelement.language#system-
windows-frameworkelement-language).  
[MinWidthSplitterBehavior](T_Tessa_UI_Behaviors_MinWidthSplitterBehavior.htm)|  
[MouseWheelFontResize](T_Tessa_UI_Behaviors_MouseWheelFontResize.htm)|  
[PasswordBinding](T_Tessa_UI_Behaviors_PasswordBinding.htm)|  Поведение,
добавляющее возможность связать введённый пароль с полем в модели
представления через Binding. При использовании сохранность пароля в памяти
клиентского компьютера может быть нарушена.  
[PreviewKeyDown](T_Tessa_UI_Behaviors_PreviewKeyDown.htm)|  Реагирует при
нажатии клавиши по событию
[PreviewKeyDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.previewkeydown)
и выполняет заданную команду.  
[ReadOnlyText](T_Tessa_UI_Behaviors_ReadOnlyText.htm)|  Определяет для
контролов, содержащих текст, свойство
[IsReadOnly](P_Tessa_UI_Behaviors_ReadOnlyText_IsReadOnly.htm), эмулирующее
режим "ReadOnly" в таких контролах, как
[TextBox](https://learn.microsoft.com/dotnet/api/system.windows.controls.textbox).
При этом не изменяется цвет фона контрола, цвет (видимость) каретки и
контекстное меню, такие изменения может потребоваться выполнить отдельно через
стили.  
[SavePlacement](T_Tessa_UI_Behaviors_SavePlacement.htm)|  
[ScrollIntoViewBehavior](T_Tessa_UI_Behaviors_ScrollIntoViewBehavior.htm)|  
[ScrollRatioBehaviorBase](T_Tessa_UI_Behaviors_ScrollRatioBehaviorBase.htm)|  
[ScrollSelectedIntoView](T_Tessa_UI_Behaviors_ScrollSelectedIntoView.htm)|  
[ScrollViewerBehaviorBase](T_Tessa_UI_Behaviors_ScrollViewerBehaviorBase.htm)|  
[ScrollViewerVisibility](T_Tessa_UI_Behaviors_ScrollViewerVisibility.htm)|  
[SelectAll](T_Tessa_UI_Behaviors_SelectAll.htm)|  Поведение предоставляет
команду, позволяющую выделить весь текст в контроле. Поддерживаются контролы
[TextBoxBase](https://learn.microsoft.com/dotnet/api/system.windows.controls.primitives.textboxbase)
(в т.ч.
[TextBox](https://learn.microsoft.com/dotnet/api/system.windows.controls.textbox)
и
[RichTextBox](https://learn.microsoft.com/dotnet/api/system.windows.controls.richtextbox)),
[PasswordBox](https://learn.microsoft.com/dotnet/api/system.windows.controls.passwordbox)
и TextEditor (Avalon).  
[SelectItemOnPreviewMouseDown](T_Tessa_UI_Behaviors_SelectItemOnPreviewMouseDown.htm)|
При нажатии любой кнопки мыши в обработчике
[MouseDown](https://learn.microsoft.com/dotnet/api/system.windows.uielement.mousedown)
выполняется выбор элемента таким же образом, как при левом клике, для
элементов управления, унаследованных от
[TreeView](https://learn.microsoft.com/dotnet/api/system.windows.controls.treeview)
или
[Selector](https://learn.microsoft.com/dotnet/api/system.windows.controls.primitives.selector).
Для последних элементы списка должны быть наследниками класса
[ListBoxItem](https://learn.microsoft.com/dotnet/api/system.windows.controls.listboxitem).  
[SelectRowFromViewModel](T_Tessa_UI_Behaviors_SelectRowFromViewModel.htm)|
Добавляет привязку к событию выбора строки контрола "Таблица" из вьюмодели
строки в вью. TwoWay биндинг ломает виртуализацию, поэтому обратная привязка
реализована через данный Behavior.  
[ShowInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowInTaskbarWhenDeactivated.htm)|  
[ShowSplashInTaskbarWhenDeactivated](T_Tessa_UI_Behaviors_ShowSplashInTaskbarWhenDeactivated.htm)|  
[StoryboardBehavior](T_Tessa_UI_Behaviors_StoryboardBehavior.htm)|  
[UpdateSourceBeforeKeyBinding](T_Tessa_UI_Behaviors_UpdateSourceBeforeKeyBinding.htm)|  
[ValidationTarget](T_Tessa_UI_Behaviors_ValidationTarget.htm)|  
[VerticalScrollRatio](T_Tessa_UI_Behaviors_VerticalScrollRatio.htm)|  
[VerticalWheelScroll](T_Tessa_UI_Behaviors_VerticalWheelScroll.htm)|  
[WindowDragMove](T_Tessa_UI_Behaviors_WindowDragMove.htm)|
