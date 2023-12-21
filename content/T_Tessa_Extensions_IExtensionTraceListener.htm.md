# IExtensionTraceListener - интерфейс
Объект, выполняющий отслеживание событий, происходящих при выполнении
расширений.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IExtensionTraceListener
VB __Копировать
     Public Interface IExtensionTraceListener
C++ __Копировать
     public interface class IExtensionTraceListener
F# __Копировать
     type IExtensionTraceListener = interface end
##  __Методы
[NotifyException](M_Tessa_Extensions_IExtensionTraceListener_NotifyException.htm)|
Уведомляет объект о том, что возникло исключение в процессе выполнения метода
расширения, информацию о котором можно получить из заданного контекста.  
---|---  
[NotifyExecuted](M_Tessa_Extensions_IExtensionTraceListener_NotifyExecuted.htm)|
Уведомляет объект о том, что было завершено выполнение метода расширения,
информацию о котором можно получить из заданного контекста.  
[NotifyExecuting](M_Tessa_Extensions_IExtensionTraceListener_NotifyExecuting.htm)|
Уведомляет объект о том, что следующим шагом будет выполнение метода
расширения, информацию о котором можно получить из заданного контекста.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
