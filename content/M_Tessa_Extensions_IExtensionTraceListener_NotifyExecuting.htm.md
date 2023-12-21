# IExtensionTraceListener.NotifyExecuting - метод
Уведомляет объект о том, что следующим шагом будет выполнение метода
расширения, информацию о котором можно получить из заданного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void NotifyExecuting(
    	IExtensionStrategyContext strategyContext
    )
VB __Копировать
     Sub NotifyExecuting ( 
    	strategyContext As IExtensionStrategyContext
    )
C++ __Копировать
     void NotifyExecuting(
    	IExtensionStrategyContext^ strategyContext
    )
F# __Копировать
     abstract NotifyExecuting : 
            strategyContext : IExtensionStrategyContext -> unit 
#### Параметры
strategyContext
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
     Контекст стратегии расширения, содержащий информацию о том, какой метод какого расширения будет выполнен. 
## __См. также
#### Ссылки
[IExtensionTraceListener - ](T_Tessa_Extensions_IExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
