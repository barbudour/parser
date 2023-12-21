# PerformanceTestBaseViewModel - класс
##  __Definition
 **Пространство имён:** [Tessa.UI.Diagnostics](N_Tessa_UI_Diagnostics.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class PerformanceTestBaseViewModel : PerformanceCounterViewModel
VB __Копировать
     Public Class PerformanceTestBaseViewModel
    	Inherits PerformanceCounterViewModel
C++ __Копировать
     public ref class PerformanceTestBaseViewModel : public PerformanceCounterViewModel
F# __Копировать
     type PerformanceTestBaseViewModel = 
        class
            inherit PerformanceCounterViewModel
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[IPerformanceCounter](T_Tessa_Diagnostics_IPerformanceCounter.htm)> __[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm) __ PerformanceTestBaseViewModel
Derived
[Tessa.UI.Diagnostics.PerformanceTestViewModel](T_Tessa_UI_Diagnostics_PerformanceTestViewModel.htm)
##  __Конструкторы
[PerformanceTestBaseViewModel(IPerformanceTest)](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel__ctor.htm)|
Инициализирует новый экземпляр класса PerformanceTestBaseViewModel  
---|---  
[PerformanceTestBaseViewModel(IPerformanceTest,
Dispatcher)](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel__ctor_1.htm)|
Инициализирует новый экземпляр класса PerformanceTestBaseViewModel  
##  __Свойства
[Interval](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Interval.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
---|---  
[IsRunning](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_IsRunning.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Maximum](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Maximum.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Minimum](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Minimum.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Model](P_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_Model.htm)|  
[Name](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Name.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[SampleCapacity](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_SampleCapacity.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[SampleInterval](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_SampleInterval.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Samples](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Samples.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[StartCommand](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_StartCommand.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Status](P_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_Status.htm)|  
[StopCommand](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_StopCommand.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[Value](P_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Value.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
##  __Методы
[CanExecuteStartCommand](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_CanExecuteStartCommand.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
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
[Refresh](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_Refresh.htm)|  
(Переопределяет
[PerformanceCounterViewModel.Refresh()](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Refresh.htm))  
[RefreshOverride](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_RefreshOverride.htm)|  
[Start](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Start.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[StartOverride](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_StartOverride.htm)|  
(Переопределяет
[PerformanceCounterViewModel.StartOverride()](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_StartOverride.htm))  
[Stop](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_Stop.htm)|  
(Унаследован от
[PerformanceCounterViewModel](T_Tessa_UI_Diagnostics_PerformanceCounterViewModel.htm))  
[StopOverride](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_StopOverride.htm)|  
(Переопределяет
[PerformanceCounterViewModel.StopOverride()](M_Tessa_UI_Diagnostics_PerformanceCounterViewModel_StopOverride.htm))  
[StopPerformanceTest](M_Tessa_UI_Diagnostics_PerformanceTestBaseViewModel_StopPerformanceTest.htm)|  
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
[Tessa.UI.Diagnostics - пространство имён](N_Tessa_UI_Diagnostics.htm)
