# IExtensionTraceListener.NotifyException - метод
Уведомляет объект о том, что возникло исключение в процессе выполнения метода
расширения, информацию о котором можно получить из заданного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void NotifyException(
    	IExtensionStrategyContext strategyContext
    )
VB __Копировать
     Sub NotifyException ( 
    	strategyContext As IExtensionStrategyContext
    )
C++ __Копировать
     void NotifyException(
    	IExtensionStrategyContext^ strategyContext
    )
F# __Копировать
     abstract NotifyException : 
            strategyContext : IExtensionStrategyContext -> unit 
#### Параметры
strategyContext
[IExtensionStrategyContext](T_Tessa_Extensions_IExtensionStrategyContext.htm)
     Контекст стратегии расширения, содержащий информацию о том, какой метод какого расширения был выполнен. В свойстве [Tessa.Extensions.IExtensionStrategyContext.Exception] будет содержаться объект возникшего исключения. Указав свойство [Tessa.Extensions.IExtensionStrategyContext.ExceptionHandlingMode] можно установить способ обработки исключения после того, как этот метод будет выполнен. 
## __См. также
#### Ссылки
[IExtensionTraceListener - ](T_Tessa_Extensions_IExtensionTraceListener.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
