# WebChartSettingsViewModel - класс
Модель-представление для редактирования настроек веб-диаграмм
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Workplaces.WebChart](N_Tessa_Extensions_Default_Client_Workplaces_WebChart.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebChartSettingsViewModel : ViewModel<EmptyModel>
VB __Копировать
     Public NotInheritable Class WebChartSettingsViewModel
    	Inherits ViewModel(Of EmptyModel)
C++ __Копировать
     public ref class WebChartSettingsViewModel sealed : public ViewModel<EmptyModel^>
F# __Копировать
     [<SealedAttribute>]
    type WebChartSettingsViewModel = 
        class
            inherit ViewModel<EmptyModel>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __[NotificationUIObject](T_Tessa_UI_NotificationUIObject.htm) __[ViewModel](T_Tessa_UI_ViewModel_1.htm)<[EmptyModel](T_Tessa_UI_EmptyModel.htm)> __ WebChartSettingsViewModel
##  __Конструкторы
[WebChartSettingsViewModel](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel__ctor.htm)|
Инициализирует новый экземпляр класса WebChartSettingsViewModel  
---|---  
##  __Свойства
[Caption](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_Caption.htm)|  
---|---  
[CaptionColumn](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_CaptionColumn.htm)|  
[ColumnCount](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_ColumnCount.htm)|  
[ColumnNames](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_ColumnNames.htm)|
Gets Список доступных для выборки столбцов  
[DiagramDirection](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_DiagramDirection.htm)|  
[DiagramDirections](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_DiagramDirections.htm)|  
[DiagramType](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_DiagramType.htm)|
Gets or sets Тип диаграммы  
[DiagramTypes](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_DiagramTypes.htm)|  
[DoesntShowZeroValues](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_DoesntShowZeroValues.htm)|  
[LegendItemMinWidth](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_LegendItemMinWidth.htm)|  
[LegendNotWrap](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_LegendNotWrap.htm)|  
[LegendPosition](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_LegendPosition.htm)|  
[LegendPositions](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_LegendPositions.htm)|  
[Model](P_Tessa_UI_ViewModel_1_Model.htm)|  Модель для текущей модели
представления.  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[PaletteViewModel](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_PaletteViewModel.htm)|  
[Scope](P_Tessa_UI_ViewModel_1_Scope.htm)|  
(Унаследован от [ViewModel<TModel>](T_Tessa_UI_ViewModel_1.htm))  
[SelectedColor](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_SelectedColor.htm)|  
[SelectedColorViewModel](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_SelectedColorViewModel.htm)|  
[SelectedPaletteTypeId](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_SelectedPaletteTypeId.htm)|  
[XColumn](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_XColumn.htm)|  
[YColumn](P_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_YColumn.htm)|  
## __Методы
[Create](M_Tessa_Extensions_Default_Client_Workplaces_WebChart_WebChartSettingsViewModel_Create.htm)|
Создает модель-представление и инициализирует ее свойства из настроек
задаваемых в параметре settings  
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
[Tessa.Extensions.Default.Client.Workplaces.WebChart - пространство
имён](N_Tessa_Extensions_Default_Client_Workplaces_WebChart.htm)
