# ExtensionContainer.TryResolveExecutorAsync - метод
##  __Список перегрузок
[TryResolveExecutorAsync<TExtension>(CancellationToken)](M_Tessa_Extensions_ExtensionContainer_TryResolveExecutorAsync__1_1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений, или null, если тип расширений не был
зарегистрирован.  
---|---  
[TryResolveExecutorAsync<TExtension>(Boolean,
CancellationToken)](M_Tessa_Extensions_ExtensionContainer_TryResolveExecutorAsync__1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений, или null, если тип расширений не был
зарегистрирован.
Обращение к созданному объекту запрещено из разных потоков, используйте
перегрузку с параметром synchronized, если выполнение цепочек расширений
возможно из разных потоков.  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
