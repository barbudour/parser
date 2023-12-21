# DispatcherService - класс
Вспомогательные методы для диспетчеризации вызовов в потоке UI.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class DispatcherService : IDispatcherService
VB __Копировать
     Public Class DispatcherService
    	Implements IDispatcherService
C++ __Копировать
     public ref class DispatcherService : IDispatcherService
F# __Копировать
     type DispatcherService = 
        class
            interface IDispatcherService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DispatcherService
Implements
    [IDispatcherService](T_Tessa_UI_IDispatcherService.htm)
##  __Конструкторы
[DispatcherService](M_Tessa_UI_DispatcherService__ctor.htm)| Инициализирует
новый экземпляр класса DispatcherService  
---|---  
##  __Методы
[CheckAccess](M_Tessa_UI_DispatcherService_CheckAccess.htm)|  Возвращает
признак того, что код выполняется в потоке диспетчера приложения, т.е. в
основном UI-потоке.  
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
[InvokeInUI(Action)](M_Tessa_UI_DispatcherService_InvokeInUI.htm)|  Выполняет
делегат в потоке UI. Не возвращает управление, пока делегат не будет выполнен.  
[InvokeInUI(Action,
DispatcherPriority)](M_Tessa_UI_DispatcherService_InvokeInUI_1.htm)|
Выполняет делегат в потоке UI. Не возвращает управление, пока делегат не будет
выполнен.  
[InvokeInUIAsync(Action)](M_Tessa_UI_DispatcherService_InvokeInUIAsync.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync(Action,
DispatcherPriority)](M_Tessa_UI_DispatcherService_InvokeInUIAsync_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>)](M_Tessa_UI_DispatcherService_InvokeInUIAsync__1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
[InvokeInUIAsync<T>(Func<T>,
DispatcherPriority)](M_Tessa_UI_DispatcherService_InvokeInUIAsync__1_1.htm)|
Выполняет делегат в потоке UI. Возвращает управление, не дожидаясь его
выполнения.  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
