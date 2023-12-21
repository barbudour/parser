# ScanDialogViewModel - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ScanDialogViewModel : WorkspaceModel, 
    	IAsyncInitializable, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class ScanDialogViewModel
    	Inherits WorkspaceModel
    	Implements IAsyncInitializable, IAsyncDisposable
C++ __Копировать
     public ref class ScanDialogViewModel sealed : public WorkspaceModel, 
    	IAsyncInitializable, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type ScanDialogViewModel = 
        class
            inherit WorkspaceModel
            interface IAsyncInitializable
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm) __ ScanDialogViewModel
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm)
##  __Конструкторы
[ScanDialogViewModel](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel__ctor.htm)|
Инициализирует новый экземпляр класса ScanDialogViewModel  
---|---  
##  __Свойства
[AddFilesCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_AddFilesCommand.htm)|  
---|---  
[CanSelectDocumentType](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_CanSelectDocumentType.htm)|  
[CloseCommand](P_Tessa_UI_WorkspaceModel_CloseCommand.htm)| Команда закрытия
рабочей области.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[ClosingAction](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_ClosingAction.htm)|
Действие при закрытии диалога.  
[DeleteCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DeleteCommand.htm)|  
[DocumentTypes](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DocumentTypes.htm)|  
[DocumentTypeSelectionAvailability](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DocumentTypeSelectionAvailability.htm)|
Доступность выбора типа документа в диалоге сканирования.  
[EditCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_EditCommand.htm)|  
[ExtractFilesCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_ExtractFilesCommand.htm)|  
[HasPagesToGenerate](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_HasPagesToGenerate.htm)|  
[IsClosed](P_Tessa_UI_WorkspaceModel_IsClosed.htm)| Признак того, что рабочая
область была закрыта.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[IsDirty](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_IsDirty.htm)|
Признак того, что диалог содержит изменения, которые надо сохранить.
Используйте метод
[SetIsDirtyAsync(Boolean)](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SetIsDirtyAsync.htm)
для асинхронной установки значения.  
[LastUsedDocumentType](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_LastUsedDocumentType.htm)|  
[MoveDownCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_MoveDownCommand.htm)|  
[MoveUpCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_MoveUpCommand.htm)|  
[Pages](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_Pages.htm)|  
[RefreshCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_RefreshCommand.htm)|  
[RotateLeftCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_RotateLeftCommand.htm)|  
[RotateRightCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_RotateRightCommand.htm)|  
[SaveAndCloseCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SaveAndCloseCommand.htm)|  
[SaveFilesAsCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SaveFilesAsCommand.htm)|  
[ScanCommand](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_ScanCommand.htm)|  
[ScanningIsStopped](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_ScanningIsStopped.htm)|  
[SelectedDocumentType](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SelectedDocumentType.htm)|  
[SelectedPage](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SelectedPage.htm)|  
[SelectedPageImage](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SelectedPageImage.htm)|  
[SelectedSource](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SelectedSource.htm)|
Текущий выбранный сканер.  
[Sources](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_Sources.htm)|
Сканеры.  
[State](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_State.htm)|  
## __Методы
[AddPagesFromFilesAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_AddPagesFromFilesAsync.htm)|  
---|---  
[CloseAsync](M_Tessa_UI_WorkspaceModel_CloseAsync.htm)|  Асинхронно закрывает
рабочую область. Возвращает false, если закрытие области было отменено, причём
значение будет возвращено синхронно. Используйте код следующего вида в
обработчике события window.Closing: async (s, e) => { var task =
model.CloseAsync(); e.Cancel = task.IsCompleted && !task.Result; await task; }  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[DeletePageAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DeletePageAsync.htm)|  
[DeleteSelectedPagesAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DeleteSelectedPagesAsync.htm)|  
[DisposeAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_DisposeAsync.htm)|  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPageTempFiles](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_GetPageTempFiles.htm)|  
[GetSelectedGenerator](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_GetSelectedGenerator.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitializeAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_InitializeAsync.htm)|
Выполняет асинхронную инициализацию объекта.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnClosedAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_OnClosedAsync.htm)|  
(Переопределяет [WorkspaceModel.OnClosedAsync(DeferredEventArgs,
CancellationToken)](M_Tessa_UI_WorkspaceModel_OnClosedAsync.htm))  
[OnClosingAsync](M_Tessa_UI_WorkspaceModel_OnClosingAsync.htm)|  Происходит
перед закрытием рабочей области. На этом этапе закрытие можно отменить,
установив флаг Cancel в аргументах события.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
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
[SetIsClosedAsync](M_Tessa_UI_WorkspaceModel_SetIsClosedAsync.htm)|
Устанавливает признак того, что рабочая область была закрыта.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[SetIsDirtyAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SetIsDirtyAsync.htm)|
Устанавливает значение свойства
[IsDirty](P_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_IsDirty.htm)
асинхронно. Метод можно вызывать не из потока UI.  
[SetSelectedPageAsync](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_SetSelectedPageAsync.htm)|  
[StopScanning](M_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel_StopScanning.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[Closed](E_Tessa_UI_WorkspaceModel_Closed.htm)| Происходит при закрытии
рабочей области.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
---|---  
[Closing](E_Tessa_UI_WorkspaceModel_Closing.htm)| Происходит перед закрытием
рабочей области.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
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
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
