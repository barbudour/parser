# IPreviewHandlerProxy - интерфейс
Описание интерфейса обработчика предварительного просмотра
## __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPreviewHandlerProxy : IAsyncDisposable
VB __Копировать
     Public Interface IPreviewHandlerProxy
    	Inherits IAsyncDisposable
C++ __Копировать
     public interface class IPreviewHandlerProxy : IAsyncDisposable
F# __Копировать
     type IPreviewHandlerProxy = 
        interface
            interface IAsyncDisposable
        end
Implements
    [IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable)
##  __Свойства
[Is64BitProcess](P_Tessa_PreviewHandlers_IPreviewHandlerProxy_Is64BitProcess.htm)|
Признак того, что обработчик предпросмотра 64-битный.  
---|---  
## __Методы
[CloseAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_CloseAsync.htm)|
Закрывает приложение  
---|---  
[DisposeAsync](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable.disposeasync#system-
iasyncdisposable-disposeasync)| Performs application-defined tasks associated
with freeing, releasing, or resetting unmanaged resources asynchronously.  
(Унаследован от
[IAsyncDisposable](https://learn.microsoft.com/dotnet/api/system.iasyncdisposable))  
[DoPreviewAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_DoPreviewAsync.htm)|
Осуществляет запуск предварительного просмотра  
[InFailedState](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_InFailedState.htm)|
Возвращает признак нахождения объекта в состоянии ошибки  
[SetFileAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_SetFileAsync.htm)|
Устанавливает путь к файлу и возвращает результат запуска. Если значение
result вернуло false, то запуск не поддерживается и значение exceptionText
может содержать текст исключения, если он доступен. Если значение result
вернуло true, то текст исключения всегда равен null.  
[SetRectAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_SetRectAsync.htm)|
Устанавливает область отображения  
[SetWindowAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_SetWindowAsync.htm)|
Устанавливает область отображения  
[UnloadAsync](M_Tessa_PreviewHandlers_IPreviewHandlerProxy_UnloadAsync.htm)|
Выгружает обработчик  
## __События
[Faulted](E_Tessa_PreviewHandlers_IPreviewHandlerProxy_Faulted.htm)|  Событие
происходящее при сбое в хэндлере  
---|---  
[ProcessExited](E_Tessa_PreviewHandlers_IPreviewHandlerProxy_ProcessExited.htm)|
Событие происходящее при завершении приложения  
## __См. также
#### Ссылки
[Tessa.PreviewHandlers - пространство имён](N_Tessa_PreviewHandlers.htm)
