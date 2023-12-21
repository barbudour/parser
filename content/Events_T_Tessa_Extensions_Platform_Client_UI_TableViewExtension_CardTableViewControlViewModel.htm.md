# CardTableViewControlViewModel - события
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
##  __См. также
#### Ссылки
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
