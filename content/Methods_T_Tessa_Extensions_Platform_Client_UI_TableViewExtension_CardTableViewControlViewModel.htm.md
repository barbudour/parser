# CardTableViewControlViewModel - методы
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
[CardTableViewControlViewModel -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_CardTableViewControlViewModel.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
