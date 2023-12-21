# WorkplaceAdapter - класс
Вкладка отображения рабочего места
## __Definition
 **Пространство имён:** [Tessa.UI.Windows](N_Tessa_UI_Windows.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorkplaceAdapter : ClosingAdapter, 
    	IActivateMarker, IDeactivateMarker, IAsyncInitializable
VB __Копировать
     Public NotInheritable Class WorkplaceAdapter
    	Inherits ClosingAdapter
    	Implements IActivateMarker, IDeactivateMarker, IAsyncInitializable
C++ __Копировать
     public ref class WorkplaceAdapter sealed : public ClosingAdapter, 
    	IActivateMarker, IDeactivateMarker, IAsyncInitializable
F# __Копировать
     [<SealedAttribute>]
    type WorkplaceAdapter = 
        class
            inherit ClosingAdapter
            interface IActivateMarker
            interface IDeactivateMarker
            interface IAsyncInitializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __[AutomationViewModel](T_Tessa_UI_Automation_AutomationViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __[ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm) __ WorkplaceAdapter
Implements
    [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), [IActivateMarker](T_Tessa_UI_Views_IActivateMarker.htm), [IDeactivateMarker](T_Tessa_UI_Views_IDeactivateMarker.htm)
##  __Конструкторы
[WorkplaceAdapter](M_Tessa_UI_Windows_WorkplaceAdapter__ctor.htm)|
Initializes a new instance of the WorkplaceAdapter class.  
---|---  
## __Свойства
[AutomationId](P_Tessa_UI_Automation_AutomationViewModel_1_AutomationId.htm)|
Уникальный идентификатор для автоматизации.  
(Унаследован от
[AutomationViewModel<TModel>](T_Tessa_UI_Automation_AutomationViewModel_1.htm))  
---|---  
[AutomationName](P_Tessa_UI_Automation_AutomationViewModel_1_AutomationName.htm)|
Имя для автоматизации.  
(Унаследован от
[AutomationViewModel<TModel>](T_Tessa_UI_Automation_AutomationViewModel_1.htm))  
[CloseCommand](P_Tessa_UI_Windows_WorkplaceAdapter_CloseCommand.htm)|  Gets
Команда закрытия  
(Переопределяет
[ClosingAdapter.CloseCommand](P_Tessa_UI_Windows_ClosingAdapter_CloseCommand.htm))  
[Content](P_Tessa_UI_Windows_WorkplaceAdapter_Content.htm)|  Gets Содержимое  
(Переопределяет
[ClosingAdapter.Content](P_Tessa_UI_Windows_ClosingAdapter_Content.htm))  
[Context](P_Tessa_UI_Windows_WorkplaceAdapter_Context.htm)|  Gets текущий
контекст вкладки  
(Переопределяет
[ClosingAdapter.Context](P_Tessa_UI_Windows_ClosingAdapter_Context.htm))  
[Header](P_Tessa_UI_Windows_WorkplaceAdapter_Header.htm)|  Gets Заголовок окна  
(Переопределяет
[ClosingAdapter.Header](P_Tessa_UI_Windows_ClosingAdapter_Header.htm))  
[IsCloseButtonEnabled](P_Tessa_UI_Windows_WorkplaceAdapter_IsCloseButtonEnabled.htm)|
Gets a value indicating whether Признак отображения кнопки закрытия  
(Переопределяет
[ClosingAdapter.IsCloseButtonEnabled](P_Tessa_UI_Windows_ClosingAdapter_IsCloseButtonEnabled.htm))  
[MenuActionGenerator](P_Tessa_UI_Windows_ClosingAdapter_MenuActionGenerator.htm)|
Используемый объект [Tessa.UI.Menu.IMenuActionGenerator].  
(Унаследован от [ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm))  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[TabManager](P_Tessa_UI_Windows_ClosingAdapter_TabManager.htm)|  Объект,
выполняющий управление открытыми вкладками.  
(Унаследован от [ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm))  
[TileWorkspace](P_Tessa_UI_Windows_WorkplaceAdapter_TileWorkspace.htm)|
Модель представления для рабочей области с боковыми панелями плиток  
(Переопределяет
[ClosingAdapter.TileWorkspace](P_Tessa_UI_Windows_ClosingAdapter_TileWorkspace.htm))  
[Workplace](P_Tessa_UI_Windows_WorkplaceAdapter_Workplace.htm)|  Gets Модель
рабочего места  
## __Методы
[Activate](M_Tessa_UI_Windows_WorkplaceAdapter_Activate.htm)|  Вызывается при
активации элемента  
---|---  
[CanCloseAsync](M_Tessa_UI_Windows_ClosingAdapter_CanCloseAsync.htm)|
Возвращает сообщение, определяющее причину, по которой окно нельзя закрыть,
или null, если разрешается немедленно закрыть окно. По умолчанию возвращает
null, если метод не был переопределён.  
(Унаследован от [ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm))  
[CloseAsync](M_Tessa_UI_Windows_WorkplaceAdapter_CloseAsync.htm)|  Закрывает
вкладку.  
(Переопределяет [ClosingAdapter.CloseAsync(Boolean,
CancellationToken)](M_Tessa_UI_Windows_ClosingAdapter_CloseAsync.htm))  
[CloseWorkplaceAsync](M_Tessa_UI_Windows_WorkplaceAdapter_CloseWorkplaceAsync.htm)|
Осуществляет закрытие узла, открытого в отдельном окне  
[Deactivate](M_Tessa_UI_Windows_WorkplaceAdapter_Deactivate.htm)|  Вызывается
при деактивации элемента  
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
[GetContextMenuAsync](M_Tessa_UI_Windows_ClosingAdapter_GetContextMenuAsync.htm)|
Возвращает контекстное меню, доступное для текущей модели представления. Если
возвращается null, пустая коллекция или коллекция из скрытых элементов, то
меню при этом не отображается.  
(Унаследован от [ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInputBindings](M_Tessa_UI_Windows_ClosingAdapter_GetInputBindings.htm)|
Коллекция объектов
[InputBinding](https://learn.microsoft.com/dotnet/api/system.windows.input.inputbinding),
связанных с текущей вкладкой.  
(Унаследован от [ClosingAdapter](T_Tessa_UI_Windows_ClosingAdapter.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_UI_Windows_WorkplaceAdapter_InitializeAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnModelPropertyChanged](M_Tessa_UI_ViewModel_1_OnModelPropertyChanged.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
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
[OnReceiveWeakEvent](M_Tessa_UI_ViewModel_1_OnReceiveWeakEvent.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[Activated](E_Tessa_UI_Windows_WorkplaceAdapter_Activated.htm)|  Событие
активации вкладки  
---|---  
[Deactivated](E_Tessa_UI_Windows_WorkplaceAdapter_Deactivated.htm)|  Событие
деактивации вкладки  
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
##  __Поля
[automationId](F_Tessa_UI_Automation_AutomationViewModel_1_automationId.htm)|  
(Унаследован от
[AutomationViewModel<TModel>](T_Tessa_UI_Automation_AutomationViewModel_1.htm))  
---|---  
[automationName](F_Tessa_UI_Automation_AutomationViewModel_1_automationName.htm)|  
(Унаследован от
[AutomationViewModel<TModel>](T_Tessa_UI_Automation_AutomationViewModel_1.htm))  
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
[Tessa.UI.Windows - пространство имён](N_Tessa_UI_Windows.htm)
