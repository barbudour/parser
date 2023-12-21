# ExtensionContainer.ResolveExecutorAsync - метод
##  __Список перегрузок
[ResolveExecutorAsync<TExtension>(CancellationToken)](M_Tessa_Extensions_ExtensionContainer_ResolveExecutorAsync__1_1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений. Метод никогда не возвращает null. Если тип
расширения не был зарегистрирован в контейнере, то метод не выбрасывает
исключение, а возвращает объект, не выполняющий действий.  
---|---  
[ResolveExecutorAsync<TExtension>(Boolean,
CancellationToken)](M_Tessa_Extensions_ExtensionContainer_ResolveExecutorAsync__1.htm)|
Возвращает объект, выполняющий расширения заданного типа и определяющий время
жизни экземпляров расширений. Метод никогда не возвращает null.
Если тип расширения не был зарегистрирован в контейнере, то метод не
выбрасывает исключение, а возвращает объект, не выполняющий действий.
Обращение к созданному объекту запрещено из разных потоков, используйте
перегрузку с параметром synchronized, если выполнение цепочек расширений
возможно из разных потоков.  
##  __См. также
#### Ссылки
[ExtensionContainer - ](T_Tessa_Extensions_ExtensionContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
