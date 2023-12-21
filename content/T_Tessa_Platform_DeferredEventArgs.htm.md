# DeferredEventArgs - класс
Аргументы события, обеспечивающие асинхронное ожидание. Используйте метод
[InvokeNullableAsync<T>(EventHandler<T>, Object, T,
CancellationToken)](M_Tessa_Platform_PlatformExtensions_InvokeNullableAsync__1.htm)
для ожидания обработчиков такого события.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DeferredEventArgs : EventArgs
VB __Копировать
     Public Class DeferredEventArgs
    	Inherits EventArgs
C++ __Копировать
     public ref class DeferredEventArgs : public EventArgs
F# __Копировать
     type DeferredEventArgs = 
        class
            inherit EventArgs
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[EventArgs](https://learn.microsoft.com/dotnet/api/system.eventargs) __ DeferredEventArgs
Derived
[Tessa.Applications.Services.PlatformApplication.MessageReceivedEventArgs](T_Tessa_Applications_Services_PlatformApplication_MessageReceivedEventArgs.htm)
[Tessa.Cards.CardContentStoreCompletedEventArgs](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)
[Tessa.Cards.CardOnContentStoringEventArgs](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)
[Tessa.Cards.Numbers.NumberContextEventArgs](T_Tessa_Cards_Numbers_NumberContextEventArgs.htm)
[Tessa.Platform.DeferredCancelEventArgs](T_Tessa_Platform_DeferredCancelEventArgs.htm)
[Tessa.Platform.Placeholders.PlaceholderParsingEventArgs](T_Tessa_Platform_Placeholders_PlaceholderParsingEventArgs.htm)
[Tessa.Platform.Placeholders.PlaceholderReplacementEventArgs](T_Tessa_Platform_Placeholders_PlaceholderReplacementEventArgs.htm)
[Tessa.Platform.Runtime.ApplicationClosingEventArgs](T_Tessa_Platform_Runtime_ApplicationClosingEventArgs.htm)
[Tessa.Platform.Runtime.ApplicationContextDeferredEventArgs](T_Tessa_Platform_Runtime_ApplicationContextDeferredEventArgs.htm)
[Tessa.PreviewHandlers.PreviewFaultedEventArgs](T_Tessa_PreviewHandlers_PreviewFaultedEventArgs.htm)
[Tessa.UI.Cards.CardModelInitializingEventArgs](T_Tessa_UI_Cards_CardModelInitializingEventArgs.htm)
[Tessa.UI.Cards.Controls.GridRowValidationEventArgs](T_Tessa_UI_Cards_Controls_GridRowValidationEventArgs.htm)
[Tessa.UI.Cards.Controls.RowAddingEventArgs](T_Tessa_UI_Cards_Controls_RowAddingEventArgs.htm)
[Tessa.UI.Cards.Controls.RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm)
[Tessa.UI.Cards.TabSelectedEventArgs](T_Tessa_UI_Cards_TabSelectedEventArgs.htm)
[Tessa.UI.Cards.Tasks.TaskNavigationEventArgs](T_Tessa_UI_Cards_Tasks_TaskNavigationEventArgs.htm)
[Tessa.UI.Cards.Tasks.TaskViewModelEventArgs](T_Tessa_UI_Cards_Tasks_TaskViewModelEventArgs.htm)
[Tessa.UI.Files.FileControlEventArgs](T_Tessa_UI_Files_FileControlEventArgs.htm)
[Tessa.UI.Tiles.TileSourceEventArgs](T_Tessa_UI_Tiles_TileSourceEventArgs.htm)
[Tessa.UI.UnloadedEventArgs](T_Tessa_UI_UnloadedEventArgs.htm)
[Tessa.UI.Windows.BackgroundChangedEventArgs](T_Tessa_UI_Windows_BackgroundChangedEventArgs.htm)
Подробнее __Less __
##  __Конструкторы
[DeferredEventArgs](M_Tessa_Platform_DeferredEventArgs__ctor.htm)|
Инициализирует новый экземпляр класса DeferredEventArgs  
---|---  
##  __Методы
[Defer](M_Tessa_Platform_DeferredEventArgs_Defer.htm)|  Возвращает объект,
обеспечивающий ожидание действия. Вызовите метод в блоке using, внутри
которого выполняйте любые ожидания await.  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[IsPropertyChanged](M_Tessa_UI_Controls_PropertyChangedHelper_IsPropertyChanged.htm)|
Проверяет наступление события изменения свойства propertyName  
(Определяется
[PropertyChangedHelper](T_Tessa_UI_Controls_PropertyChangedHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
