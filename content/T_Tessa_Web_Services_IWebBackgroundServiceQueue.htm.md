# IWebBackgroundServiceQueue - интерфейс
Очередь действий для асинхронной обработки в фоновом режиме веб-сервером.
## __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWebBackgroundServiceQueue : IBackgroundServiceQueue
VB __Копировать
     Public Interface IWebBackgroundServiceQueue
    	Inherits IBackgroundServiceQueue
C++ __Копировать
     public interface class IWebBackgroundServiceQueue : IBackgroundServiceQueue
F# __Копировать
     type IWebBackgroundServiceQueue = 
        interface
            interface IBackgroundServiceQueue
        end
Implements
    [IBackgroundServiceQueue](T_Tessa_Platform_IBackgroundServiceQueue.htm)
##  __Методы
[DequeAsync](M_Tessa_Web_Services_IWebBackgroundServiceQueue_DequeAsync.htm)|
Возвращает следующее действие для обработки и соответствующий отправке данного
действия контекст обработки. Если на момент вызова метода очередь пустая,
метод будет ожидать, пока в очередь не поместят следующее действие.  
---|---  
[EnqueueAsync](M_Tessa_Platform_IBackgroundServiceQueue_EnqueueAsync.htm)|
Помещает действие в очередь асинхронной обработки в фономов режиме.  
(Унаследован от
[IBackgroundServiceQueue](T_Tessa_Platform_IBackgroundServiceQueue.htm))  
##  __См. также
#### Ссылки
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
