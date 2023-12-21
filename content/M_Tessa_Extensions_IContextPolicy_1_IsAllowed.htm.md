# IContextPolicy<TContext>.IsAllowed - метод
Признак того, что политика выполняется для указанного контекста.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool IsAllowed(
    	IExtension extension,
    	TContext context
    )
VB __Копировать
     Function IsAllowed ( 
    	extension As IExtension,
    	context As TContext
    ) As Boolean
C++ __Копировать
     bool IsAllowed(
    	IExtension^ extension, 
    	TContext context
    )
F# __Копировать
     abstract IsAllowed : 
            extension : IExtension * 
            context : 'TContext -> bool 
#### Параметры
extension [IExtension](T_Tessa_Extensions_IExtension.htm)
    Расширение, для которого выполняется проверка.
context [TContext](T_Tessa_Extensions_IContextPolicy_1.htm)
    Проверяемый контекст расширений.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если политика выполняется для указанного контекста; false в противном
случае.
## __См. также
#### Ссылки
[IContextPolicy<TContext> \- ](T_Tessa_Extensions_IContextPolicy_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
