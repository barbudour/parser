# UIDialog - класс
Диалоговое окно.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UIDialog : WorkspaceModel
VB __Копировать
     Public NotInheritable Class UIDialog
    	Inherits WorkspaceModel
C++ __Копировать
     public ref class UIDialog sealed : public WorkspaceModel
F# __Копировать
     [<SealedAttribute>]
    type UIDialog = 
        class
            inherit WorkspaceModel
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm) __ UIDialog
##  __Конструкторы
[UIDialog](M_Tessa_UI_UIDialog__ctor.htm)|  Создаёт экземпляр класса с
указанием контента и коллекции кнопок диалогового окна.  
---|---  
## __Свойства
[Buttons](P_Tessa_UI_UIDialog_Buttons.htm)|  Кнопки диалогового окна.  
---|---  
[ButtonsMargin](P_Tessa_UI_UIDialog_ButtonsMargin.htm)|  Отступы для нижних
кнопок.  
[CloseCommand](P_Tessa_UI_WorkspaceModel_CloseCommand.htm)| Команда закрытия
рабочей области.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[Content](P_Tessa_UI_UIDialog_Content.htm)|  Контент диалогового окна.  
[IsClosed](P_Tessa_UI_WorkspaceModel_IsClosed.htm)| Признак того, что рабочая
область была закрыта.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
[WindowPadding](P_Tessa_UI_UIDialog_WindowPadding.htm)|  Отступы от края окна.  
## __Методы
[CloseAsync](M_Tessa_UI_WorkspaceModel_CloseAsync.htm)|  Асинхронно закрывает
рабочую область. Возвращает false, если закрытие области было отменено, причём
значение будет возвращено синхронно. Используйте код следующего вида в
обработчике события window.Closing: async (s, e) => { var task =
model.CloseAsync(); e.Cancel = task.IsCompleted && !task.Result; await task; }  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
---|---  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnClosedAsync](M_Tessa_UI_WorkspaceModel_OnClosedAsync.htm)| Происходит при
закрытии рабочей области.  
(Унаследован от [WorkspaceModel](T_Tessa_UI_WorkspaceModel.htm))  
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
