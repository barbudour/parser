# IExtensionStrategyContext - свойства
##  __Свойства
[BuildKey](P_Tessa_Extensions_IExtensionStrategyContext_BuildKey.htm)|  Ключ,
используемый для идентификации типа расширения. Возвращаемое значение никогда
не равно null.  
---|---  
[ConcreteContexts](P_Tessa_Extensions_IExtensionStrategyContext_ConcreteContexts.htm)|
Список контекстов для экземпляров расширений, доступных на этапе
упорядочивания цепочки типов расширений, или null на прочих этапах.  
[Exception](P_Tessa_Extensions_IExtensionStrategyContext_Exception.htm)|
Исключение, возникшее в процессе выполнения метода расширения, или null, если
метод ещё не был выполнен или расширение не выбросило исключение.  
[ExceptionHandlingMode](P_Tessa_Extensions_IExtensionStrategyContext_ExceptionHandlingMode.htm)|
Режим обработки исключений, возникающий в методах расширений. Может быть
изменён в т.ч. в методе
[Tessa.Extensions.IExtensionTraceListener.NotifyException].  
[Executed](P_Tessa_Extensions_IExtensionStrategyContext_Executed.htm)|
Признак того, что метод экземпляра расширения не будет выполнен стандартным
образом, т.к. либо он уже был выполнен, либо его выполнение не требуется.  
[ExecutionContext](P_Tessa_Extensions_IExtensionStrategyContext_ExecutionContext.htm)|
Параметр метода, выполняемого для экземпляра расширения.  
[ExecutionKey](P_Tessa_Extensions_IExtensionStrategyContext_ExecutionKey.htm)|
Ключ, используемый для идентификации метода, выполняемого для экземпляра
расширения.  
[FilterContext](P_Tessa_Extensions_IExtensionStrategyContext_FilterContext.htm)|
Контекст фильтрации, используемый перед выполнением цепочки экземпляров
расширений.  
[Policies](P_Tessa_Extensions_IExtensionStrategyContext_Policies.htm)|
Контейнер политик, ассоциированных с типом или экземпяром расширения.
Возвращаемое значение никогда не равно null.  
[ResolvedExtension](P_Tessa_Extensions_IExtensionStrategyContext_ResolvedExtension.htm)|
Полученный экземпляр расширения или null, если экземпляр ещё не был получен.  
[ResolveKey](P_Tessa_Extensions_IExtensionStrategyContext_ResolveKey.htm)|
Ключ, используемый для идентификации экземпляра расширения, или null, если
контекст построен для типа расширения, а не для экземпляра.  
[StopExecution](P_Tessa_Extensions_IExtensionStrategyContext_StopExecution.htm)|
Признак того, что запрошена остановка выполнения цепочки расширений. Т.е.
текущее выполняемое расширение станет последним. При этом ошибок не
выбрасывается.  
[TraceContext](P_Tessa_Extensions_IExtensionStrategyContext_TraceContext.htm)|
Контекст трассировки, используемый для хранения информации между сообщениями
трассировки.  
##  __См. также
#### Ссылки
[IExtensionStrategyContext -
](T_Tessa_Extensions_IExtensionStrategyContext.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
