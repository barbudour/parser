# FakeScanProvider - класс
Объект, не выполняющий действий при сканировании. Зарегистрирован по
умолчанию.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FakeScanProvider : ViewModel<EmptyModel>, 
    	IScanProvider, INotifyPropertyChanged, IAsyncDisposable
VB __Копировать
     Public NotInheritable Class FakeScanProvider
    	Inherits ViewModel(Of EmptyModel)
    	Implements IScanProvider, INotifyPropertyChanged, IAsyncDisposable
C++ __Копировать
     public ref class FakeScanProvider sealed : public ViewModel<EmptyModel^>, 
    	IScanProvider, INotifyPropertyChanged, IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type FakeScanProvider = 
        class
            inherit ViewModel<EmptyModel>
            interface IScanProvider
            interface INotifyPropertyChanged
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __ FakeScanProvider
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IScanProvider](T_Tessa_Extensions_Platform_Client_Scanning_IScanProvider.htm)
##  __Конструкторы
[FakeScanProvider](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider__ctor.htm)|
Инициализирует новый экземпляр класса FakeScanProvider  
---|---  
##  __Свойства
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
---|---  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[State](P_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_State.htm)|
Текущее состояние сканирования  
## __Методы
[CancelAsync](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_CancelAsync.htm)|
Вызывает отмену сканирования  
---|---  
[DisposeAsync](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_DisposeAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
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
[GetSourcesAsync](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_GetSourcesAsync.htm)|
Возвращает список доступных источников сканирования. Значение null аналогично
пустому списку.  
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
[ScanAsync](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_ScanAsync.htm)|
Запускает сканирование для заданного источника. Возвращает признак того, что
сканирование было запущено и отсутствовали ошибки при запуске. Ошибки
выводятся на экран средствами текущего объекта.  
[SetProcessAction](M_Tessa_Extensions_Platform_Client_Scanning_FakeScanProvider_SetProcessAction.htm)|
Устанавливает функцию, вызываемую для отсканированной страницы.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
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
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
