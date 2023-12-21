# PreviewHandlerProxy - класс
Объект осуществляющий взаимодействие с сервисом просмотра файлов
## __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PreviewHandlerProxy : IPreviewHandlerProxy, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class PreviewHandlerProxy
    	Implements IPreviewHandlerProxy, IAsyncDisposable
C++ __Копировать
     public ref class PreviewHandlerProxy sealed : IPreviewHandlerProxy, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type PreviewHandlerProxy = 
        class
            interface IPreviewHandlerProxy
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PreviewHandlerProxy
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IPreviewHandlerProxy](T_Tessa_PreviewHandlers_IPreviewHandlerProxy.htm)
##  __Конструкторы
[PreviewHandlerProxy](M_Tessa_PreviewHandlers_PreviewHandlerProxy__ctor.htm)|
Initializes a new instance of the PreviewHandlerProxy class.  
---|---  
## __Свойства
[Is64BitProcess](P_Tessa_PreviewHandlers_PreviewHandlerProxy_Is64BitProcess.htm)|
Признак того, что обработчик предпросмотра 64-битный.  
---|---  
## __Методы
[CloseAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_CloseAsync.htm)|
Закрывает приложение  
---|---  
[DisposeAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_DisposeAsync.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources asynchronously.  
[DoPreviewAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_DoPreviewAsync.htm)|
Осуществляет запуск предварительного просмотра  
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
[InFailedState](M_Tessa_PreviewHandlers_PreviewHandlerProxy_InFailedState.htm)|
Возвращает признак нахождения объекта в состоянии ошибки  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetFileAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_SetFileAsync.htm)|
Устанавливает путь к файлу и возвращает результат запуска. Если значение
result вернуло false, то запуск не поддерживается и значение exceptionText
может содержать текст исключения, если он доступен. Если значение result
вернуло true, то текст исключения всегда равен null.  
[SetRectAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_SetRectAsync.htm)|
Устанавливает область отображения  
[SetWindowAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_SetWindowAsync.htm)|
Устанавливает область отображения  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnloadAsync](M_Tessa_PreviewHandlers_PreviewHandlerProxy_UnloadAsync.htm)|
Выгружает обработчик  
## __События
[Faulted](E_Tessa_PreviewHandlers_PreviewHandlerProxy_Faulted.htm)|  Событие
происходящее при сбое в хэндлере  
---|---  
[ProcessExited](E_Tessa_PreviewHandlers_PreviewHandlerProxy_ProcessExited.htm)|
Событие происходящее при завершении приложения  
## __Методы расширения
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
[Tessa.PreviewHandlers - пространство имён](N_Tessa_PreviewHandlers.htm)
