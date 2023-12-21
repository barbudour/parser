# PreviewServiceClient - класс
##  __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PreviewServiceClient : IPreviewService, 
    	IAsyncDisposable
VB __Копировать
     Public NotInheritable Class PreviewServiceClient
    	Implements IPreviewService, IAsyncDisposable
C++ __Копировать
     public ref class PreviewServiceClient sealed : IPreviewService, 
    	IAsyncDisposable
F# __Копировать
     [<SealedAttribute>]
    type PreviewServiceClient = 
        class
            interface IPreviewService
            interface IAsyncDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PreviewServiceClient
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable), [IPreviewService](T_Tessa_PreviewHandlers_IPreviewService.htm)
##  __Конструкторы
[PreviewServiceClient](M_Tessa_PreviewHandlers_PreviewServiceClient__ctor.htm)|
Инициализирует новый экземпляр класса PreviewServiceClient  
---|---  
##  __Свойства
[Connection](P_Tessa_PreviewHandlers_PreviewServiceClient_Connection.htm)|  
---|---  
## __Методы
[DisposeAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_DisposeAsync.htm)|  
---|---  
[DoPreviewAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_DoPreviewAsync.htm)|
Осуществляет запуск предварительного просмотра и возвращает результат запуска.
Если значение result вернуло false, то запуск не поддерживается и значение
exceptionText может содержать текст исключения, если он доступен. Если
значение result вернуло true, то текст исключения всегда равен null.  
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
[SetFileAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_SetFileAsync.htm)|
Устанавливает путь к файлу и возвращает результат запуска. Если значение
result вернуло false, то запуск не поддерживается и значение exceptionText
может содержать текст исключения, если он доступен. Если значение result
вернуло true, то текст исключения всегда равен null.  
[SetFocusAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_SetFocusAsync.htm)|
Устанавливает фокус  
[SetPreviewAreaAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_SetPreviewAreaAsync.htm)|
Осуществляет установку позиции элемента отображающего файл относительно окна
приложения  
[SetPreviewAreaWindowAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_SetPreviewAreaWindowAsync.htm)|
Устанавливает указатель окна и область в которой требуется отобразить просмотр
файла.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UnloadAsync](M_Tessa_PreviewHandlers_PreviewServiceClient_UnloadAsync.htm)|
Осуществляет выгрузку приложения  
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
